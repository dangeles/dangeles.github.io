---
layout: post
title: For your genAI to work in biotech, pick the right modality
categories: AI ML biotech
author: David
description: Resist the temptation to build an AI engine that can translate between all modalities. Instead, build an engine that translates all other modalities into the one that is most central to your hypothesis generation and testing approaches.
---

Multimodal, generative AI is all the rage today, and for good reason. These engines are changing how humans write, how we make videos, and how we interface with computers. 

Similarly in biology, there are increasing calls for multimodal AI engines that can translate for example from ATAC-seq data to transcriptomes, or from images to transcriptomes. A very natural progression is then to insist that we should build an engine that can freely translate between images, transcriptomes and ATAC-seq data. In other words, from an RNA-seq profile, I should be able to obtain an image; from an image, an ATAC-seq dataset, and from ATAC-seq, a transcriptome. This is a very good idea, except building such an engine does not come without its challenges (how do you collect paired data when measurements are destructive? how much data do you need? how do you account for batch effects from using different sequencing platforms?).

Set aside the complexity of this issue. Let's take a step back and imagine the minimum viable product that would fundamentally change biology. What is it? Once we start thinking about this problem, we should quickly come to one conclusion: Complete translatability across modalities is not necessary. Why? Not all measurements are equal!

Biology is an experimental science. That means we have methods for controlling cells. The largest class of such control methods is gene expression control. Today, it is straightforward to take a gene, any gene, and force a cell to express it. Therefore, I would claim the most generally actionable measurement in biology is the transcriptome, because the transcriptome tells us what genes are expressed in response to any given perturbation. This suggests a path forward -- to maximize your hypothesis testing velocity, build engines that translate from all other modalities to the transcriptome. It is not necessary to build truly multimodal engines, nor is it essential to be able to transform transcriptomes into other modalities. This reduces the complexity of the engines you have to build, and clarifies the data and experiments needed to train these models.

You may disagree with my claims about the transcriptome, but the point stands: to build the most impactful ML engine for your company, your ML engineers must speak to your biologists and identify the modality that is most central to your hypothesis generation and testing approaches. Develop AI engines that translate other information into that central modality, and profit. It is tempting to try to build engines that are 'complete' in the sense that they can go back and forth between all modalities of interest. I encourage you to resist this urge. It is better to build a smaller engine that helps you discover biology than to build an engine that can map any input into any output, but which hallucinates constantly and costs millions to begin to build.

What do you think?
