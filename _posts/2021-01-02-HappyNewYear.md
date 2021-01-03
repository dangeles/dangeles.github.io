---
layout: post
title: Happy New Year! How effective does a vaccine have to be to eliminate SARS-Cov2 from the planet?
categories: epidemiology pandemic
---

The Moderna, Pfizer and Astrazeneca vaccines are out! What an exciting way to
start 2021. Everyone wants them, but the question I have been pondering the
first few days of this New Year is: Can we eliminate SARS-Cov2 from the planet?
Can we physically drive this virus to extinction? We know, at least in theory,
that vaccines can do that. A famous example is smallpox, which was declared
eradicated in 1980 by the World Health Organization.

In [this notebook](https://dangeles.github.io/jupyter/SIRV_model.html), I
explore three Susceptible-Infected-Recovered (SIR) models of increasing
complexity: constant population without births or deaths, constant population
with new births and deaths, and constant population with births, deaths and a
vaccine. I work through some basic aspects of these models, including conditions
for disease eradication and arrive at the following conclusion:

**To drive SARS-Cov2 to extinction, the total fraction of the population protected
by the vaccine must exceed 1 - 1 / R_0**, where R_0 is the infectivity of the
virus in the absence of all social distancing conditions and at the beginning of
the pandemic. For SARS-Cov2, I think it's not unreasonable to expect R_0 ~ 7 - 12
(though please note that these are my estimates; there are a number of papers out
there estimating R_0 for SARS-Cov2 and initial estimates ranged from 2 - 5).

Fortunately, both the Pfizer and Moderna, though not the Astrazeneca, vaccines
both have an efficacy exceeding 90%, suggesting that it may indeed be possible
to wipe out SARS-Cov2 from the planet if we socially distance AND vaccinate.

So go get those vaccines!

[Jupyter Notebook](https://dangeles.github.io/jupyter/SIRV_model.html)
