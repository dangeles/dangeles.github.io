---
layout: post
title: Domain expertise matters, especially in fields that want to use AI
categories: AI biotech
author: David
description: There seems to be this feeling in Silicon Valley that you can just throw a bunch of MLEs at a biology problem and it will get solved. I argue that this is a mistake.
---

Domain-expertise matters. 

AI is coming and will affect all of our fields, but the Silicon Valley idea that your team should consist of 10MLEs, 1-2MLOps and an associate scientist to solve biological problems is a naïve and costly mistake. 

The recent Nobel for computational design of proteins and prediction of protein structure is being touted as proof that AI is revolutionizing biology. This is undoubtedly true--but there are other lessons to be learned. 

First, look at the problem: It is well-posed. Given a sequence, infer its most likely structure (probably in a crystal). Second, the way to measure this problem is well-specified: for example, measure the deviation between expected and observed angles and positions of bonds and atoms. Finally, there is a well-defined distribution: remove all proteins that are intrinsically disordered. I would claim that each of these points was figured out by biophysicists, crystallographers and biochemists long before the computational crowd came along. That's not to say the computation was easy, I am saying that the term "AI" necessarily includes the people who contributed to figuring out points 1, 2 and 3 above, since these are the conditions and distributions that are necessary to build a working ML engine. This work is also done upfront, frequently before any code is written, and requires a willingness to generate and understand data from the perspective of the experts in the field. 

My bet is that, if you're building an AI tech bio company, your salary distribution probably ought to skew towards scientists with domain expertise in your area of interest over MLEs. Additionally, I bet that it's more important your MLEs learn biology than the other way around. 

None of this is to say your company has to perform experiments, or that AI isn't as full of promise as people claim. But stop to consider how well-posed and well-understood the protein design and structure problem was. Now compare it with the outsized claims from group after group, talking about making models that can "solve genomics", or that vacuously claim to build "multimodal, multiscale models for biology". If you cannot immediately grasp what these statements mean or what problem they are impacting, there's a good chance the problem is not well posed. And if the problem is not well-posed, no algorithm is ever going to get you a solution. 
