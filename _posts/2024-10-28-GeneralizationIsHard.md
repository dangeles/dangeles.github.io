---
layout: post
title: Generalization is Hard
categories: AI biotech
author: David
description: I have been thinking a lot about generalization in AI, and why it is so hard. 
---

I am currently traveling through Southeast Asia, a region entirely new to me. Navigating certain situations has been unexpectedly challenging. Do I pay at the beginning or the end of a taxi ride? Have we agreed on a price? Is tipping customary?

The procedure for getting a cab, telling the driver where to go, settling on a price, and reaching the destination is relatively simple and, to a large extent, consistent worldwide. Yet, slight regional differences have made it surprisingly harder to reach some of my destinations than I expected. I spent more energy, more money, and more time getting on a cab than I normally would. 

The point of this post isn’t to share travel challenges but to reflect on generalizability and why ML models often struggle to generalize effectively.

It seems to me that generalizability is difficult because small variations accumulate and create significant noise. Minor habits can quickly add up, and each small inconvenience can be surprisingly costly and interactive. In other words, the combined effect of two minor issues is often greater than their sum. Nowhere is this non-additive effect better understood than in aviation. Aircraft rarely fail due to single, spontaneous issues. Instead, crashes almost always result from a complex sequence of minor errors, each harmless on its own, that together lead to failure, and these mistakes often happen over a remarkably long period of time (hours). 

How have people tackled the generalization problem? Broadly, I think there are two main approaches. The first, though less widely applicable, is to develop domain expertise. People are trained in a procedure and exposed to as much variation within it as possible. This requires significant time and dedication. The second approach is to control variation. In the taxi example, apps like Uber and Grab provide a streamlined process for hailing a ride that eliminates potential issues. Calling and getting into an Uber is nearly identical whether you’re in the U.S., Mexico, or anywhere else. This approach is highly effective. In other words, the most successful human systems don’t solve the generalization problem; they address it by artificially limiting the range of possibilities!

In biology, variation stems from experimental results, experimental design differences, operator habits, technical differences due to reagents and machines, and what we broadly call “biological” variation. The successful application of ML/AI in this field will occur in areas where we can minimize variation across as many of these dimensions as possible. Of course, minimizing variation also requires us to answer a fundamental question: what do we want our ML pipeline to do with the remaining variance?
