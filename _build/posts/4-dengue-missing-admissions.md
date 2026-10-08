slug: dengue-missing-admissions
title: 105,000 dengue admissions were missing from the 2023 division data
series: From my projects
date: 8 October 2026
iso: 2026-10-08
standfirst: In 2023 the eight divisions on the DGHS dengue dashboard did not add up to the national total. How I found where the gap came from, rebuilt it from 176 daily press releases, and checked that the rebuild was right.
excerpt: In 2023 the divisions on the DGHS dengue dashboard were short by about 105,000 admissions. How I found out why and rebuilt them from 176 daily press releases.
---
Before I fitted a single forecasting model on Bangladesh's dengue data, I did one boring check. For every week I added up the eight divisions and compared the sum with the national total.

For 2024, 2025 and 2026 they matched. For 2023 they did not. The divisions were short by 104,648 admissions. That is a third of the year, in the biggest dengue outbreak the country has recorded.

This post is about where those admissions went and how I got them back. It comes from my [dengue forecasting project](../project.html?p=dengue).

## Where the gap appeared {#gap}

The DGHS dashboard has no export button, so I read the numbers out of the chart code in the page. The national total comes from the daily admissions chart. The division numbers come from a separate weekly chart. Up to the week of 2 July 2023 the two agreed within a few admissions. Then they split.

[[fig:dengue_gap|National admissions against the sum of the eight divisions, May to December 2023.|Weekly hospital admissions as published on the DGHS dashboard, downloaded on 1 October 2026. Before May both lines are close to zero. The shaded area is what the division series is missing.]]

The weeks around the split show what went wrong.

| Week of (2023) | National | Sum of divisions | Dhaka | Barishal |
|---|---:|---:|---:|---:|
| 16 Jul | 11,231 | 9,906 | 6,621 | 137 |
| 23 Jul | 15,722 | 6,967 | 2,772 | 23 |
| 30 Jul | 17,561 | 7,841 | 2,632 | 0 |
| 6 Aug | 18,538 | 8,536 | 3,311 | 0 |
| 13 Aug | 15,354 | 7,191 | 2,572 | 0 |
| 20 Aug | 14,324 | 7,949 | 2,230 | 1,092 |

In the week of 23 July national admissions went up by 40%, but Dhaka division went down from 6,621 to 2,772. And Barishal reported exactly zero for three weeks in a row, at its own peak.

A real outbreak does not halve in its biggest division in the same week it grows everywhere else. A count of exactly zero for three weeks in a division with thousands of patients is not a quiet spell either. Both looked like reporting problems, not epidemiology.

## Two separate problems {#problems}

1. **Dhaka lost its city.** From late July 2023 the dashboard's Dhaka series counted only Dhaka division outside Dhaka's two city corporations. The city is where most of the division's patients are. From 2024 the city corporations are included again.
2. **Barishal went missing.** Its numbers were zero or far too low for several weeks around its peak.

## A second source {#press-releases}

DGHS also publishes a press release every day as a PDF. It has two things the dashboard was missing: the day's admissions split into Dhaka city and outside Dhaka city, and a table by division with Barishal in it. I downloaded all 176 press releases from 9 July to 31 December 2023.

## Reading 176 PDFs so they check themselves {#self-checking}

Reading numbers out of PDFs is where errors creep in. A table shifts by one row and you read the wrong division. So I only accepted a number when the PDF itself confirmed it.

- **Dhaka city.** The city and outside-city numbers must add up exactly to the day's national total from the dashboard, or the reading is rejected. This worked on 172 of the 176 days. The four days that failed were 9 to 12 July, before the reporting change, so no value had to be guessed.
- **Barishal.** Every row of the division table obeys two rules: government plus private hospitals equals total new admissions, and cumulative cases minus deaths minus discharges equals patients still in hospital. A row was kept only if it passed both. On top of that, Barishal's cumulative count had to grow by exactly the day's new admissions for at least 7 days in a row. That accepted Barishal on 62 days, from 11 July to 10 September. After that the table layout changed and the reading stopped by itself.

A week used the press-release value for Barishal only if every day of that week passed. That held for 8 weeks, from 16 July to 3 September.

## Checking the rebuild {#checks}

Two checks had to pass before I used any of it.

The first is a week where the dashboard was not broken. In the week of 3 September the dashboard's own Barishal number was intact. The press releases gave 2,342. The dashboard gave 2,342.

The second compares two numbers found in different ways. Once Barishal is corrected, whatever is still missing in a week should be the Dhaka city admissions that fell out of the Dhaka series. I had also read Dhaka city admissions directly from the press releases. In the weeks of 27 August and 3 September the two differ by 4 and 2 admissions. In the week of 23 July they differ by 980, because the reporting change happened in the middle of that week, not at its start.

## Two shortcuts I did not take {#shortcuts}

- **Dropping 2023.** It is the largest outbreak on record and half of my training data. A forecasting model that has never seen a big year is not much use in one.
- **Scaling all divisions up to the national total.** It is quick, and the totals would match. But the missing patients were in Dhaka city and Barishal. Scaling would have spread Dhaka city's patients over the other seven divisions and made places like Chattogram and Khulna look worse than they were.

## The result {#result}

- 91,241 admissions went back to Dhaka.
- 12,616 went to Barishal: 10,625 from the press releases and 1,991 from leftovers above 3% of a week's national total.
- 791 could not be placed in any division. The largest leftover in a single week is 335.

Every rule and the number of admissions it moved is written in a cleaning log, and the repaired weeks are flagged in the data, so anyone can see which numbers are estimates.

## Why it mattered {#why}

| 2023 | As published | After the repair |
|---|---:|---:|
| Dhaka division admissions | 77,801 | 169,007 |
| Dhaka's share of all division admissions | 36.6% | 53.5% |
| Dhaka admissions per 100,000 people | 176 | 382 |
| Barishal admissions | 23,911 | 36,527 |
| Barishal admissions per 100,000 people | 263 | 401 |

With the published numbers, Khulna would have looked worse than Dhaka per person in 2023 (193 against 176 per 100,000). And a model trained on the published series would have learned a collapse in Dhaka, at the peak of the worst outbreak, that never happened.

::: note
2023 here means the 52 weeks from 1 January to 30 December 2023, as downloaded from the dashboard on 1 October 2026. The DGHS press release of 31 December 2023 reports 321,179 admissions for the year, a little more than the dashboard, because the dashboard series was revised later. The press-release figure is the one used in my statistics notes.
:::

## What I take from it {#lessons}

- **Add up the parts before you model anything.** Divisions should add up to the national total, months to the year, groups to the whole. It takes minutes, and here it found a third of a year's admissions.
- **A sudden drop at the worst moment is usually a reporting change.** Real outbreaks do not halve in one week while they grow everywhere else.
- **Find a second source, and make it check itself.** The press releases were only useful because every number I took from them had to agree with something else.
- **Keep a log.** Every change and the number of admissions it touched is written down, so the repair can be questioned and run again.

The full repair, with the code and the week-by-week table, is in notebook 02 of the [project on GitHub](https://github.com/Ashiq-r-khan/Bangladesh-Dengue-Forecasting-Analysis) and in section 3.3 of the [report](../assets/reports/dengue.pdf).
