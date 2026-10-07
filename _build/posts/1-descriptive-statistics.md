slug: descriptive-statistics
title: Descriptive statistics for public health
series: Statistics for Public Health
part: 1
date: 7 October 2026
iso: 2026-10-07
standfirst: How to summarise health data in a few numbers that are correct. Counts and rates, mean and median, spread, percentiles, z-scores, correlation, and the Table 1 that opens almost every paper.
excerpt: How to summarise health data in a few correct numbers: counts and rates, mean and median, spread, percentiles, z-scores, correlation and Table 1, with worked public health examples.
---
These are my study notes on the statistics a public health data analyst uses every day. They come in three parts: descriptive statistics (this post), [probability and distributions](probability-and-distributions.html) and [inferential statistics](inferential-statistics.html).

Every idea follows the same order: a definition in simple words, the formula, a worked example with the steps shown, and what it means for a public health decision. There is no code. Every calculation can be followed with a basic calculator.

Descriptive statistics turns raw records into a small number of summaries that a person can read and act on. It makes no claim beyond the data in front of you. Every report, dashboard and research paper in public health starts here.

## How to read these notes {#how-to-read}

Each example carries one of two labels.

| Label | Meaning |
|---|---|
| Real data | The numbers come from a published source, listed under [Sources](#sources) at the end. Examples: the 2023 dengue outbreak in Bangladesh, the Bangladesh Demographic and Health Survey 2022, the 1954 Salk polio vaccine trial. |
| Illustrative numbers | A realistic public health situation with made-up numbers chosen so the arithmetic is easy to follow. Do not quote these as facts. |

Four kinds of box appear throughout. **In simple words** is the plain definition, so read it first. **Example** is a worked calculation or a real case. **Common mistake** is an error seen often in theses and reports. **Remember** is the one line to keep.

### Symbols you will see

Statistics uses Greek letters for the population (the truth we cannot see) and Latin letters for the sample (the data we have).

| Quantity | Population (parameter) | Sample (statistic) | How to read it |
|---|---|---|---|
| Size | $N$ | $n$ | Number of people or units |
| Mean | $\mu$ (mu) | $\bar{x}$ (x-bar) | The average |
| Standard deviation | $\sigma$ (sigma) | $s$ | Typical distance from the mean |
| Variance | $\sigma^2$ | $s^2$ | Standard deviation squared |
| Proportion | $p$ or $\pi$ | $\hat{p}$ (p-hat) | Share of people with the characteristic |
| Correlation | $\rho$ (rho) | $r$ | Strength of a straight-line relationship |

Two more symbols come up often. $\sum$ (capital sigma) means "add up all the values". $\alpha$ (alpha) and $\beta$ (beta) are error rates: the chance of a false alarm and the chance of a missed effect.

## What descriptive statistics is {#what}

::: simple
Descriptive statistics means describing the data you have: how many, how much, how spread out, and what shape. It answers "what happened?" It does not answer "why?" or "will it happen again?"
:::

A surveillance officer who receives 321,179 dengue records cannot read them one by one. Descriptive statistics lets the officer say: how many cases, in which months, in which age groups, in which districts, and how many died. In epidemiology this is called describing disease by **person, place and time**.

| Question | What you summarise | Public health example |
|---|---|---|
| Person | Age, sex, occupation, education, wealth | Which age group has the most dengue deaths? |
| Place | Division, district, urban or rural, ward | Is stunting higher in Sylhet than in Khulna? |
| Time | Day, week, month, year, season | In which month do cases peak? |

## Population, sample, parameter and statistic {#population-sample}

::: simple
- **Population**: everyone you want to know about. Example: all children under 5 in Bangladesh.
- **Sample**: the part of the population you actually measured. Example: the children measured in a survey.
- **Parameter**: a true number about the population. It is usually unknown. Example: the true percentage of all under-5 children who are stunted.
- **Statistic**: a number calculated from the sample. Example: 24% stunted among the children measured.
:::

::: example real Real example
The Bangladesh Demographic and Health Survey (BDHS) 2022 interviewed 30,018 households and 30,078 women aged 15 to 49. Nobody measured every child in the country. The published figure, 24% of under-5 children stunted, is a statistic from the sample that is used to estimate the parameter for the whole country. [Part 3](inferential-statistics.html) explains how far a statistic can be trusted.
:::

## Types of variables {#variables}

A variable is anything that differs from one person to the next: age, sex, blood pressure, vaccination status. The type of variable decides which summary, which chart and which statistical test you are allowed to use, so identify the type before anything else.

| Type | Meaning in simple words | Public health examples | Correct summary |
|---|---|---|---|
| **Nominal** (categorical) | Named groups with no order | Sex, blood group, division, cause of death | Count and percentage, mode |
| **Binary** (a nominal variable with two groups) | Yes or no | Vaccinated or not, died or survived, test positive or negative | Count and percentage |
| **Ordinal** (categorical) | Groups with a natural order, but the gaps between groups are not equal | Education level, wealth quintile, pain score, cancer stage | Count and percentage, median |
| **Discrete** (numerical) | Whole-number counts | Number of children, number of clinic visits, number of cases per week | Mean or median, with a spread; or rate |
| **Continuous** (numerical) | Measured on a scale; any value is possible | Weight, height, haemoglobin, blood pressure, age | Mean and SD, or median and IQR |

Two more labels are used in every analysis:

- **Outcome** (dependent variable): the result you care about, such as having diabetes.
- **Exposure** or **predictor** (independent variable): the thing that may influence the outcome, such as BMI or smoking.

::: mistake
**Codes are not numbers.** If sex is stored as 1 = male and 2 = female, a "mean sex of 1.48" has no meaning. The same applies to division codes and to ordinal scales such as education level (1 to 5). A second mistake is cutting a continuous variable into groups too early, for example turning age into "young" and "old". Grouping throws away information. Keep the original values and group only for presentation.
:::

## Counts, proportions, ratios and rates {#rates}

For a categorical variable the basic summary is a **frequency table**: each category, how many people fall in it, and what percentage that is. Public health then builds four kinds of number from counts. They are often confused, even in published reports.

| Measure | Meaning in simple words | Formula | Example |
|---|---|---|---|
| **Proportion** | A part divided by the whole. The top number is included in the bottom number. Always between 0 and 1. | $\dfrac{a}{a+b}$ | Stunted children ÷ all children measured = 0.24 |
| **Percentage** | A proportion multiplied by 100. | $\dfrac{a}{a+b}\times 100$ | 24% of under-5 children stunted (BDHS 2022) |
| **Ratio** | One number divided by a different number. The top is not part of the bottom. | $\dfrac{a}{b}$ | Stunted to not stunted = 24 : 76, about 1 to 3.2 |
| **Rate** | How fast events happen: events divided by the population at risk over a period of time. | $\dfrac{\text{events}}{\text{population}\times\text{time}}\times k$ | Dengue cases per 100,000 people per year |

The multiplier $k$ (100, 1,000 or 100,000) only makes small numbers readable. Use 100 for common events, 1,000 for births and deaths, and 100,000 for rarer diseases.

::: example real Real example: dengue in Bangladesh, 2023
The Directorate General of Health Services (DGHS) recorded 321,179 hospitalised dengue cases and 1,705 deaths in 2023, the largest outbreak in the country's history.

- **Proportion (case fatality)**: 1,705 ÷ 321,179 = 0.0053, or **0.53%**. Out of every 1,000 hospitalised patients, about 5 died. This is called the case fatality "rate" by habit, but it is a proportion, because the deaths are part of the cases.
- **Rate (incidence)**: with a population of about 170 million (2022 census), 321,179 ÷ 170,000,000 × 100,000 ≈ **189 hospitalised cases per 100,000 people in the year**.
- **Percentage (seasonality)**: 303,913 of the cases were recorded from July to November, which is **94.6%** of the year's total in five months.

These three numbers already tell a health manager what to prepare (beds for a July to November surge) and how deadly the disease was among those admitted.
:::

::: mistake
**Comparing raw counts between places of different size.** Dhaka will almost always have more cases than a small district simply because more people live there. Compare rates per population, not counts. Also state the denominator clearly: the 0.53% above is deaths among *hospitalised* cases. Mild cases that never reached a hospital are not counted, so the true fatality among all infections is lower.
:::

::: own
I ran into this in my [dengue forecasting project](../project.html?p=dengue). In 2023 Dhaka division had 53.5% of all dengue hospital admissions in the country. Per 100,000 people it is Barishal that is hit hardest. It had the highest admission rate in three of the four years.
:::

Some named public health indicators that follow these definitions:

| Indicator | How it is calculated | Real value |
|---|---|---|
| Under-5 mortality rate | Deaths before age 5 per 1,000 live births | 31 per 1,000 (BDHS 2022) |
| Prevalence of stunting | Stunted children ÷ children measured × 100 | 24% (BDHS 2022) |
| Caesarean section rate | C-section births ÷ all births × 100 | 45% (BDHS 2022) |
| Case fatality | Deaths from a disease ÷ cases of that disease × 100 | 0.53% (dengue 2023, hospitalised) |

## Mean, median and mode {#centre}

A measure of centre gives one "typical" value for a numerical variable.

::: simple
- **Mean**: add all the values and divide by how many there are. It is the balance point of the data.
- **Median**: put the values in order and take the middle one. Half the values are below it and half are above. With an even number of values, average the two middle ones.
- **Mode**: the value that appears most often. It is the only measure of centre that works for nominal data.
:::

$$\bar{x}=\frac{\sum x_i}{n}=\frac{x_1+x_2+\cdots+x_n}{n}$$

::: example illus Worked example: length of hospital stay
Ten dengue patients stayed in hospital for these numbers of days: 2, 2, 3, 3, 3, 4, 4, 5, 6, 28.

- **Mean** = (2 + 2 + 3 + 3 + 3 + 4 + 4 + 5 + 6 + 28) ÷ 10 = 60 ÷ 10 = **6.0 days**
- **Median** = average of the 5th and 6th values = (3 + 4) ÷ 2 = **3.5 days**
- **Mode** = **3 days** (appears three times)

Nine of the ten patients stayed 6 days or fewer, yet the mean is 6.0. One patient with a 28-day stay pulled the mean upward. The median, 3.5 days, describes the typical patient better. A hospital planning beds needs both: the median for the typical patient and the mean for total bed-days (mean × number of patients).
:::

### Which one should you report?

| Situation | Report | Why |
|---|---|---|
| Numerical data, roughly symmetric, no extreme values | Mean (with SD) | Uses every value and works with most statistical tests |
| Numerical data that is skewed or has outliers: income, length of stay, cost, incubation period, viral load | Median (with IQR) | Not pulled by extreme values |
| Ordinal data: pain score, satisfaction, wealth quintile | Median | The gaps between categories are not equal, so a mean is not meaningful |
| Nominal data: blood group, cause of death | Mode, or the full percentage table | Categories cannot be ordered or added |

[[fig:dengue|Monthly hospitalised dengue cases, Bangladesh, 2023 (real data, DGHS).|The mean of the 12 months is 26,765 cases, but the median is only 7,622. Seven months lie below the mean. For data shaped like this, the mean describes almost no actual month. This bar chart of cases over time is called an epidemic curve.]]

### Two special means used in public health

**Weighted mean.** When groups have different sizes, each group's value must count in proportion to its size.

$$\bar{x}_w=\frac{\sum w_i x_i}{\sum w_i}$$

::: example illus Worked example: vaccination coverage
Three upazilas report measles vaccination coverage of 90%, 80% and 60%. Their child populations are 10,000, 30,000 and 60,000.

- Simple mean = (90 + 80 + 60) ÷ 3 = 76.7%. This is wrong for the district as a whole.
- Weighted mean = (0.90 × 10,000 + 0.80 × 30,000 + 0.60 × 60,000) ÷ 100,000 = 69,000 ÷ 100,000 = **69%**.

The largest upazila has the lowest coverage, so the true district coverage is well below the simple average. National survey estimates such as BDHS are weighted means for the same reason.
:::

**Geometric mean.** Used when values multiply instead of add, or when they span several powers of ten: antibody titres, bacterial counts, viral load. Take the logarithm of each value, find the ordinary mean of the logs, then convert back.

$$GM=\sqrt[n]{x_1\times x_2\times\cdots\times x_n}=10^{\,\text{mean of }\log_{10}(x_i)}$$

::: example illus Worked example: antibody titres
Five vaccinated people have antibody titres of 10, 20, 40, 80 and 640. The logs (base 10) are 1.000, 1.301, 1.602, 1.903 and 2.806. Their mean is 1.722, and $10^{1.722}$ = **52.8**. The ordinary mean is 158, which is higher than four of the five values. The geometric mean titre (GMT) of 52.8 is the standard summary in vaccine studies.
:::

## Range, variance, standard deviation and IQR {#spread}

Two districts can have the same mean blood pressure while one has everybody near the mean and the other has many very low and very high values. A measure of centre alone hides this. Always report a measure of spread with it.

::: simple
- **Range**: largest value minus smallest value.
- **Variance**: the average of the squared distances from the mean.
- **Standard deviation (SD)**: the square root of the variance. It is the typical distance of a value from the mean, in the same unit as the data.
- **Interquartile range (IQR)**: the width of the middle 50% of the data, from the 25th percentile (Q1) to the 75th percentile (Q3).
:::

$$s^2=\frac{\sum(x_i-\bar{x})^2}{n-1}\qquad s=\sqrt{s^2}\qquad \text{IQR}=Q_3-Q_1$$

::: example illus Worked example: systolic blood pressure
Eight adults at a community clinic have systolic blood pressure (mmHg) of 110, 118, 122, 126, 130, 134, 140 and 160. The mean is 1,040 ÷ 8 = 130.

| Value $x$ | 110 | 118 | 122 | 126 | 130 | 134 | 140 | 160 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Distance from mean $x-\bar{x}$ | −20 | −12 | −8 | −4 | 0 | 4 | 10 | 30 | 0 |
| Squared $(x-\bar{x})^2$ | 400 | 144 | 64 | 16 | 0 | 16 | 100 | 900 | 1,640 |

- **Range** = 160 − 110 = 50 mmHg
- **Variance** = 1,640 ÷ (8 − 1) = 234.3 mmHg²
- **SD** = √234.3 = **15.3 mmHg**
- **Quartiles**: the lower half is 110, 118, 122, 126, so Q1 = (118 + 122) ÷ 2 = 120. The upper half is 130, 134, 140, 160, so Q3 = (134 + 140) ÷ 2 = 137. **IQR** = 137 − 120 = **17 mmHg**.

In a report: "Mean systolic blood pressure was 130 mmHg (SD 15.3)."
:::

### Why divide by n − 1 and not n?

The sample mean sits closer to the sample's own values than the true population mean does, so distances measured from it are a little too small. Dividing by $n-1$ corrects this. The quantity $n-1$ is called the **degrees of freedom**: once the mean is fixed, only $n-1$ of the values are free to vary. For a full population (a census) you divide by $N$.

### How outliers affect each measure

Suppose the last patient's reading was 220 instead of 160.

| Measure | Original data (max 160) | With outlier (max 220) | Affected? |
|---|---:|---:|---|
| Mean | 130.0 | 137.5 | Yes |
| Standard deviation | 15.3 | 34.6 | Yes, strongly |
| Range | 50 | 110 | Yes, strongly |
| Median | 128 | 128 | No |
| IQR | 17 | 17 | No |

::: remember
**Mean goes with SD. Median goes with IQR.** The mean and SD are sensitive to extreme values. The median and IQR are *robust*, which means extreme values barely move them.
:::

### Coefficient of variation (CV)

The SD has units, so you cannot directly compare the spread of weight (kg) with the spread of haemoglobin (g/dL). The CV expresses the SD as a percentage of the mean, which removes the unit.

$$CV=\frac{s}{\bar{x}}\times 100\%$$

For the blood pressure data, CV = 15.3 ÷ 130 × 100 = 11.8%. For the 2023 monthly dengue counts the SD is 31,933 and the mean is 26,765, so CV = 119%. A CV above 100% says the data vary more than their own average, which is typical of outbreak data. Laboratories also use CV to check whether a test gives consistent results.

## Percentiles, quartiles and outliers {#percentiles}

::: simple
The **pth percentile** is the value below which p% of the data fall. The 90th percentile of birth weight is the weight that 90% of babies are lighter than. **Quartiles** are three special percentiles: Q1 is the 25th, Q2 is the 50th (the median) and Q3 is the 75th.
:::

::: example real Real example: COVID-19 quarantine length
Lauer and colleagues (Annals of Internal Medicine, 2020) analysed 181 confirmed cases and estimated the incubation period of COVID-19, the time from infection to first symptoms.

- 2.5th percentile: 2.2 days
- 50th percentile (median): 5.1 days
- 97.5th percentile: 11.5 days

The policy question was "how long must an exposed person be quarantined?" The median cannot answer it, because half of infected people develop symptoms later than 5.1 days. The upper percentiles answer it. The authors estimated that after a 14-day quarantine only about 101 of every 10,000 infected people would develop symptoms later. This is how a percentile became the 14-day rule used worldwide.
:::

The **five-number summary** is minimum, Q1, median, Q3, maximum. A **box plot** draws it: the box runs from Q1 to Q3, a line marks the median, and "whiskers" extend to the smallest and largest values that are not outliers.

### The 1.5 × IQR rule for outliers

A value is flagged as a possible outlier if it lies below $Q_1-1.5\times\text{IQR}$ or above $Q_3+1.5\times\text{IQR}$. These two limits are called fences.

::: example illus Worked example: length of stay again
Data: 2, 2, 3, 3, 3, 4, 4, 5, 6, 28. Lower half 2, 2, 3, 3, 3 gives Q1 = 3. Upper half 4, 4, 5, 6, 28 gives Q3 = 5. IQR = 2.

Lower fence = 3 − 1.5 × 2 = 0. Upper fence = 5 + 1.5 × 2 = 8. The 28-day stay is above 8, so it is flagged. Five-number summary: 2, 3, 3.5, 5, 28.
:::

[[fig:boxplot|How to read a box plot,|drawn from the length-of-stay example. The box holds the middle 50% of patients.]]

::: mistake
**Deleting outliers automatically.** An outlier is a flag to investigate, not an instruction to delete. First ask whether it is a data-entry error (a weight of 650 kg) or a real value (a 28-day stay for a patient with severe dengue). Errors are corrected or removed with a note. Real values stay in the data, and you use robust summaries such as the median. In outbreak detection the "outliers" are the signal you are looking for.
:::

::: note
A note on quartiles: there are several accepted ways to calculate quartiles in small samples. These notes split the data at the median and take the median of each half. R, Excel, SPSS and Python may each give slightly different quartiles for small data sets. With large data the differences disappear.
:::

## Skewness and kurtosis {#shape}

::: simple
A **distribution** shows which values a variable takes and how often. Draw it as a histogram and look at the shape. **Skewness** measures whether one tail is longer than the other. **Kurtosis** measures how heavy the tails are, which means how often extreme values occur.
:::

[[fig:shapes|Three common shapes.|The mean is pulled toward the long tail. The median stays near the bulk of the data.]]

| Shape | Mean and median | Typical public health variables |
|---|---|---|
| Symmetric | Mean ≈ median | Adult height, haemoglobin, blood pressure in a general population, birth weight of term babies |
| Right-skewed (positive skew) | Mean &gt; median | Income, health expenditure, length of hospital stay, incubation period, number of clinic visits, antibody titre, parasite count |
| Left-skewed (negative skew) | Mean &lt; median | Age at death in a high-income country, gestational age at birth |

Most health-care data are right-skewed, because values cannot go below zero but can be very large. Other shape words you will meet:

- **Unimodal** means one peak. **Bimodal** means two peaks, which often signals two different groups mixed together, for example an outbreak that hits young children and elderly people but not adults in between.
- **Skewness value**: 0 means symmetric. As a rough guide, between −0.5 and 0.5 is nearly symmetric, and beyond −1 or 1 is strongly skewed.
- **Kurtosis value**: a normal distribution has kurtosis 3. Software usually reports "excess kurtosis", which is kurtosis minus 3, so 0 means normal-like tails and a positive value means heavier tails and more outliers.

::: remember
Always draw a histogram before calculating anything. If the mean and median are far apart, the data are skewed: report the median and IQR, and think about a log transformation or a non-parametric test later.
:::

## The z-score {#z-score}

::: simple
A **z-score** tells you how many standard deviations a value is above or below the mean. A z-score of 0 is exactly average. A z-score of −2 is two SDs below average.
:::

$$z=\frac{x-\mu}{\sigma}$$

Converting to z-scores is called **standardising**. It puts different measurements on one common scale, so a child's height and weight can be compared with a reference population of the same age and sex.

::: example real Real example: how stunting is defined
The World Health Organization (WHO) Child Growth Standards give, for every age and sex, the median height of healthy children and the SD. For boys aged 24 months the median length is 87.8 cm and the SD is about 3.06 cm.

A 24-month-old boy who measures 80.5 cm has a height-for-age z-score of

$$z=\frac{80.5-87.8}{3.06}=-2.39$$

WHO defines a child as **stunted** when the height-for-age z-score is below −2, and severely stunted below −3. This boy is stunted. The same idea gives **wasting** (weight-for-height z-score below −2) and **underweight** (weight-for-age z-score below −2).

In a healthy reference population only about 2.3% of children fall below −2. BDHS 2022 found 24% of Bangladeshi under-5 children below −2 for height, about ten times the expected share. Wasting was 11% and underweight 22%.
:::

[[fig:zscore|Why 24% stunting is a population problem.|The orange curve is an illustration of a population in which 24% of children fall below the cut-off: the whole distribution has moved left, not only its tail.]]

Other uses of z-scores: comparing a laboratory result with a reference range, finding unusual values (a z-score beyond ±3 is rare), and comparing results measured on different scales.

## Relationships between two variables {#relationships}

### Two categorical variables: the cross-tabulation

A cross-tabulation (contingency table) counts people in every combination of two categorical variables. The most important one in public health is the **2 × 2 table** of exposure by outcome. Always calculate percentages within each exposure group (row percentages), so the groups can be compared fairly.

::: example real Real example: the 1954 Salk polio vaccine trial
| Group | Children | Polio cases | Cases per 100,000 |
|---|---:|---:|---:|
| Vaccine | 200,745 | 57 | 28.4 |
| Placebo | 201,229 | 142 | 70.6 |

The counts 57 and 142 look small next to 200,000. The rates per 100,000 make the comparison clear: the placebo group had about 2.5 times the polio rate of the vaccine group. [Part 3](inferential-statistics.html#chi-square) tests whether a difference this large could be due to chance.
:::

### Two numerical variables: covariance and correlation

::: simple
- **Covariance** shows the direction in which two variables move together. Positive: when one is high the other tends to be high. Negative: when one is high the other tends to be low. Its size depends on the units, so it is hard to interpret.
- **Correlation** (Pearson's r) is covariance with the units removed. It always lies between −1 and +1 and measures how closely the points follow a straight line.
:::

$$\text{cov}(x,y)=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{n-1}\qquad r=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i-\bar{x})^2\,\sum(y_i-\bar{y})^2}}$$

::: example illus Worked example: age and blood pressure
Five adults: ages 30, 40, 50, 60, 70 and systolic blood pressure 118, 124, 130, 140, 148. Mean age is 50 and mean blood pressure is 132.

| Age $x$ | 30 | 40 | 50 | 60 | 70 | Sum |
|---|---:|---:|---:|---:|---:|---:|
| $x-\bar{x}$ | −20 | −10 | 0 | 10 | 20 | |
| $y-\bar{y}$ | −14 | −8 | −2 | 8 | 16 | |
| Product | 280 | 80 | 0 | 80 | 320 | 760 |
| $(x-\bar{x})^2$ | 400 | 100 | 0 | 100 | 400 | 1,000 |
| $(y-\bar{y})^2$ | 196 | 64 | 4 | 64 | 256 | 584 |

Covariance = 760 ÷ 4 = 190. Correlation $r$ = 760 ÷ √(1,000 × 584) = 760 ÷ 764.2 = **0.99**, a very strong positive relationship. $r^2$ = 0.99 means that 99% of the variation in blood pressure in this small group moves together with age.
:::

[[fig:scatter|What different values of r look like.|The last panel is the warning: a strong curved relationship can have r close to zero, because r only measures straight-line relationships. Always look at the scatter plot.]]

| Size of r (ignore the sign) | Rough description |
|---|---|
| 0.00 to 0.19 | Very weak |
| 0.20 to 0.39 | Weak |
| 0.40 to 0.59 | Moderate |
| 0.60 to 0.79 | Strong |
| 0.80 to 1.00 | Very strong |

These labels are a common guide only. What counts as "strong" depends on the field. In studies of human behaviour 0.3 can be important. In laboratory calibration 0.9 can be poor.

**Spearman's rank correlation** ($r_s$ or $\rho$) replaces each value with its rank (1st, 2nd, 3rd...) and then calculates Pearson's r on the ranks. Use it when the data are ordinal, skewed, contain outliers, or follow a curve that keeps rising or keeps falling.

::: mistake
**Correlation is not causation.** Three other explanations must be ruled out before claiming that X causes Y:

- **Confounding**: a third variable drives both. Ice cream sales and drowning deaths rise together because both rise in hot weather.
- **Reverse causation**: Y causes X. Sick people may stop exercising, so "no exercise" and "illness" correlate.
- **Chance**: with many variables some will correlate by accident.

A related error is the **ecological fallacy**: finding a correlation between district averages and then assuming it holds for each individual person.
:::

::: own
Confounding showed up in my [NHANES mortality analysis](../project.html?p=nhanes). People with prediabetes had a crude death rate of 19.4 per 1,000 person-years, against 10.8 with normal glucose. After full adjustment the hazard ratio was 0.99 (0.92 to 1.06). The excess was age.
:::

## Choosing the right chart {#charts}

| What you want to show | Chart | Notes |
|---|---|---|
| Counts or percentages across categories | Bar chart | Bars have gaps between them. Start the axis at zero. Sort bars by size unless the categories have a natural order. |
| Shape of one numerical variable | Histogram | Bars touch because the scale is continuous. Try more than one bin width. |
| Compare a numerical variable across groups | Box plot | Shows median, spread and outliers for each group side by side. |
| Cases over time during an outbreak | Epidemic curve | A histogram of cases by date of onset. Its shape suggests how the disease spreads ([Figure 1](#fig-1)). |
| Trend of a rate over years | Line chart | Time on the horizontal axis. |
| Relationship between two numerical variables | Scatter plot | Outcome on the vertical axis. |
| Rates across areas | Shaded map | Map rates, not raw counts, or the map will only show where people live. |
| Shares of a whole | Bar chart, or pie chart for 2 or 3 groups only | Angles are hard to compare. Avoid pie charts with many slices and all 3D charts. |

## Reporting: Table 1 {#table-1}

Almost every public health paper begins with a table describing the study participants. The rules:

- Categorical variables: number and percentage, written as n (%).
- Symmetric numerical variables: mean (SD).
- Skewed numerical variables: median (IQR), giving Q1 and Q3.
- State the total sample size, and report how many values are missing for each variable.
- Use sensible rounding. One decimal place is enough for most percentages and means.

::: example illus Example layout
| Characteristic | All participants (n = 400) |
|---|---|
| Age in years, mean (SD) | 41.6 (12.3) |
| Female, n (%) | 216 (54.0) |
| Residence: urban, n (%) | 148 (37.0) |
| Systolic blood pressure in mmHg, mean (SD) | 126.4 (15.8) |
| Monthly household income in BDT, median (IQR) | 22,000 (15,000 to 35,000) |
| Current smoker, n (%) | 88 (22.0) |
| Body mass index missing, n (%) | 12 (3.0) |
:::

::: mistake Common mistakes in descriptive statistics
- Reporting a mean without any measure of spread.
- Reporting mean (SD) for skewed data such as income or length of stay. A result like "mean stay 6.0 days (SD 7.8)" is a warning sign: the SD is larger than the mean for a variable that cannot be negative.
- Giving percentages without the count they are based on. "50% improved" could be 1 of 2 patients.
- Confusing SD with standard error (SE). SD describes how spread out the people are. SE describes how precise the mean is. [Part 3](inferential-statistics.html#standard-error) explains the difference.
- Calculating a mean of percentages from groups of different sizes without weighting.
:::

## Check yourself {#check}

Try each question first, then open it to see the answer.

??? Household health spending in a survey has mean 4,800 BDT and median 1,900 BDT. What does this tell you, and which should you report?
The mean is much higher than the median, so the data are right-skewed: a few households spent very large amounts. Report the median with the IQR.
???

??? A district reports 480 tuberculosis cases in a year in a population of 1.2 million. Another reports 150 cases in a population of 250,000. Which has the bigger problem?
Rates: 480 ÷ 1,200,000 × 100,000 = 40 per 100,000, and 150 ÷ 250,000 × 100,000 = 60 per 100,000. The second district has fewer cases but a higher rate.
???

??? A girl's weight-for-age z-score is −3.2. What does it mean?
Her weight is 3.2 standard deviations below the median of healthy girls of her age. Below −3 is classified as severely underweight.
???

??? Is "number of antenatal care visits" nominal, ordinal, discrete or continuous?
Discrete. It is a whole-number count.
???

??? The correlation between a district's number of doctors and its number of deaths is +0.8. Do doctors cause deaths?
No. Population size is a confounder: large districts have more doctors and more deaths. Compare rates per population instead of counts.
???

??? Find the median and IQR of these ages at diagnosis: 22, 25, 29, 31, 34, 38, 45, 52.
Median = (31 + 34) ÷ 2 = 32.5. Lower half 22, 25, 29, 31 gives Q1 = 27. Upper half 34, 38, 45, 52 gives Q3 = 41.5. IQR = 14.5.
???

## Formula sheet {#formulas}

| Quantity | Formula |
|---|---|
| Mean | $\bar{x}=\sum x_i/n$ |
| Weighted mean | $\bar{x}_w=\sum w_i x_i/\sum w_i$ |
| Variance and SD | $s^2=\sum(x_i-\bar{x})^2/(n-1)$, $s=\sqrt{s^2}$ |
| Interquartile range | $\text{IQR}=Q_3-Q_1$ |
| Coefficient of variation | $CV=(s/\bar{x})\times 100\%$ |
| Outlier fences | $Q_1-1.5\,\text{IQR}$ and $Q_3+1.5\,\text{IQR}$ |
| z-score | $z=(x-\mu)/\sigma$ |
| Pearson correlation | $r=\dfrac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i-\bar{x})^2\,\sum(y_i-\bar{y})^2}}$ |

## Glossary {#glossary}

| Term | Meaning in simple words |
|---|---|
| Case fatality | The share of people with a disease who die from it. |
| Confounder | A third variable related to both the exposure and the outcome that distorts their relationship. |
| Incidence | New cases of a disease in a population over a period of time. |
| Outlier | A value far from the rest of the data. |
| Parameter | A true but usually unknown number describing a population. |
| Percentile | The value below which a given percentage of the data fall. |
| Prevalence | The share of a population that has a condition at a given time. |
| Robust | Not strongly affected by extreme values. |
| Skewness | Lack of symmetry: one tail of the distribution is longer. |
| Standard deviation | The typical distance of individual values from the mean. |
| Statistic | A number calculated from a sample. |
| z-score | How many standard deviations a value is from the mean. |

## Sources {#sources}

1. Dengue in Bangladesh, 2023 (321,179 hospitalised cases, 1,705 deaths, monthly counts). Directorate General of Health Services daily dengue reports, as compiled in: Hossain M. et al. [The 2023 Dengue Outbreak in Bangladesh: An Epidemiological Update](https://pmc.ncbi.nlm.nih.gov/articles/PMC12106341/). Health Science Reports, 2025. Cases to 30 June 2023: [WHO Disease Outbreak News, Dengue, Bangladesh](https://www.who.int/emergencies/disease-outbreak-news/item/2023-DON481). The DGHS live dashboard groups some cases by a different date and shows slightly different monthly figures.
2. Bangladesh Demographic and Health Survey 2022 (stunting 24%, wasting 11%, underweight 22%, under-5 mortality 31 per 1,000 live births, caesarean births 45%, 30,018 households). NIPORT and ICF. [Key Indicators Report](https://dhsprogram.com/pubs/pdf/PR148/PR148.pdf).
3. [WHO Child Growth Standards](https://www.who.int/tools/child-growth-standards/standards/length-height-for-age) (length-for-age, boys, 24 months: median 87.8 cm; −2 SD 81.7 cm).
4. COVID-19 incubation period. Lauer S.A. et al. The Incubation Period of Coronavirus Disease 2019 (COVID-19) From Publicly Reported Confirmed Cases. Annals of Internal Medicine, 2020; 172: 577-582.
5. Salk polio vaccine field trial, 1954. Francis T. et al. An evaluation of the 1954 poliomyelitis vaccine trials. American Journal of Public Health, 1955; 45 (5, Part 2). Counts for the placebo-controlled areas as tabulated at [randomservices.org](https://www.randomservices.org/random/data/Polio.html).
6. Population of Bangladesh. Bangladesh Bureau of Statistics, Population and Housing Census 2022 (about 170 million).
