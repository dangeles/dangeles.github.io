---
layout: post
title: Are AI models truly 'emergent'?
categories: AI ML biotech
author: David
description: The most important term in AI today seems to be "emergence", and it refers to the point where a model "learns" something significant and not predictable. I argue that this is a dangerous concept, because it suggests that 'learning' is not quantifiable and therefore not predictable.
---

One of the exciting concepts in AI relates to the idea of emergent properties-model properties that appear abruptly when dataset size or model complexity reaches a threshold. Put another way: There exists an unknown data threshold (assumed to be large) at which an ML engine of sufficiently complex architecture will spontaneously learn something significant about biology. 

Our field commonly believes that we need large amounts of data and compute to extract signal. However, because emergent properties are thresholded, you won't see signal until you reach the aforementioned thresholds. Therefore, progress milestones for research on emergent properties of AI usually swivels around getting enough data and enough compute power, and disregards how to assess whether the threshold exists, and how far one may be from said threshold. Emergence seen from this angle is almost a religious belief.

I don't think these claims are sacrosanct. I suspect we should challenge ourselves to work with less data, not more. Astounding advances in ML have often trained on middle-sized or even small datasets, to the point that performance on a set of small datasets has been a gold-standard for decades. If we can't learn off of small datasets, why do we expect to learn with more data? Second, the idea of thresholded learning is rapidly disappearing from my mind. Yes, learning sometimes requires lots of data, but I think learning is fundamentally continuous.

Imagine you are trying to train an LLM that knows "advanced math". Your training set is drawn from the internet. Most of the internet does not know advanced math. You need to sample a huge fraction of the internet before even encountering concepts from "advanced math". Therefore, you probably cannot see emergent 'advanced math skills' if you assess your LLM's to solve 'advanced math' problems until you hit a sufficiently large data threshold. Learning appears spontaneous, binary and unpredictable. To de-risk our approach, we need to change our definition of success. 

Instead of asking your LLM whether it knows advanced math, benchmark it on whether it knows kindergarten math, a much more common concept in our dataset. Assess middle school skills in your LLM, then high school skills. These benchmarks don't guarantee the LLM will ever learn advanced math, but they can help us assess whether your engine is **learning in the desired direction**. By shifting our definition of success from 'our engine can do advanced math' to 'our engines are solving incrementally more complex math problems', we can update our belief in this project's success continuously.

I get it, this seems obvious. But I have been thinking about what a comparable 'kindergarten', 'middle school', 'high school' progression of assessments would be for genomics and perturbational biology in such a setting. I cannot easily come up with such a sequence. Can you? What are good examples?
