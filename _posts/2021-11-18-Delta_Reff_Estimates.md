---
layout: post
title: Back of the envelope calculation of R_0 for the SARS-Cov-2 Delta strain
categories: pandemic science epidemiology
author: David
description: A quick back of the envelope calculation of the viral reproductive number for the SARS-Cov-2 Delta strain based on readily available data. 
---

A few months ago, the Delta strain made its conspicuous landing in the US. This strain is more contagious than the original SARS-Cov-2, but by how much?

Recently, I came across an [interesting paper](https://www.science.org/doi/10.1126/science.abg3055) that tried to estimate $R_0$, the viral reproductive number in the absence of all social distancing measures and in a completely susceptible population.

The paper is fairly involved, and makes use of extensive mathematical modeling to achieve its main claim that **Delta is 40 - 100% more transmissible than SARS-Cov-2**. I was wondering if a super quick back of the envelope calculation would reach a similar conclusion.

## Methodology

In the following notebook, I:
  * Calculated the new cases per day, smoothed using a wavelet transform (for no particular reason other than to familiarize myself with this method)
  * Calculated a poor man's viral reproductive number by dividing the reported cases each day by the reported cases a week previous.
  * Found the maximal reproductive number for the ancestor lineage per state between the dates of 2020/05/01 and 2021/07/01; similarly, I found the maximal reproductive number for delta per US state by searching in the period where Delta became prevalent (2021/07/01 and onwards).
  * Compared and contrasted the observed reproductive number, adjusting for fraction of the population that is susceptible at each time.

## Findings
The conclusions from my back of the envelope calculations are that:
  1. Without adjustment for susceptible fraction, Delta's effective viral
  reproductive number is about 15% greater than the ancestor lineage.
  2. Adjusted for susceptibles, Delta is probably twice as transmissible as
  the ancestor lineage.
  3. Accounting for susceptible fractions and governmental interventions,
  Delta's viral reproductive number is about 8! Current estimates put Delta's
  reproductive number, R0, at around 6-9, with most estimates around 8-8.5. Not
  a bad estimate, though this number is quite terrifyingly large.

[Notebook](https://dangeles.github.io/jupyter/DeltaEstimates.html)
