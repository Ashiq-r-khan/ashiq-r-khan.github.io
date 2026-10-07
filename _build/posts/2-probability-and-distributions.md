slug: probability-and-distributions
title: Probability and distributions for public health
series: Statistics for Public Health
part: 2
date: 7 October 2026
iso: 2026-10-07
standfirst: Risk, odds and conditional probability, why a positive test can still be wrong most of the time, and how to match your data to the right distribution.
excerpt: Risk, odds and conditional probability, Bayes' theorem for diagnostic tests, and the binomial, Poisson, negative binomial and normal distributions, with worked public health examples.
---
This is the second part of my study notes on statistics for public health. [Part 1](descriptive-statistics.html) covered descriptive statistics, and [Part 3](inferential-statistics.html) covers inference. The layout is the same as before: a definition in simple words, the formula, a worked example, and what it means for a decision. The labels and symbols are explained [at the start of Part 1](descriptive-statistics.html#how-to-read).

Probability is the language of uncertainty. Public health uses it every day under other names: risk, prevalence, sensitivity, survival. Distributions are the standard patterns that data follow, and they decide which model you use later.

## What probability means {#what}

::: simple
**Probability** is a number between 0 and 1 that says how likely something is. 0 means it cannot happen. 1 means it is certain. 0.24 means it happens about 24 times in every 100.
:::

In public health almost every probability is estimated from data as a **relative frequency**: the number of times the event happened divided by the number of chances it had to happen.

$$P(\text{event})=\frac{\text{number of people with the event}}{\text{number of people who could have had it}}$$

This is the same as a proportion from [Part 1](descriptive-statistics.html#rates). When the event is a disease, the probability is called **risk**. The basic vocabulary:

| Term | Meaning in simple words | Example |
|---|---|---|
| Experiment or trial | Any process with an uncertain result | Testing one person for dengue |
| Outcome | One possible result | Positive |
| Sample space | The list of all possible outcomes | {Positive, Negative} |
| Event | The outcome, or set of outcomes, you are interested in | "The test is positive" |
| Complement, written $A^c$ or "not A" | Everything that is not event A | "The test is not positive" |

## The basic rules of probability {#rules}

All of the rules can be read from one table. The example below is used for the next three sections.

::: example illus Running example: smoking and hypertension
A survey of 1,000 adults records smoking status and hypertension.

| | Hypertension (H) | No hypertension | Total |
|---|---:|---:|---:|
| Smoker (S) | 90 | 210 | 300 |
| Non-smoker | 140 | 560 | 700 |
| Total | 230 | 770 | 1,000 |

From the totals: $P(H)$ = 230/1,000 = 0.23 and $P(S)$ = 300/1,000 = 0.30.
:::

| Rule | Formula | In the example |
|---|---|---|
| Range | $0\le P(A)\le 1$ | All probabilities in the table are between 0 and 1 |
| Complement | $P(\text{not }A)=1-P(A)$ | P(no hypertension) = 1 − 0.23 = 0.77 |
| Joint probability ("and") | $P(A\text{ and }B)$, written $P(A\cap B)$ | P(H and S) = 90/1,000 = 0.09 |
| Addition rule ("or") | $P(A\text{ or }B)=P(A)+P(B)-P(A\text{ and }B)$ | P(H or S) = 0.23 + 0.30 − 0.09 = 0.44 |
| Addition rule, mutually exclusive events | $P(A\text{ or }B)=P(A)+P(B)$ | Used when A and B cannot both happen (see below) |

Why subtract in the addition rule? The 90 people who are both smokers and hypertensive are counted once in the 230 and again in the 300. Subtracting removes the double count: 230 + 300 − 90 = 440 people have at least one of the two.

::: simple
**Mutually exclusive** events cannot happen together. A person's blood group cannot be both A and B at once, so P(A or B) is a simple sum. "Or" in probability always means "one, or the other, or both".
:::

## Conditional probability and independence {#conditional}

::: simple
**Conditional probability** is the probability of an event inside a specific group. $P(A\mid B)$ is read "the probability of A given B". You stop looking at everybody and look only at the people in group B.
:::

$$P(A\mid B)=\frac{P(A\text{ and }B)}{P(B)}$$

::: example illus Worked example (same table)
- Risk of hypertension among smokers: $P(H\mid S)$ = 90/300 = **0.30**
- Risk of hypertension among non-smokers: $P(H\mid\text{not }S)$ = 140/700 = **0.20**
- Share of hypertensive people who smoke: $P(S\mid H)$ = 90/230 = **0.39**

The first two are the numbers epidemiology compares. Their ratio, 0.30 ÷ 0.20 = 1.5, is the **risk ratio**: in this survey smokers have 1.5 times the risk of hypertension.
:::

::: mistake
**$P(A\mid B)$ is not the same as $P(B\mid A)$.** Above, 30% of smokers have hypertension, but 39% of hypertensive people smoke. Swapping the two is the single most common probability error in medicine. The classic case: "most people with lung cancer are smokers" does not mean "most smokers get lung cancer".
:::

### Independence

::: simple
Two events are **independent** when knowing that one happened tells you nothing about the other. In symbols, $P(A\mid B)=P(A)$.
:::

In the example $P(H)$ = 0.23 but $P(H\mid S)$ = 0.30. Knowing that a person smokes changes the probability of hypertension, so the two are **not independent**. They are associated. Testing whether two variables are independent is exactly what the [chi-square test in Part 3](inferential-statistics.html#chi-square) does.

### The multiplication rule

| Case | Formula |
|---|---|
| Any two events | $P(A\text{ and }B)=P(A)\times P(B\mid A)$ |
| Independent events | $P(A\text{ and }B)=P(A)\times P(B)$ |

::: example real Worked example: "at least one"
BDHS 2022 found 24% of under-5 children stunted. Choose 5 children at random from different households, so they are independent.

- P(one child is not stunted) = 1 − 0.24 = 0.76
- P(none of the 5 is stunted) = 0.76 × 0.76 × 0.76 × 0.76 × 0.76 = $0.76^5$ = 0.254
- P(at least one is stunted) = 1 − 0.254 = **0.746**
:::

::: remember
"At least one" is always easiest through the complement: $P(\text{at least one})=1-P(\text{none})=1-(1-p)^n$. The same formula explains why running many tests produces false positives: with a 5% false positive chance per test, 10 independent tests on a healthy person give 1 − $0.95^{10}$ = 40% chance of at least one false alarm.
:::

::: mistake
**Multiplying probabilities of events that are not independent.** Children in the same household share food, water and income, so their stunting status is related. Cases of an infectious disease are not independent either: one case makes the next more likely. Many statistical methods assume independence, and cluster surveys and outbreak data break that assumption.
:::

## Probability and odds {#odds}

::: simple
**Odds** compare the chance that something happens with the chance that it does not. If 1 person in 5 has a disease, the probability is 1/5 = 0.20, and the odds are 1 to 4 = 0.25.
:::

$$\text{odds}=\frac{p}{1-p}\qquad p=\frac{\text{odds}}{1+\text{odds}}$$

| Probability $p$ | 0.01 | 0.10 | 0.20 | 0.24 | 0.50 | 0.80 | 0.90 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Odds $p/(1-p)$ | 0.010 | 0.111 | 0.25 | 0.316 | 1.00 | 4.00 | 9.00 |

Two things to notice. When the probability is small (under about 10%), odds and probability are almost equal. As probability grows, odds become much larger than probability. Odds matter because logistic regression, the main model for yes/no outcomes in public health, works with odds and reports **odds ratios**. For a common outcome, an odds ratio is further from 1 than the risk ratio, so reading an odds ratio as if it were a risk ratio exaggerates the effect.

::: own
My [diabetes readmission analysis](../project.html?p=diabetes) shows the gap. Of patients with 3 or more prior inpatient stays, 26.5% were readmitted within 30 days, against 8.1% of patients with none. As a risk ratio that is 26.5 ÷ 8.1 = 3.3. As an odds ratio it is (0.265 ÷ 0.735) ÷ (0.081 ÷ 0.919) = 4.1. Readmission is not rare in the first group, so the two numbers move apart. After adjustment in the logistic regression the odds ratio was 3.61 (3.09 to 4.23).
:::

## Bayes' theorem and diagnostic tests {#bayes}

::: simple
**Bayes' theorem** is the rule for turning $P(B\mid A)$ into $P(A\mid B)$. It answers the question a patient actually asks: "My test is positive. What is the chance I really have the disease?"
:::

$$P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}$$

$$\text{where}\quad P(B)=P(B\mid A)\,P(A)+P(B\mid\text{not }A)\,P(\text{not }A)$$

The second formula is the **law of total probability**: the overall probability of B is a weighted average over the groups. In the smoking example, $P(H)$ = 0.30 × 0.30 + 0.20 × 0.70 = 0.09 + 0.14 = 0.23, which matches the table.

### The four numbers that describe a test

| | Disease present | Disease absent |
|---|---|---|
| Test positive | True positive (TP) | False positive (FP) |
| Test negative | False negative (FN) | True negative (TN) |

| Measure | Formula | Question it answers |
|---|---|---|
| **Sensitivity** | $\dfrac{TP}{TP+FN}$ | Of the people who have the disease, what share does the test catch? $P(\text{positive}\mid\text{disease})$ |
| **Specificity** | $\dfrac{TN}{TN+FP}$ | Of the people who are healthy, what share does the test correctly clear? $P(\text{negative}\mid\text{no disease})$ |
| **Positive predictive value (PPV)** | $\dfrac{TP}{TP+FP}$ | Of the people who test positive, what share truly have the disease? $P(\text{disease}\mid\text{positive})$ |
| **Negative predictive value (NPV)** | $\dfrac{TN}{TN+FN}$ | Of the people who test negative, what share are truly healthy? $P(\text{no disease}\mid\text{negative})$ |

Sensitivity and specificity belong to the test. PPV and NPV depend on the test **and** on how common the disease is in the people being tested. Prevalence is the starting probability, also called the *prior* or *pre-test probability*.

::: example illus Worked example: screening 10,000 people
A rapid test has sensitivity 90% and specificity 95%. It is used for mass screening in a community where 1% of people have the disease. Count people instead of using the formula. This "natural frequency" method avoids most errors.

1. Of 10,000 people, 1% have the disease: 100 diseased and 9,900 healthy.
2. Sensitivity 90%: the test catches 90 of the 100 diseased (true positives) and misses 10 (false negatives).
3. Specificity 95%: the test correctly clears 9,405 of the 9,900 healthy (true negatives) and wrongly flags 5%, which is 495 (false positives).

| | Disease | No disease | Total |
|---|---:|---:|---:|
| Test positive | 90 | 495 | 585 |
| Test negative | 10 | 9,405 | 9,415 |
| Total | 100 | 9,900 | 10,000 |

PPV = 90 ÷ 585 = **15.4%**. NPV = 9,405 ÷ 9,415 = **99.9%**.

A test that is "90% sensitive and 95% specific" sounds excellent, yet 85 of every 100 positive results here are false. The reason is simple: healthy people are so numerous that even a 5% error among them (495) is far bigger than all the true cases (90).

Now use the same test in a fever clinic during an outbreak, where 30% of patients have the disease: 3,000 diseased give 2,700 true positives, and 7,000 healthy give 350 false positives. PPV = 2,700 ÷ 3,050 = **88.5%**. Same test, same accuracy, very different meaning.
:::

| Prevalence in the group tested | 0.1% | 1% | 5% | 10% | 30% | 50% |
|---|---:|---:|---:|---:|---:|---:|
| PPV (sensitivity 90%, specificity 95%) | 1.8% | 15.4% | 48.6% | 66.7% | 88.5% | 94.7% |
| NPV | 99.99% | 99.9% | 99.4% | 98.8% | 95.7% | 90.5% |

[[fig:ppv|Predictive values depend on prevalence|(sensitivity 90%, specificity 95%). In low-prevalence screening, a positive result needs a confirmatory test. In high-prevalence settings, a negative result is the one to be careful with.]]

**Likelihood ratios** combine sensitivity and specificity into one number that does not depend on prevalence. The positive likelihood ratio is sensitivity ÷ (1 − specificity) = 0.90 ÷ 0.05 = 18: a positive result is 18 times more likely in a diseased person than in a healthy one. The negative likelihood ratio is (1 − sensitivity) ÷ specificity = 0.10 ÷ 0.95 = 0.11.

::: remember
- A highly **sensitive** test is good for ruling disease *out* when it is negative. Use it for screening, when missing a case is costly.
- A highly **specific** test is good for ruling disease *in* when it is positive. Use it for confirmation, when a false positive is costly.
- Screening a low-risk population produces mostly false positives, however good the test.
:::

## Random variables, expected value and variance {#random-variables}

::: simple
A **random variable** is a number whose value depends on chance, such as "number of dengue cases next week" or "birth weight of the next baby". A **discrete** random variable takes separate values you can count (0, 1, 2, ...). A **continuous** random variable can take any value in a range (2.31 kg, 2.317 kg, ...).
:::

| Term | Meaning in simple words |
|---|---|
| Probability distribution | The complete list of values a random variable can take, with the probability of each. |
| Probability mass function (PMF) | For a discrete variable: the probability of each exact value, $P(X=x)$. The probabilities add to 1. |
| Probability density function (PDF) | For a continuous variable: a curve. Probability is the *area under the curve* between two values. The total area is 1. The probability of any single exact value is zero. |
| Cumulative distribution function (CDF) | The probability of being at or below a value, $P(X\le x)$. Percentiles are read from the CDF. |
| Expected value $E(X)$ or $\mu$ | The long-run average: what you would get on average if the situation were repeated many times. |
| Variance $\text{Var}(X)$ or $\sigma^2$ | The expected squared distance from the expected value. Its square root is the SD. |

$$E(X)=\sum x\,P(X=x)\qquad \text{Var}(X)=\sum(x-\mu)^2\,P(X=x)=E(X^2)-[E(X)]^2$$

::: example illus Worked example: diarrhoea cases per household
Let $X$ be the number of children with diarrhoea in a household in a given week.

| $x$ | 0 | 1 | 2 | 3 | Sum |
|---|---:|---:|---:|---:|---:|
| $P(X=x)$ | 0.50 | 0.30 | 0.15 | 0.05 | 1.00 |
| $x\times P$ | 0 | 0.30 | 0.30 | 0.15 | 0.75 |
| $x^2\times P$ | 0 | 0.30 | 0.60 | 0.45 | 1.35 |

$E(X)$ = **0.75 cases per household**. $\text{Var}(X)$ = 1.35 − 0.75² = 0.79, so SD = 0.89. No household has 0.75 of a case. The expected value is for planning: 2,000 households would be expected to produce about 2,000 × 0.75 = 1,500 cases a week, which tells you how much oral rehydration solution to stock.
:::

## Bernoulli and binomial distributions {#binomial}

::: simple
A **Bernoulli trial** is one event with two possible results, for example one person who is either vaccinated or not. The **binomial distribution** describes how many "yes" results you get when you repeat a Bernoulli trial $n$ times.
:::

Use the binomial when four conditions hold:

- There is a fixed number of trials, $n$.
- Each trial has only two outcomes (yes or no).
- The probability of "yes", $p$, is the same for every trial.
- The trials are independent.

$$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}\qquad\text{where}\qquad\binom{n}{k}=\frac{n!}{k!\,(n-k)!}$$

$\binom{n}{k}$ is the number of different ways to choose which $k$ of the $n$ people are the "yes" ones. $n!$ (n factorial) means $n\times(n-1)\times\cdots\times 1$.

| Distribution | Mean | Variance | Standard deviation |
|---|---|---|---|
| Bernoulli($p$) | $p$ | $p(1-p)$ | $\sqrt{p(1-p)}$ |
| Binomial($n,p$) | $np$ | $np(1-p)$ | $\sqrt{np(1-p)}$ |

::: example real Worked example: stunted children in a sample
With national stunting at 24% (BDHS 2022), a field worker measures 10 randomly chosen under-5 children. $n$ = 10, $p$ = 0.24.

Probability that exactly 2 are stunted:

$$P(X=2)=\binom{10}{2}(0.24)^2(0.76)^8=45\times 0.0576\times 0.1113=0.288$$

| Stunted children $k$ | 0 | 1 | 2 | 3 | 4 | 5 or more |
|---|---:|---:|---:|---:|---:|---:|
| Probability | 0.064 | 0.203 | 0.288 | 0.243 | 0.134 | 0.067 |

Expected number = $np$ = 10 × 0.24 = **2.4**. SD = $\sqrt{10\times 0.24\times 0.76}$ = 1.35.

Reading it: finding **0** stunted children in a sample of 10 happens 6.4% of the time even when the true level is 24%. A small sample can easily mislead. And if a village sample of 10 has 5 or more stunted children, that is unusual (6.7%) under the national rate and suggests the village is worse than average.
:::

[[fig:binomial|Binomial distributions with p = 0.24.|With 10 children the shape is right-skewed. With 50 children it is close to a symmetric bell centred on 12. This is the basis of the normal approximation described further down.]]

**Where it is used**: any count of people with a yes/no characteristic out of a fixed number: positives among those tested, deaths among patients treated, vaccinated children among those surveyed. Every proportion and percentage you report rests on the binomial distribution, and so does logistic regression.

## The Poisson distribution {#poisson}

::: simple
The **Poisson distribution** describes how many times an event happens in a fixed amount of time, area or population, when events occur independently at a steady average rate. It has one parameter, $\lambda$ (lambda), the average number of events.
:::

Use the Poisson when you are counting events (0, 1, 2, ...) with no fixed upper limit, the events happen independently of each other, and the average rate is constant over the period.

$$P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}\qquad\text{Mean}=\lambda\qquad\text{Variance}=\lambda$$

$e$ is the constant 2.718. The key property is that **the mean equals the variance**.

::: example illus Worked example: snakebite admissions
A district hospital admits an average of 3 snakebite patients a week, so $\lambda$ = 3.

Probability of exactly 5 admissions next week:

$$P(X=5)=\frac{e^{-3}\times 3^5}{5!}=\frac{0.0498\times 243}{120}=0.101$$

| Admissions $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 or more |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Probability | 0.050 | 0.149 | 0.224 | 0.224 | 0.168 | 0.101 | 0.050 | 0.034 |

**Using it for stock**: if the hospital keeps antivenom for 6 patients a week, it runs short only when 7 or more arrive, which is 3.4% of weeks.

**Using it for surveillance**: 8 or more admissions in one week has probability 1.2% if nothing has changed. A week with 8 admissions is therefore a signal worth investigating (flooding? a change in farming activity?). Outbreak detection systems work on this logic: compare the observed count with what the usual rate predicts.
:::

[[fig:poisson|Poisson distributions.|For rare events (small λ) the distribution is strongly right-skewed and zero is common. As λ grows it becomes symmetric and bell-shaped.]]

### Rates and exposure

Counts depend on how many people were watched and for how long. A Poisson model handles this by writing the expected count as rate × exposure:

$$\lambda=\text{rate}\times\text{person-time}$$

If the tuberculosis rate is 40 per 100,000 people per year, a town of 250,000 expects 40 × 2.5 = 100 cases a year and a town of 25,000 expects 10. In Poisson regression the exposure enters as the "offset". That is a topic for later notes on regression, but the idea starts here.

**Binomial or Poisson?** If each person can only be a yes or a no and you know how many people there were, it is binomial. If you are counting events with no fixed ceiling, or the event is rare in a very large population ($n$ large, $p$ small), use Poisson with $\lambda=np$.

## The negative binomial distribution {#negative-binomial}

Real public health counts usually break the Poisson rule that the variance equals the mean. Cases cluster in households, some areas have much higher risk than others, and infectious cases cause further cases. The result is **overdispersion**: the variance is larger than the mean.

::: simple
The **negative binomial distribution** is a Poisson distribution with extra spread. It has the same kind of mean, $\mu$, plus a second parameter, $k$, that controls the extra variation. A small $k$ means strong overdispersion. As $k$ becomes very large, the negative binomial turns back into the Poisson.
:::

$$\text{Mean}=\mu\qquad\text{Variance}=\mu+\frac{\mu^2}{k}$$

::: example real Real example: superspreading in COVID-19
Early in the pandemic each COVID-19 case infected about 2.5 other people on average. If transmission followed a Poisson distribution, almost every case would infect between 0 and 6 people. That is not what happened. Endo and colleagues (Wellcome Open Research, 2020) fitted a negative binomial distribution and estimated $k$ = 0.1 (95% credible interval 0.05 to 0.2) for a mean of 2.5.

| With mean 2.5 new infections per case | Poisson | Negative binomial, k = 0.1 |
|---|---:|---:|
| Variance | 2.5 | 2.5 + 2.5² ÷ 0.1 = 65 |
| Cases that infect nobody | 8% | 72% |
| Cases that infect 10 or more people | 0.03% | 7.7% |

The study concluded that about 80% of secondary infections may have been caused by roughly 10% of infectious people. The average was the same under both models, but the public health message is completely different: preventing large gatherings and tracing clusters matters far more than treating every case as equally infectious.
:::

[[fig:negbin|Same mean, different story.|Both distributions average 2.5 new infections per case. The negative binomial puts most cases at zero and a few far out in the tail.]]

::: remember
For count data, compare the mean with the variance first. If the variance is clearly larger than the mean, the data are overdispersed. A Poisson model will then give standard errors that are too small and p-values that are too optimistic. Use the negative binomial. The usual path for count data is: Poisson, check overdispersion, negative binomial.
:::

::: own
Weekly dengue admissions are counts of this kind. One of the five forecasting models in my [dengue forecasting project](../project.html?p=dengue) is a negative binomial model.
:::

## The normal distribution {#normal}

::: simple
The **normal distribution** is the symmetric bell-shaped curve. Most values are near the mean, and values become rarer the further they are from it. It is fully described by two numbers: the mean $\mu$ (where the centre is) and the standard deviation $\sigma$ (how wide it is). It is written $N(\mu,\sigma^2)$.
:::

**Properties**: symmetric around the mean; mean = median = mode; the curve never quite touches zero; the total area under it is 1.

[[fig:normal|The 68-95-99.7 rule.|In any normal distribution about 68% of values lie within 1 SD of the mean, 95% within 2 SD (exactly 1.96 SD) and 99.7% within 3 SD.]]

The **standard normal distribution** has mean 0 and SD 1. Any normal variable can be converted to it with the [z-score from Part 1](descriptive-statistics.html#z-score), $z=(x-\mu)/\sigma$, and then one table (the z-table, [in Part 3](inferential-statistics.html#tables)) gives every probability.

| $z$ | −1.96 | −1.645 | −1 | 0 | 1 | 1.28 | 1.645 | 1.96 | 2.576 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Area to the left, $P(Z\le z)$ | 0.025 | 0.050 | 0.159 | 0.500 | 0.841 | 0.900 | 0.950 | 0.975 | 0.995 |

::: example illus Worked example: blood pressure in a population
Suppose systolic blood pressure in adults is normal with mean 125 mmHg and SD 15 mmHg.

- **What share have 140 or above?** $z$ = (140 − 125)/15 = 1.0. The area to the left of 1.0 is 0.841, so the area to the right is 1 − 0.841 = **15.9%**.
- **What share lie between 110 and 140?** That is from $z$ = −1 to $z$ = +1: **68.3%**.
- **What range holds the middle 95%?** 125 ± 1.96 × 15 = **95.6 to 154.4 mmHg**.
- **What is the 90th percentile?** The z-value with 90% to its left is 1.28, so 125 + 1.28 × 15 = **144.2 mmHg**.
:::

**Where it is used in public health**:

- **Reference ranges.** A laboratory "normal range" is usually the middle 95% of healthy people, mean ± 1.96 SD. By construction, 5% of healthy people fall outside it.
- **Growth standards.** Stunting, wasting and underweight are defined by z-scores ([Part 1](descriptive-statistics.html#z-score)).
- **Statistical inference.** Sample means and sample proportions follow a normal distribution when samples are large, even when the raw data do not. This is the [central limit theorem in Part 3](inferential-statistics.html#clt), and it is the main reason the normal distribution matters.

### Normal approximation to the binomial

When $n$ is large enough that both $np$ and $n(1-p)$ are at least 10 (some books say 5), a binomial count is approximately normal with mean $np$ and SD $\sqrt{np(1-p)}$. For a survey of 400 children with $p$ = 0.24: mean 96 stunted children, SD 8.5. About 95% of such surveys would find between 96 − 1.96 × 8.5 = 79 and 96 + 1.96 × 8.5 = 113 stunted children.

::: mistake
**Assuming data are normal without checking.** Many health variables are not: length of stay, cost, counts, titres and waiting times are skewed. Check with a histogram and a Q-Q plot (a plot where normal data fall on a straight line). Also remember that "normal" is only the name of a curve. It does not mean healthy or usual.
:::

## Exponential and time-to-event distributions {#exponential}

::: simple
The **exponential distribution** describes the waiting time until the next event when events happen at a constant average rate. It is the continuous partner of the Poisson: Poisson counts the events, exponential measures the gaps between them.
:::

$$P(T>t)=e^{-\lambda t}\qquad\text{Mean waiting time}=\frac{1}{\lambda}\qquad\text{Median}=\frac{\ln 2}{\lambda}$$

::: example illus Worked example (continuing the snakebite example)
With 3 admissions a week, the mean gap between admissions is 1/3 of a week, or 2.3 days. The probability of going a whole week with no admission is $e^{-3}$ = 0.050, exactly the Poisson probability of 0 admissions in the [snakebite example](#poisson). The median gap is ln 2/3 weeks = 1.6 days, shorter than the mean, because the distribution is right-skewed.
:::

The exponential distribution is the simplest model in **survival analysis**. Its $\lambda$ is the **hazard**: the instantaneous risk of the event for someone who has not had it yet. The exponential assumes the hazard never changes, which is called being "memoryless". Real hazards change over time, so survival analysis uses more flexible relatives:

| Distribution | Simple description | Used for |
|---|---|---|
| Weibull | Like the exponential, but the hazard can rise or fall over time | Survival after diagnosis, time to relapse |
| Gamma | A flexible right-skewed distribution for positive values | Health-care costs, serial intervals, incubation periods |
| Log-normal | The logarithm of the variable is normal | Incubation periods, antibody titres, exposure concentrations |

::: example real Real example
Incubation periods of infectious diseases are right-skewed, and the log-normal distribution has been the standard description since Sartwell's work in 1950. Lauer and colleagues fitted a log-normal model to COVID-19 incubation data in 2020 to obtain the median of 5.1 days and the 97.5th percentile of 11.5 days quoted in [Part 1](descriptive-statistics.html#percentiles).
:::

## The distributions behind statistical tests: t, chi-square and F {#test-distributions}

Three more distributions appear in [Part 3](inferential-statistics.html). They do not describe raw data. They describe how a *test statistic* behaves when the null hypothesis is true, and they are all built from the normal distribution.

| Distribution | Simple description | Used in |
|---|---|---|
| **Student's t** | Looks like the standard normal but with heavier tails. The extra width accounts for estimating the SD from a small sample. Its shape depends on the degrees of freedom (df). Above about 30 df it is almost identical to the normal. | t-tests, confidence intervals for means, regression coefficients |
| **Chi-square** ($\chi^2$) | The distribution of a sum of squared standard normal values. Always positive and right-skewed. | Chi-square tests for categorical data, tests of model fit |
| **F** | The ratio of two variances. Always positive and right-skewed. | ANOVA, comparing regression models |

[[fig:t|The t distribution compared with the normal.|With few degrees of freedom the tails are heavier, so the critical value is larger than 1.96 and confidence intervals are wider.]]

## Choosing a distribution for your data {#choosing}

| Your outcome | Distribution | Public health example | Regression model that follows |
|---|---|---|---|
| Yes or no for one person | Bernoulli | Has diabetes or not | Logistic regression |
| Number of "yes" out of n | Binomial | Positives out of 200 tested | Logistic regression |
| Count of events, variance about equal to the mean | Poisson | Cases per district per month | Poisson regression |
| Count of events, variance larger than the mean | Negative binomial | Dengue cases per ward, clinic visits per person | Negative binomial regression |
| Continuous, symmetric | Normal | Blood pressure, haemoglobin, height | Linear regression |
| Continuous, positive, right-skewed | Log-normal or gamma | Cost, length of stay, titre | Linear regression on the log, or gamma regression |
| Time until an event | Exponential, Weibull | Time to death, time to recovery | Survival analysis, Cox regression |

::: mistake Common mistakes in probability
- Confusing $P(A\mid B)$ with $P(B\mid A)$. Sensitivity is not PPV. "95% of patients had the risk factor" is not "95% of people with the risk factor become patients".
- Ignoring the base rate. Judging a positive test without asking how common the disease is.
- Assuming independence for people in the same household, village or outbreak.
- The gambler's fallacy. After three quiet weeks an outbreak is not "due". Independent events have no memory.
- Using the Poisson for overdispersed counts without checking the variance against the mean.
- Treating probability 0.05 as impossible. A 1 in 20 event happens all the time when thousands of districts, weeks or tests are examined.
:::

## Check yourself {#check}

Try each question first, then open it to see the answer.

??? In a village 40% of adults chew betel nut, 15% have oral lesions, and 10% have both. What is the probability that an adult has at least one of the two? What is the probability of oral lesions among chewers?
At least one: 0.40 + 0.15 − 0.10 = 0.45. Among chewers: 0.10 ÷ 0.40 = 0.25, compared with 15% overall, so the two are associated.
???

??? A test has sensitivity 95% and specificity 90%. Prevalence is 2%. Out of 1,000 people tested, how many positive results are true?
Diseased: 20, of whom 19 test positive. Healthy: 980, of whom 10% = 98 test positive. PPV = 19 ÷ 117 = 16%. About 5 of every 6 positives are false.
???

??? A health centre sees on average 2 measles cases a month. Which distribution describes the monthly count, and what is the probability of a month with no cases?
Poisson with $\lambda$ = 2. P(0) = $e^{-2}$ = 0.135.
???

??? Weekly malaria counts in 50 unions have mean 4 and variance 22. Which distribution fits better, Poisson or negative binomial?
Negative binomial. The variance is more than five times the mean, so the data are overdispersed.
???

??? Haemoglobin in adult women is normal with mean 12.5 g/dL and SD 1.25. Anaemia is defined as below 12.0. What share are anaemic?
$z$ = (12.0 − 12.5) ÷ 1.25 = −0.4. The area to the left of −0.4 is 0.345, so about 34.5%.
???

??? If the probability of an outcome is 0.75, what are the odds?
0.75 ÷ 0.25 = 3, or "3 to 1".
???

## Formula sheet {#formulas}

| Quantity | Formula |
|---|---|
| Complement | $P(\text{not }A)=1-P(A)$ |
| Addition rule | $P(A\text{ or }B)=P(A)+P(B)-P(A\text{ and }B)$ |
| Conditional probability | $P(A\mid B)=P(A\text{ and }B)/P(B)$ |
| At least one in n | $1-(1-p)^n$ |
| Odds | $\text{odds}=p/(1-p)$, $p=\text{odds}/(1+\text{odds})$ |
| Bayes' theorem | $P(A\mid B)=P(B\mid A)\,P(A)/P(B)$ |
| Sensitivity, specificity | $TP/(TP+FN)$, $TN/(TN+FP)$ |
| PPV, NPV | $TP/(TP+FP)$, $TN/(TN+FN)$ |
| Expected value, variance | $E(X)=\sum x\,P(x)$, $\text{Var}(X)=E(X^2)-[E(X)]^2$ |
| Binomial | $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$; mean $np$, variance $np(1-p)$ |
| Poisson | $P(X=k)=e^{-\lambda}\lambda^k/k!$; mean $\lambda$, variance $\lambda$ |
| Negative binomial | mean $\mu$, variance $\mu+\mu^2/k$ |
| Exponential | $P(T>t)=e^{-\lambda t}$; mean $1/\lambda$ |

## Glossary {#glossary}

| Term | Meaning in simple words |
|---|---|
| Independence | Knowing one event tells you nothing about the other. |
| Odds | The chance that something happens divided by the chance that it does not. |
| Overdispersion | Count data whose variance is larger than the mean. |
| Sensitivity | The share of diseased people that a test correctly identifies. |
| Specificity | The share of healthy people that a test correctly identifies. |

## Sources {#sources}

1. Bangladesh Demographic and Health Survey 2022 (stunting 24%). NIPORT and ICF. [Key Indicators Report](https://dhsprogram.com/pubs/pdf/PR148/PR148.pdf).
2. COVID-19 overdispersion. Endo A. et al. [Estimating the overdispersion in COVID-19 transmission using outbreak sizes outside China](https://pmc.ncbi.nlm.nih.gov/articles/PMC7338915/). Wellcome Open Research, 2020; 5: 67.
3. COVID-19 incubation period. Lauer S.A. et al. The Incubation Period of Coronavirus Disease 2019 (COVID-19) From Publicly Reported Confirmed Cases. Annals of Internal Medicine, 2020; 172: 577-582.
