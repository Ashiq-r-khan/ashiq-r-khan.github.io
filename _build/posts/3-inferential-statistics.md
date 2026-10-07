slug: inferential-statistics
title: Inferential statistics for public health
series: Statistics for Public Health
part: 3
date: 7 October 2026
iso: 2026-10-07
standfirst: What a sample can tell you about a whole population, and how sure you can be. Standard errors, confidence intervals, p-values, power, sample size, and how to choose and report a test.
excerpt: What a sample can say about a population: standard errors, confidence intervals, p-values, power, sample size, choosing the right test and reporting the result, with worked public health examples.
---
This is the third part of my study notes on statistics for public health. [Part 1](descriptive-statistics.html) covered descriptive statistics and [Part 2](probability-and-distributions.html) covered probability and distributions. The layout is the same: a definition in simple words, the formula, a worked example, and what it means for a decision. The labels and symbols are explained [at the start of Part 1](descriptive-statistics.html#how-to-read).

Inferential statistics uses a sample to say something about the whole population, and attaches an honest measure of uncertainty to it. It has two tools: estimation (confidence intervals) and hypothesis testing (p-values).

## From sample to population {#sample-to-population}

::: simple
**Inference** means drawing a conclusion about a population from a sample. Because a sample is only part of the population, the conclusion always carries uncertainty. Inferential statistics measures that uncertainty.
:::

A sample result can differ from the truth for two very different reasons.

| | Sampling error (random error) | Bias (systematic error) |
|---|---|---|
| What it is | The luck of the draw. A different random sample would give a slightly different answer. | A flaw in how people were selected or measured that pushes the result in one direction. |
| Example | One survey of 400 children finds 22% stunted, another finds 26%. | Measuring only children who attend a clinic, who are sicker than average. |
| Fixed by a bigger sample? | Yes. It shrinks as n grows. | No. A bigger biased sample gives a more precise wrong answer. |
| Measured by statistics? | Yes: standard errors, confidence intervals, p-values. | No. It must be prevented by good study design. |

::: remember
Every confidence interval and p-value in this part assumes a random sample and measures sampling error only. None of them can detect or correct bias. That is why epidemiology (study design, bias, confounding) is a separate topic.
:::

## Sampling distributions and the standard error {#standard-error}

Imagine repeating a survey thousands of times, each time with a new random sample of the same size, and writing down the sample mean each time. Those means would differ a little from each other. The distribution of all those means is called the **sampling distribution** of the mean.

::: simple
The **standard error (SE)** is the standard deviation of the sampling distribution. It tells you how much a sample statistic would typically change from one sample to the next. A small SE means a precise estimate.
:::

$$\text{SE of a mean}=\frac{s}{\sqrt{n}}\qquad\text{SE of a proportion}=\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

| | Standard deviation (SD) | Standard error (SE) |
|---|---|---|
| Describes | How much individual people differ from each other | How precise the sample mean (or proportion) is |
| As n increases | Stays about the same | Gets smaller |
| Use it to | Describe your sample (Table 1) | Build confidence intervals and tests |

::: example illus Worked example: haemoglobin survey
A survey of 400 adolescent girls finds mean haemoglobin 11.2 g/dL with SD 1.6 g/dL.

SE = 1.6 ÷ √400 = 1.6 ÷ 20 = **0.08 g/dL**.

The SD says individual girls typically differ from the mean by 1.6. The SE says the sample mean of 11.2 would typically move by only 0.08 if the survey were repeated. Because of the square root, quadrupling the sample to 1,600 only halves the SE to 0.04.
:::

## The central limit theorem {#clt}

::: simple
The **central limit theorem (CLT)** says: if you take a large enough random sample, the sample mean follows an approximately normal distribution, whatever the shape of the original data. The sampling distribution is centred on the true population mean and its SD is the standard error.
:::

$$\bar{x}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right)\quad\text{approximately, when }n\text{ is large}$$

[[fig:clt|The central limit theorem in action|(simulated length-of-stay data). Individual stays are strongly right-skewed. Means of samples of 5 are less skewed. Means of samples of 30 are close to a narrow, symmetric bell centred on the population mean.]]

**Why this matters**: hospital stays, costs and counts are not normal, but the CLT lets us use normal-based confidence intervals and tests for their *means* and *proportions* as long as the sample is large enough.

**How large is "large enough"?** The common rule is $n\ge 30$. For strongly skewed data more is needed. For a proportion, the usual check is that the sample contains at least 10 people with the characteristic and at least 10 without it.

The **law of large numbers** is a related idea: as the sample grows, the sample mean gets closer to the true mean. The law of large numbers says the estimate becomes accurate. The CLT describes the shape of its remaining error.

## Estimation: point estimates and confidence intervals {#confidence-intervals}

::: simple
- A **point estimate** is a single best guess for the population value, such as "24% are stunted".
- A **confidence interval (CI)** is a range of values around the estimate that is likely to contain the true population value. A 95% CI is built by a method that captures the truth in 95 out of 100 repeated samples.
:::

Almost every confidence interval has the same structure:

$$\text{estimate}\;\pm\;\underbrace{\text{critical value}\times\text{standard error}}_{\text{margin of error}}$$

| Confidence level | 90% | 95% | 99% |
|---|---:|---:|---:|
| Critical value $z$ | 1.645 | 1.96 | 2.576 |

### Confidence interval for a mean

$$\bar{x}\pm t_{n-1}\times\frac{s}{\sqrt{n}}$$

The critical value comes from the t distribution with $n-1$ degrees of freedom, because the SD is estimated from the sample. For large samples it is almost 1.96.

::: example illus Worked example: haemoglobin
- n = 400, mean 11.2, SD 1.6, SE 0.08. Critical value 1.97. 95% CI = 11.2 ± 1.97 × 0.08 = **11.04 to 11.36 g/dL**.
- n = 25 with the same mean and SD: SE = 1.6 ÷ 5 = 0.32. Critical value for 24 df = 2.064. 95% CI = 11.2 ± 2.064 × 0.32 = **10.54 to 11.86 g/dL**.

The small study gives the same estimate but a much wider interval. If the cut-off for anaemia is 12.0 g/dL, both intervals lie entirely below it, so even the small study supports the statement that mean haemoglobin in this group is below the cut-off.
:::

### Confidence interval for a proportion

$$\hat{p}\pm z\times\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

::: example illus Worked example: a district stunting survey
A district survey measures 400 children and finds 96 stunted, so $\hat{p}$ = 0.24.

SE = $\sqrt{0.24\times 0.76/400}$ = 0.0214. Margin of error = 1.96 × 0.0214 = 0.042. 95% CI = **19.8% to 28.2%**.

| Sample size | Standard error | Margin of error | 95% confidence interval |
|---:|---:|---:|---:|
| 100 | 4.3% | ± 8.4% | 15.6% to 32.4% |
| 400 | 2.1% | ± 4.2% | 19.8% to 28.2% |
| 1,600 | 1.1% | ± 2.1% | 21.9% to 26.1% |

To halve the margin of error you need four times the sample. Precision is expensive.
:::

::: note
This simple formula is called the Wald interval. It works poorly when the sample is small or the proportion is near 0% or 100%. Statistical software then uses the Wilson or exact (Clopper-Pearson) interval. Complex surveys such as BDHS also adjust the SE for clustering and weighting (see the [design effect](#sample-size) below).
:::

### What a 95% confidence interval means

[[fig:ci|Forty surveys of the same population|(simulated, true stunting 24%, 400 children each). Each survey gives a different estimate and a different interval. Most intervals contain the true value and a few miss. In the long run 95% contain it. In real life you run one survey and never know whether yours is one of the misses.]]

| Correct | Incorrect |
|---|---|
| "We are 95% confident that the true stunting prevalence in the district is between 19.8% and 28.2%." | "95% of children have a value between 19.8% and 28.2%." (A CI is about the population average, not about individuals.) |
| "The method used produces intervals that contain the true value 95% of the time." | "There is a 95% probability that the true value is in this particular interval." (Strictly, the true value is fixed and the interval either contains it or does not. In everyday reporting this wording is common, but know the difference.) |
| "Values inside the interval are compatible with the data. Values outside are not well supported." | "If we repeat the study, 95% of new estimates will fall inside this interval." |

### What makes an interval wider or narrower

- **Sample size**: larger $n$ gives a narrower interval.
- **Variability**: a larger SD gives a wider interval.
- **Confidence level**: 99% is wider than 95%, which is wider than 90%. More confidence costs precision.

## Hypothesis testing and the p-value {#hypothesis-testing}

::: simple
A **hypothesis test** asks: "Could the difference I see in my sample be due to chance alone?" It works like a court trial. The starting assumption is "no effect" (innocent). You reject it only if the evidence against it is strong.
:::

| Term | Meaning in simple words |
|---|---|
| Null hypothesis $H_0$ | The "nothing is happening" statement: no difference, no association, no effect. Example: the vaccine and placebo groups have the same polio risk. |
| Alternative hypothesis $H_1$ or $H_a$ | What you suspect is true instead: there is a difference. |
| Test statistic | One number that measures how far the sample result is from what $H_0$ predicts, in standard-error units. Examples: $z$, $t$, $\chi^2$, $F$. |
| p-value | The probability of getting a result at least as extreme as yours **if the null hypothesis were true**. |
| Significance level $\alpha$ | The cut-off chosen before the study, usually 0.05. If p &lt; $\alpha$, the result is called "statistically significant". |

### The five steps

1. **State the hypotheses.** Write $H_0$ and $H_1$ in terms of population values.
2. **Choose the significance level** ($\alpha$ = 0.05 unless there is a reason for another value) and the right test for your data (see [choosing the right test](#choosing-test)).
3. **Calculate the test statistic**: (observed value − value expected under $H_0$) ÷ standard error.
4. **Find the p-value** from the matching distribution.
5. **Conclude in plain language**, with the effect size and confidence interval, not only "significant" or "not significant".

::: example illus Worked example: is this district different from the national level?
National stunting is 24% (BDHS 2022). A district survey of 400 children finds 120 stunted, which is 30%.

1. $H_0$: the district's true prevalence is 0.24. $H_1$: it is not 0.24.
2. $\alpha$ = 0.05. One sample, one proportion, large $n$: one-sample z-test.
3. Under $H_0$ the SE is $\sqrt{0.24\times 0.76/400}$ = 0.0214. $z$ = (0.30 − 0.24)/0.0214 = 2.81.
4. The area beyond ±2.81 in the standard normal is $p$ = 0.005.
5. If the district were truly at 24%, a sample this far away would occur only 5 times in 1,000. We reject $H_0$: stunting in the district is higher than the national level, by an estimated 6 percentage points.
:::

[[fig:pvalue|What a p-value is.|The curve shows the test statistics we would expect if the null hypothesis were true. The p-value is the shaded area: the chance of a statistic at least as far from zero as the one observed. The numbers are from the iron supplementation example further down.]]

### What a p-value is not

In 2016 the American Statistical Association published a formal statement because p-values are misused so widely. Its main points, in simple words:

| Wrong belief | The truth |
|---|---|
| "p = 0.03 means there is a 3% chance the null hypothesis is true." | The p-value is calculated *assuming* $H_0$ is true. It cannot give the probability that $H_0$ is true. |
| "p = 0.03 means there is a 3% chance the result is due to chance." | Same error in different words. |
| "A small p-value means a large or important effect." | The p-value mixes effect size with sample size. A tiny, useless effect can have a very small p-value in a big study (see [effect size](#effect-size)). |
| "p &gt; 0.05 means there is no effect." | It means the study did not find convincing evidence. The effect may be real but the sample too small. Absence of evidence is not evidence of absence. |
| "p = 0.049 is a finding and p = 0.051 is not." | The 0.05 line is a convention. The two results carry almost the same evidence. |

### One-sided and two-sided tests

A **two-sided** test asks "is there a difference in either direction?" and counts both tails. A **one-sided** test asks only about one direction and counts one tail, which halves the p-value. Use two-sided tests by default. A one-sided test is acceptable only when a difference in the other direction is impossible or irrelevant, and it must be decided before seeing the data.

### Confidence intervals and tests agree

If a 95% CI for a difference does not contain 0, the two-sided test gives p &lt; 0.05. For a ratio (risk ratio, odds ratio) the "no effect" value is 1 instead of 0. The confidence interval tells you more than the p-value, because it also shows how big the effect could be. Report both.

::: own
My [Dunnhumby retail analysis](../project.html?p=dunnhumby) has a result like this. After matching, the campaign effect was +\$1.03 a week, with a 95% CI of −\$0.99 to \$3.05 and p = 0.32. The interval contains 0 and the p-value is above 0.05. Both say the same thing.
:::

## Type I error, Type II error and power {#errors-power}

A test can be wrong in two ways.

| | Truth: no real effect ($H_0$ true) | Truth: a real effect exists ($H_0$ false) |
|---|---|---|
| Test says "significant" (reject $H_0$) | **Type I error**: false alarm. Probability = $\alpha$ | Correct. Probability = power = $1-\beta$ |
| Test says "not significant" (do not reject $H_0$) | Correct. Probability = $1-\alpha$ | **Type II error**: missed effect. Probability = $\beta$ |

::: simple
- **Type I error ($\alpha$)**: saying there is an effect when there is none. Like a false positive on a diagnostic test.
- **Type II error ($\beta$)**: missing an effect that is really there. Like a false negative.
- **Power ($1-\beta$)**: the chance that the study detects an effect that truly exists. Like sensitivity. Studies are usually designed for 80% or 90% power.
:::

[[fig:power|The two errors and power.|The teal curve is what the test statistic does when there is no effect. The orange curve is what it does when a real effect exists. Moving the critical value to the right reduces false alarms (α) but increases missed effects (β).]]

**Public health consequences.** A Type I error can lead to a useless programme being funded or a harmless food being blamed for an outbreak. A Type II error can lead to an effective intervention being abandoned or a real hazard being declared safe. Which error is worse depends on the situation.

**Power increases when**:

- the sample size is larger;
- the true effect is larger;
- the data are less variable (smaller SD, better measurement);
- $\alpha$ is set higher (0.10 instead of 0.05), which trades more false alarms for fewer missed effects.

::: example illus Worked example: how sample size drives power
A programme is expected to reduce anaemia from 30% to 20%. The table shows the chance that a study comparing two groups would find a significant difference (two-sided $\alpha$ = 0.05), if that reduction is real.

| Participants per group | 50 | 100 | 200 | 291 | 400 | 600 |
|---|---:|---:|---:|---:|---:|---:|
| Power | 21% | 38% | 64% | 80% | 91% | 98% |

With 50 per group the study would miss this large and important effect four times out of five. A "not significant" result from such a study says almost nothing. This is why sample size must be calculated before data collection.
:::

## Effect size: statistical significance and practical importance {#effect-size}

::: simple
An **effect size** says how big a difference or association is. The p-value only says whether the difference can be told apart from zero. Public health decisions need the size.
:::

| Comparison | Effect size | Meaning |
|---|---|---|
| Two means | Mean difference, with CI | In the original units, such as mmHg or g/dL. The most useful for decisions. |
| Two means, standardised | Cohen's d = mean difference ÷ SD | Common guide: 0.2 small, 0.5 medium, 0.8 large. |
| Two proportions | Risk difference, risk ratio, odds ratio | Covered in the [section on risk ratios and odds ratios](#ratio-intervals) below. |
| Two numerical variables | Correlation $r$, or $r^2$ | Strength of the straight-line relationship. |
| Three or more means | Eta squared ($\eta^2$) | Share of the total variation explained by the groups. |

::: example illus Worked example: significant but unimportant
A study with 100,000 people in each group finds that a new salt-awareness leaflet lowers mean systolic blood pressure by 0.3 mmHg (SD 15).

SE of the difference = 15 × $\sqrt{2/100{,}000}$ = 0.067. $z$ = 0.3/0.067 = 4.47, giving p &lt; 0.00001. Cohen's d = 0.3/15 = 0.02.

The result is "highly significant", yet 0.3 mmHg has no clinical meaning. With a huge sample, almost any difference becomes statistically significant. The opposite also happens: a 6 mmHg reduction in a study of 20 people may be "not significant" and still be worth a larger trial.
:::

::: remember
Statistical significance answers "is it real?" Effect size answers "is it big enough to matter?" A confidence interval answers both at once. Always ask all three.
:::

::: own
My [diabetes readmission analysis](../project.html?p=diabetes) had 69,970 patients, and with a sample that size almost every difference was statistically significant. So I ranked the features by effect size instead of p-values.
:::

## Sample size basics {#sample-size}

Sample size is decided before the study, from what you want to achieve. Too few people and the study cannot answer the question. Too many and money and participants' time are wasted.

### To estimate one proportion (a prevalence survey)

$$n=\frac{z^2\,p\,(1-p)}{d^2}$$

Here $z$ is 1.96 for 95% confidence, $p$ is the expected prevalence, and $d$ is the margin of error you can accept, written as a proportion (0.05 for ±5 percentage points). This is often called Cochran's formula. If you have no idea of $p$, use 0.5, which gives the largest sample and is therefore the safe choice.

::: example illus Worked example
Unknown prevalence, ±5% margin: $n$ = 1.96² × 0.5 × 0.5/0.05² = 3.8416 × 0.25/0.0025 = 384.2, rounded up to **385**. This is where the "384" seen in so many theses comes from.

Expected prevalence 24%, ±5% margin: $n$ = 3.8416 × 0.24 × 0.76/0.0025 = 280.3, rounded up to **281**.

| Margin of error (p = 0.5) | ± 10% | ± 5% | ± 3% | ± 2% | ± 1% |
|---|---:|---:|---:|---:|---:|
| Sample size needed | 97 | 385 | 1,068 | 2,401 | 9,604 |
:::

Three adjustments are made in practice:

- **Design effect (DEFF).** Cluster surveys select villages or wards first and then households, because that is cheaper. People in the same cluster are alike, so each one adds less new information. Multiply $n$ by the design effect, often taken as 1.5 to 2. With DEFF 1.5: 385 × 1.5 = 577.5, rounded up to 578.
- **Non-response.** Divide by the expected response rate. With 10% non-response: 578 ÷ 0.9 = 642.2, rounded up to 643.
- **Small populations.** If the population $N$ is small, use the finite population correction $n_{adj}=n/(1+(n-1)/N)$. For $N$ = 2,000: 384.2 ÷ (1 + 383.2/2,000) = 322.4, rounded up to 323.

### To compare two proportions

$$n\text{ per group}=\frac{(z_{\alpha/2}+z_{\beta})^2\,\big[\,p_1(1-p_1)+p_2(1-p_2)\,\big]}{(p_1-p_2)^2}$$

For $\alpha$ = 0.05, $z_{\alpha/2}$ = 1.96. For 80% power $z_{\beta}$ = 0.84, and for 90% power $z_{\beta}$ = 1.28.

::: example illus Worked example
To detect a fall in anaemia from 30% to 20% with 80% power: (1.96 + 0.84)² = 7.84. The variance part is 0.30 × 0.70 + 0.20 × 0.80 = 0.37. The difference squared is 0.10² = 0.01.

$n$ = 7.84 × 0.37/0.01 = 290.1, so **291 per group**, matching the [power table](#errors-power) above.
:::

::: remember
The smaller the difference you want to detect, the larger the sample. Halving the difference needs about four times as many people. A sample size statement must list its inputs: confidence level, power, expected values, margin or difference, design effect, and non-response.
:::

## Choosing the right test {#choosing-test}

Ask three questions. What type is the outcome variable? How many groups are being compared? Are the groups independent, or are the same people measured more than once (paired)?

| Outcome | Comparison | Test | If assumptions fail |
|---|---|---|---|
| **Numerical** | One sample against a known value | One-sample t-test | Wilcoxon signed-rank test |
| Numerical | Two independent groups | Independent t-test (Welch) | Mann-Whitney U test |
| Numerical | Two paired measurements | Paired t-test | Wilcoxon signed-rank test |
| Numerical | Three or more independent groups | One-way ANOVA | Kruskal-Wallis test |
| Numerical | Three or more repeated measurements | Repeated-measures ANOVA | Friedman test |
| **Categorical** | One sample against a known proportion | One-sample z-test for a proportion | Exact binomial test |
| Categorical | Two or more independent groups | Chi-square test | Fisher's exact test |
| Categorical | Two paired yes/no measurements | McNemar's test | Exact McNemar test |
| Categorical | Ordered groups (dose levels) | Chi-square test for trend | |
| **Two numerical variables** | Strength of relationship | Pearson correlation | Spearman correlation |
| **Binary outcome, several predictors** | Adjusting for confounders | Logistic regression | |
| **Count outcome** | Rates across groups | Poisson regression | Negative binomial regression |

**Parametric** tests (t-test, ANOVA, Pearson) assume the data, or the sample means, follow a known distribution, usually the normal. **Non-parametric** tests (Mann-Whitney, Wilcoxon, Kruskal-Wallis, Spearman) work on ranks and make fewer assumptions. They are safer for small, skewed or ordinal data, at the cost of slightly less power when the data really are normal.

## Tests for numerical outcomes {#numerical-tests}

### Independent two-sample t-test

Question: is the mean of a numerical variable different between two separate groups? $H_0$: the two population means are equal.

$$t=\frac{\bar{x}_1-\bar{x}_2}{\sqrt{\dfrac{s_1^2}{n_1}+\dfrac{s_2^2}{n_2}}}$$

This version is **Welch's t-test**, which does not assume the two groups have the same variance. It is the default in R and is the safer choice. The older Student's version pools the two variances.

::: example illus Worked example: iron supplementation
After 12 weeks, 40 girls who received iron tablets have mean haemoglobin 11.8 g/dL (SD 1.4). Forty girls in the comparison group have mean 11.1 g/dL (SD 1.5).

- Difference = 11.8 − 11.1 = **0.7 g/dL**
- SE = $\sqrt{1.4^2/40+1.5^2/40}$ = $\sqrt{0.049+0.056}$ = 0.324
- $t$ = 0.7/0.324 = 2.16, with about 78 degrees of freedom, **p = 0.034**
- 95% CI for the difference = 0.7 ± 1.99 × 0.324 = **0.05 to 1.35 g/dL**
- Cohen's d = 0.7/1.45 = 0.48, a medium effect

Reporting sentence: "Mean haemoglobin was 0.7 g/dL higher in the supplemented group (95% CI 0.05 to 1.35; p = 0.034)." The interval shows the honest picture: the true benefit could be as small as 0.05 or as large as 1.35.
:::

### Paired t-test

Question: did a measurement change in the same people (before and after), or differ between matched pairs? Calculate the difference for each pair, then test whether the mean difference is zero.

$$t=\frac{\bar{d}}{s_d/\sqrt{n}}\quad\text{with }n-1\text{ degrees of freedom}$$

::: example illus Worked example: salt reduction and blood pressure
Ten hypertensive patients have systolic blood pressure measured before and after 8 weeks of a low-salt diet.

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Mean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Before | 150 | 148 | 160 | 155 | 142 | 158 | 165 | 149 | 152 | 157 | 153.6 |
| After | 144 | 146 | 151 | 150 | 143 | 149 | 158 | 145 | 147 | 150 | 148.3 |
| Difference | 6 | 2 | 9 | 5 | −1 | 9 | 7 | 4 | 5 | 7 | 5.3 |

- Mean difference $\bar{d}$ = 5.3 mmHg. SD of the differences $s_d$ = 3.09.
- SE = 3.09 ÷ √10 = 0.978. $t$ = 5.3/0.978 = 5.42 with 9 df, **p = 0.0004**.
- 95% CI = 5.3 ± 2.262 × 0.978 = **3.1 to 7.5 mmHg**.

**Why pairing matters**: if these data are wrongly analysed as two independent groups, the result is p = 0.053, "not significant". Patients differ a lot from each other (142 to 165), and that variation hides the effect. Pairing removes it, because each patient is compared with himself or herself.
:::

::: mistake
A before-and-after study with no control group cannot prove that the diet *caused* the fall. Blood pressure may drop anyway on a second visit because patients are calmer, or because extreme first readings tend to move toward the average (**regression to the mean**). The test shows the change is real. Only the study design can show what caused it.
:::

### One-way ANOVA (analysis of variance)

Question: are the means of three or more groups all equal? $H_0$: all the population means are equal. $H_1$: at least one is different.

::: simple
ANOVA compares two kinds of variation: how far the group means are from each other (between-group) and how spread out people are inside each group (within-group). If the groups differ more than the noise inside them can explain, the $F$ statistic is large.
:::

$$F=\frac{\text{variation between groups}}{\text{variation within groups}}=\frac{MS_{\text{between}}}{MS_{\text{within}}}$$

::: example illus Worked example: haemoglobin in three districts
Twenty women are sampled in each of three districts. Mean haemoglobin is 11.0, 11.6 and 12.1 g/dL, and the SD within each district is 1.2.

- Overall mean = (11.0 + 11.6 + 12.1) ÷ 3 = 11.57
- Between-group sum of squares = 20 × [(11.0 − 11.57)² + (11.6 − 11.57)² + (12.1 − 11.57)²] = 12.13, with 3 − 1 = 2 df, so $MS_{\text{between}}$ = 6.07
- $MS_{\text{within}}$ = 1.2² = 1.44, with 60 − 3 = 57 df
- $F$ = 6.07/1.44 = **4.21**, p = 0.020

At least one district differs. ANOVA does not say which. Eta squared = 12.13 ÷ (12.13 + 82.08) = 0.13: district explains 13% of the variation in haemoglobin.
:::

To find which pairs differ, run a **post hoc test** such as Tukey's HSD or Bonferroni-corrected t-tests. Do not run many separate t-tests without correction (see [multiple testing](#assumptions)).

### Non-parametric alternatives

These tests replace the values with their ranks, so an extreme value counts only as "the largest" however large it is.

::: example illus Worked example: Mann-Whitney U test
Length of stay in days for 5 patients on a standard protocol: 7, 9, 11, 14, 30. For 5 patients on a new protocol: 2, 3, 5, 6, 8.

Rank all 10 values from smallest to largest. The new-protocol patients get ranks 1, 2, 3, 4 and 6, which sum to 16. The standard-protocol patients get ranks 5, 7, 8, 9 and 10, which sum to 39.

$U=16-\dfrac{5\times 6}{2}=1$. The exact two-sided p-value is **0.016**. Median stay is 5 days against 11 days.

A t-test on the same data gives p = 0.084, because the single 30-day stay inflates the variance. With small, skewed samples the rank test is both safer and, here, more powerful.
:::

| Non-parametric test | Replaces | Notes |
|---|---|---|
| Mann-Whitney U (Wilcoxon rank-sum) | Independent t-test | Report medians and IQRs with it |
| Wilcoxon signed-rank | Paired t-test | Uses the ranks of the paired differences |
| Kruskal-Wallis | One-way ANOVA | Follow with Dunn's test for pairwise comparisons |
| Spearman rank correlation | Pearson correlation | For ordinal, skewed or curved-but-rising data |

### Testing a correlation

To test whether a correlation differs from zero: $t=r\sqrt{n-2}\,/\sqrt{1-r^2}$ with $n-2$ df. For the [age and blood pressure example in Part 1](descriptive-statistics.html#relationships) ($r$ = 0.995, $n$ = 5): $t$ = 16.5, p = 0.0005. With large samples even $r$ = 0.1 becomes "significant", so always judge the size of $r$, not only its p-value.

## Tests for categorical outcomes {#categorical-tests}

### Chi-square test of independence {#chi-square}

Question: are two categorical variables related? $H_0$: they are independent, meaning the outcome percentage is the same in every group.

::: simple
The chi-square test compares the counts you **observed** (O) with the counts you would **expect** (E) if there were no relationship at all. The bigger the gap between observed and expected, the bigger the statistic.
:::

$$\chi^2=\sum\frac{(O-E)^2}{E}\qquad E=\frac{\text{row total}\times\text{column total}}{\text{grand total}}$$

$$df=(\text{rows}-1)(\text{columns}-1)$$

::: example real Real example: the 1954 Salk polio vaccine field trial
In the randomised, placebo-controlled part of the trial, 401,974 children received either the vaccine or a placebo injection. Neither the children nor the doctors knew who received which.

| Observed | Polio | No polio | Total |
|---|---:|---:|---:|
| Vaccine | 57 | 200,688 | 200,745 |
| Placebo | 142 | 201,087 | 201,229 |
| Total | 199 | 401,775 | 401,974 |

1. **Expected counts if the vaccine did nothing.** The 199 cases would be shared in proportion to group size. Expected cases in the vaccine group = 200,745 × 199 ÷ 401,974 = 99.4. In the placebo group = 201,229 × 199 ÷ 401,974 = 99.6.
2. **Compare.** The vaccine group had 57 cases where 99.4 were expected. The placebo group had 142 where 99.6 were expected.
3. **Statistic.** (57 − 99.4)² ÷ 99.4 = 18.07 and (142 − 99.6)² ÷ 99.6 = 18.03. The two "no polio" cells add only 0.009 each. $\chi^2$ = **36.1** with 1 df.
4. **p-value.** The critical value for 1 df at $\alpha$ = 0.05 is 3.84. A value of 36.1 gives p &lt; 0.000001.

A difference this large would essentially never arise by chance. Combined with randomisation and blinding, which rule out bias and confounding, the trial showed that the vaccine prevented polio. It was licensed in 1955.
:::

**Assumptions**: observations are independent (each person appears in one cell only), and expected counts are large enough: the usual rule is that every expected count should be at least 5.

| Degrees of freedom | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Critical value of $\chi^2$ at $\alpha$ = 0.05 | 3.84 | 5.99 | 7.81 | 9.49 | 11.07 | 12.59 |

### Fisher's exact test

When any expected count is below 5, the chi-square approximation is unreliable. Fisher's exact test calculates the exact probability of the observed table, and of every more extreme table, using the hypergeometric distribution. It is the standard choice for small 2 × 2 tables, which are common in outbreak investigations.

::: example illus Worked example: a food-poisoning outbreak
Twenty guests at a wedding are interviewed. Of the 11 who ate the beef curry, 9 became ill. Of the 9 who did not, 2 became ill.

| | Ill | Not ill | Total | Attack rate |
|---|---:|---:|---:|---:|
| Ate beef curry | 9 | 2 | 11 | 81.8% |
| Did not eat it | 2 | 7 | 9 | 22.2% |

Three of the four expected counts are below 5 (4.95, 4.95 and 4.05), so use Fisher's exact test: **p = 0.022**. The risk ratio is 81.8 ÷ 22.2 = 3.7. Guests who ate the curry were about 3.7 times as likely to become ill, and this is unlikely to be chance. The curry becomes the main suspect for laboratory testing.
:::

### McNemar's test for paired categorical data

Used when the same people are classified twice (before and after, or by two different tests). Only the pairs that *changed* carry information. If $b$ people changed from yes to no and $c$ changed from no to yes:

$$\chi^2=\frac{(b-c)^2}{b+c}\quad\text{with 1 df}$$

Example with illustrative numbers: 100 patients are tested with two rapid tests. Fifteen are positive on test A only and 5 on test B only. $\chi^2$ = (15 − 5)²/20 = 5.0, p = 0.025. Test A gives positive results more often.

## Confidence intervals for risk ratios and odds ratios {#ratio-intervals}

Public health papers rarely stop at "p &lt; 0.05" for a 2 × 2 table. They report how many times higher the risk is, with a confidence interval. Ratios are not symmetric (they cannot go below 0 but can be very large), so the interval is calculated on the log scale and then converted back.

| | Outcome | No outcome | Total |
|---|---|---|---|
| Exposed | $a$ | $b$ | $n_1$ |
| Unexposed | $c$ | $d$ | $n_0$ |

$$RR=\frac{a/n_1}{c/n_0}\qquad SE(\ln RR)=\sqrt{\frac{1}{a}-\frac{1}{n_1}+\frac{1}{c}-\frac{1}{n_0}}$$

$$OR=\frac{a\times d}{b\times c}\qquad SE(\ln OR)=\sqrt{\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}}$$

$$95\%\text{ CI}=e^{\,\ln RR\,\pm\,1.96\times SE}$$

::: example real Real example: the Salk trial, continued
- Risk in the vaccine group = 57 ÷ 200,745 = 28.4 per 100,000. Risk in the placebo group = 142 ÷ 201,229 = 70.6 per 100,000.
- **Risk ratio** = 28.4 ÷ 70.6 = **0.40**. Vaccinated children had 40% of the risk of unvaccinated children.
- ln(0.40) = −0.910. SE = √(1/57 − 1/200,745 + 1/142 − 1/201,229) = 0.157.
- 95% CI: $e^{-0.910-1.96\times 0.157}$ to $e^{-0.910+1.96\times 0.157}$ = **0.30 to 0.55**. The interval does not contain 1, which agrees with the chi-square test.
- **Vaccine efficacy** = (1 − RR) × 100 = **60%** (95% CI 45% to 70%) against all reported polio. Against paralytic polio only (33 cases against 115), efficacy was 71%.
- **Risk difference** = 70.6 − 28.4 = 42.2 fewer cases per 100,000 children vaccinated. About 2,400 children had to be vaccinated to prevent one case in that season.

The odds ratio here is also 0.40. When the outcome is rare, the odds ratio and the risk ratio are almost identical.
:::

::: example real Real example: reading a published result
The Physicians' Health Study randomised 22,071 male doctors in the United States to 325 mg of aspirin every other day or placebo and followed them for about five years. The published result for a first heart attack was a relative risk of **0.56 (95% CI 0.45 to 0.70; p &lt; 0.00001)**.

How to read it: aspirin users had 56% of the risk of heart attack, a 44% reduction. The whole interval lies well below 1, so the result is statistically clear, and the true reduction is plausibly anywhere from 30% to 55%. The same study found no reduction in deaths from cardiovascular disease overall, which is a reminder to look at all the important outcomes and not only the one with the striking p-value.
:::

## Checking assumptions and the multiple testing problem {#assumptions}

### Assumptions to check before trusting a test

| Assumption | Needed by | How to check | If it fails |
|---|---|---|---|
| Independence of observations | Almost every test | Think about the design: clusters, households, repeated measurements? | Paired tests, mixed models, or survey methods |
| Normality of the data or of the sample means | t-tests, ANOVA, Pearson | Histogram, Q-Q plot, Shapiro-Wilk test | Rely on the CLT if n is large; otherwise transform (log) or use a rank test |
| Equal variances across groups | Student's t-test, classic ANOVA | Compare the SDs, Levene's test | Welch's t-test or Welch's ANOVA |
| Expected counts of at least 5 | Chi-square test | Look at the expected table | Fisher's exact test, or merge categories |
| Straight-line relationship | Pearson correlation | Scatter plot | Spearman correlation |

A warning about normality tests: with a small sample the Shapiro-Wilk test often fails to detect non-normal data, and with a very large sample it flags tiny departures that do not matter. Plots are usually more informative.

### Multiple testing

Each test at $\alpha$ = 0.05 has a 5% chance of a false alarm when there is no real effect. Run many tests and false alarms become almost certain.

$$P(\text{at least one false positive in }m\text{ independent tests})=1-(1-\alpha)^m$$

| Number of tests | 1 | 5 | 10 | 20 |
|---|---:|---:|---:|---:|
| Chance of at least one false positive | 5% | 23% | 40% | 64% |

A survey that tests 20 risk factors against one disease should expect about one "significant" association by chance alone. The simplest protection is the **Bonferroni correction**: use $\alpha/m$ as the cut-off, so 0.05 ÷ 20 = 0.0025 for 20 tests. It is strict. Gentler methods exist (Holm, and the Benjamini-Hochberg false discovery rate). The better protection is to state one main question before the analysis and to label everything else as exploratory.

::: mistake
**p-hacking**: trying many outcomes, subgroups, cut-offs or tests and reporting only the ones with p &lt; 0.05. The reported p-values are then meaningless. Decide the analysis plan before looking at the results, and report every analysis you ran.
:::

::: own
In my [wind speed forecasting project](../project.html?p=wind) I tested five machine learning models against SARIMA with Diebold-Mariano tests. That is five tests on the same question, so the p-values carry a Holm correction.
:::

## How to report and interpret results {#reporting}

A good results sentence contains four things: the estimate, its confidence interval, the test and p-value, and the meaning in plain words.

| Weak | Better |
|---|---|
| "There was a significant difference in haemoglobin (p &lt; 0.05)." | "Mean haemoglobin was 0.7 g/dL higher in the supplemented group (11.8 against 11.1 g/dL; 95% CI for the difference 0.05 to 1.35; Welch's t-test, p = 0.034)." |
| "Vaccination was associated with polio (p = 0.000)." | "Polio occurred in 28.4 per 100,000 vaccinated children and 70.6 per 100,000 in the placebo group (risk ratio 0.40, 95% CI 0.30 to 0.55; p &lt; 0.001)." |
| "The intervention had no effect (p = 0.21)." | "The difference was 2.1 mmHg (95% CI −1.2 to 5.4; p = 0.21). The study could not rule out a reduction of up to 5 mmHg." |

- Give exact p-values (p = 0.034), except write p &lt; 0.001 for very small ones. Never write p = 0.000.
- Name the test you used and say whether it was two-sided.
- Report the number of people in each analysis.
- Say "not statistically significant", never "insignificant" or "no difference".
- Finish with the public health meaning: who is affected, by how much, and what should be done.

::: mistake Common mistakes in inferential statistics
- Using an independent t-test on paired data, or a paired test on independent groups.
- Running several t-tests instead of ANOVA when there are three or more groups.
- Using the chi-square test when expected counts are below 5.
- Treating "not significant" as proof of no effect, especially in a small study.
- Treating "significant" as proof of an important or causal effect.
- Reporting SE in place of SD to make the data look less variable.
- Ignoring clustering and weights when analysing survey data such as BDHS, which makes confidence intervals too narrow.
- Choosing the test after seeing which one gives the smallest p-value.
- Forgetting that statistics measures chance, not bias. A biased sample gives a precise wrong answer.
:::

## Check yourself {#check}

Try each question first, then open it to see the answer.

??? A survey of 900 adults finds 180 with hypertension. Calculate the prevalence and its 95% confidence interval.
Prevalence = 180 ÷ 900 = 20%. SE = √(0.20 × 0.80 ÷ 900) = 0.0133. Margin = 1.96 × 0.0133 = 0.026. 95% CI = 17.4% to 22.6%.
???

??? Which test would you use? (a) Mean birth weight in smokers' and non-smokers' babies. (b) Blood sugar in the same 30 patients before and after a diet. (c) Vaccination status (yes/no) by mother's education (4 levels). (d) Household income in urban and rural areas. (e) BMI across four wealth groups.
(a) Independent (Welch) t-test. (b) Paired t-test. (c) Chi-square test, or chi-square test for trend because education is ordered. (d) Mann-Whitney U test, because income is skewed. (e) One-way ANOVA, then a post hoc test.
???

??? A trial of 30 patients reports "no significant difference, p = 0.18". A colleague concludes the drug does not work. What is wrong?
A small study has low power, so a Type II error is likely. Look at the effect size and its confidence interval. If the interval includes clinically important benefits, the study is inconclusive, not negative.
???

??? A study reports an odds ratio of 1.8 with 95% CI 0.9 to 3.6. Is it statistically significant at the 5% level?
No. The interval contains 1, the "no effect" value for a ratio, so p is above 0.05. The data are compatible with anything from a small protective effect to a risk more than three times higher, so the study is imprecise.
???

??? You want to estimate exclusive breastfeeding prevalence, expected to be about 55%, within ±4 percentage points at 95% confidence, using a cluster survey with design effect 2. What sample size do you need?
n = 1.96² × 0.55 × 0.45 ÷ 0.04² = 3.8416 × 0.2475 ÷ 0.0016 = 594.3, rounded up to 595. With design effect 2: 1,190.
???

??? A researcher compares 12 biomarkers between cases and controls and finds one with p = 0.03. What should she conclude?
With 12 tests the chance of at least one false positive is 1 − $0.95^{12}$ = 46%. The Bonferroni cut-off is 0.05 ÷ 12 = 0.004, and 0.03 does not pass it. The finding is a lead for a new study, not a conclusion.
???

## Formula sheet {#formulas}

| Quantity | Formula |
|---|---|
| Standard error of a mean | $SE=s/\sqrt{n}$ |
| Standard error of a proportion | $SE=\sqrt{\hat{p}(1-\hat{p})/n}$ |
| Confidence interval | estimate ± critical value × SE |
| Sample size, one proportion | $n=z^2p(1-p)/d^2$ |
| Sample size, two proportions | $n=(z_{\alpha/2}+z_{\beta})^2\,[p_1(1-p_1)+p_2(1-p_2)]/(p_1-p_2)^2$ |
| Two-sample t (Welch) | $t=(\bar{x}_1-\bar{x}_2)/\sqrt{s_1^2/n_1+s_2^2/n_2}$ |
| Paired t | $t=\bar{d}/(s_d/\sqrt{n})$ |
| Chi-square | $\chi^2=\sum(O-E)^2/E$, $E$ = row × column/total |
| Risk ratio, odds ratio | $RR=(a/n_1)/(c/n_0)$, $OR=ad/bc$ |
| Bonferroni cut-off | $\alpha/m$ |

## Reference tables {#tables}

### Standard normal distribution: area to the left of z

| $z$ | Area to the left | $z$ | Area to the left |
|---:|---:|---:|---:|
| −3.0 | 0.0013 | 0.5 | 0.6915 |
| −2.5 | 0.0062 | 1.0 | 0.8413 |
| −2.0 | 0.0228 | 1.28 | 0.8997 |
| −1.96 | 0.0250 | 1.5 | 0.9332 |
| −1.645 | 0.0500 | 1.645 | 0.9500 |
| −1.5 | 0.0668 | 1.96 | 0.9750 |
| −1.28 | 0.1003 | 2.0 | 0.9772 |
| −1.0 | 0.1587 | 2.5 | 0.9938 |
| −0.5 | 0.3085 | 2.576 | 0.9950 |
| 0 | 0.5000 | 3.0 | 0.9987 |

Area to the right of $z$ = 1 − area to the left. Area between $-z$ and $+z$ = 2 × (area to the left of $z$) − 1.

### t distribution: critical values for a 95% confidence interval (two-sided α = 0.05)

| Degrees of freedom | 5 | 10 | 15 | 20 | 24 | 30 | 60 | 120 | Very large |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Critical t | 2.571 | 2.228 | 2.131 | 2.086 | 2.064 | 2.042 | 2.000 | 1.980 | 1.960 |

## Glossary {#glossary}

| Term | Meaning in simple words |
|---|---|
| Alpha ($\alpha$) | The accepted chance of a false alarm (Type I error), usually 0.05. |
| Bias | A systematic error that pushes results in one direction. Not reduced by a bigger sample. |
| Central limit theorem | Sample means are approximately normal when the sample is large, whatever the shape of the data. |
| Confidence interval | A range that is likely to contain the true population value. |
| Degrees of freedom | The number of values that are free to vary once certain totals are fixed. It selects the right t, chi-square or F curve. |
| Design effect | How much a cluster survey inflates the variance compared with a simple random sample of the same size. |
| Effect size | How big a difference or association is. |
| Null hypothesis | The statement of no effect or no difference that a test tries to reject. |
| p-value | The probability of a result at least as extreme as the one observed, if the null hypothesis were true. |
| Power | The chance that a study detects an effect that really exists. |
| Sampling error | The difference between a sample result and the truth that is due to chance alone. |
| Standard error | The typical distance of a sample estimate from the true population value. |
| Type I error | Concluding there is an effect when there is none. |
| Type II error | Missing an effect that really exists. |

## Where these ideas are used next {#next}

| Idea from these notes | Where it is used next |
|---|---|
| Proportions, rates, the 2 × 2 table, risk ratio | Epidemiology: prevalence, incidence, measures of association |
| Conditional probability, confounding | Bias, confounding and causality |
| Correlation, t-test, normal distribution | Linear regression |
| Binomial distribution, odds | Logistic regression and odds ratios |
| Poisson distribution, rate × exposure | Poisson regression and offsets |
| Overdispersion | Negative binomial regression |
| Exponential distribution, hazard | Survival analysis: Kaplan-Meier and Cox regression |
| Independence, design effect | Mixed-effects models and complex survey analysis |

## Sources {#sources}

1. Bangladesh Demographic and Health Survey 2022 (stunting 24%). NIPORT and ICF. [Key Indicators Report](https://dhsprogram.com/pubs/pdf/PR148/PR148.pdf).
2. Salk polio vaccine field trial, 1954. Francis T. et al. An evaluation of the 1954 poliomyelitis vaccine trials. American Journal of Public Health, 1955; 45 (5, Part 2). Counts for the placebo-controlled areas as tabulated at [randomservices.org](https://www.randomservices.org/random/data/Polio.html).
3. Physicians' Health Study. Steering Committee of the Physicians' Health Study Research Group. Final report on the aspirin component of the ongoing Physicians' Health Study. New England Journal of Medicine, 1989; 321: 129-135.
4. p-values. Wasserstein R.L., Lazar N.A. The ASA Statement on p-Values: Context, Process, and Purpose. The American Statistician, 2016; 70: 129-133.
