---
layout: post
title: Back of the envelope calculation of R_0 for the SARS-Cov-2 Delta strain
categories: pandemic science epidemiology
---

A few months ago, the Delta strain made its conspicuous landing in the US. This strain is more contagious than the original SARS-Cov-2, but by how much?

Recently, I came across an [interesting paper](https://www.science.org/doi/10.1126/science.abg3055) that tried to estimate $R_0$, the viral reproductive number in the absence of all social distancing measures and in a completely susceptible population.

The paper is fairly involved, and makes use of extensive mathematical modeling to achieve its main claim that **Delta is 40 - 100% more transmissible than SARS-Cov-2**. I was wondering if a super quick back of the envelope calculation would reach a similar conclusion.

In the following notebook, I:
  * Calculated the new cases per day, smoothed using a wavelet transform (for no particular reason other than to familiarize myself with this method)
  * Calculated a poor man's viral reproductive number by dividing the reported cases each day by the reported cases a week previous.
  * Found the maximal reproductive number for the ancestor lineage per state between the dates of 2020/05/01 and 2021/07/01; similarly, I found the maximal reproductive number for delta per US state by searching in the period where Delta became prevalent (2021/07/01 and onwards).
  * Compared and contrasted the observed reproductive number, adjusting for fraction of the population that is susceptible at each time.

[Notebook](https://dangeles.github.io/jupyter/DeltaEstimates.html)
