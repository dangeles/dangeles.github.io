---
layout: post
title: Is your company's computational biology deck unique?
categories: AI ML biotech
author: David
description: Why do all the biotech companies have the same computational biology deck?
---

More and more often, I am seeing computational biology decks that worry me. Why? Because they all look identical: they propose that biology is complicated (gasp!), and they posit that to solve it we need better AI tools that make sense of data. Inevitably, these decks call for multimodal, high throughput (single cell) data, and they make calls for the development of foundation models. They end by showing promising slides where they can explain a bit of the overall variance in the data, and claim that this progress will lead to much faster advancement in drug development. 

What's wrong with this? Why does this worry me? Let's be clear--the reason is not that AI/ML is bad or wrong.

What worries me the most about these slide decks is that they are interchangeable among companies. Not a single slide deck I have seen contains ideas or approaches that are unique to one company over another. The ideas are clonal--therefore, if one deck is flawed, chances are they are all flawed. Moreover, if everyone has the right approach, then the winner will be determined by dataset size, which means if you are a small or new company, you're inherently at a disadvantage by choosing to take the exact same approach as big pharma. Computational biology and AI/ML are big fields, so why are we seeing total convergence of ideas and approaches?

This leads me to my next concern. All the decks I'm seeing lament the complexity of biological data, and argue that we need to improve models to increase the rate of development in biology. However, not a single one of these decks tells us how development will be augmented by AI. One common claim is that these models will enable perturbation prediction--but this is a non-starter. Why? Because most drugs act to modulate physiology, but these models are trained on in vitro cell culture data. What does it mean to predict perturbation effects in fibroblasts when the drug acts on, say, Kupffer cells, for which we have practically zero data in vitro? How and why is this superior to an empirical drug screen? How and why is it cheaper (recall: these models require enormous amounts of GPUs to run). 

I have found that when we ask ML engineers how we will validate their models, the answer is typically vague and hand-wavey, and often involves long timescales. I argue that this is anathema to computational biology. Call me old fashioned, but if you give me a good experiment, some data from that experiment and a bit of PCA, I can generate testable hypotheses in just over 20 minutes. Why is the bar for these AI models that their effects on biological research will be validated over the next decade?

It is important we insist on strong tests of deep learning models. A strong test is NOT a test of generalizability or on-task performance. Foundation models should generate immediately testable biological hypotheses that cannot be reached using other methods. Let's validate AI not on variance explained, but on signal extracted.
