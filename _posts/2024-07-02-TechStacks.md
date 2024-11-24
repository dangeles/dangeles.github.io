---
layout: post
title: Stop recommending single-cell RNA-seq, recommend bulk RNA-seq!
categories: NGS RNA-seq techdev 
author: David
description: I have realized that people are fascinated with single-cell RNA-seq, but increasingly I would like to see us develop methods that augment bulk RNA-seq to allow us to get the same information at lower cost.
---

One of the amazing and beautiful things about science is that new technologies arrive continuously, allowing us to see things we could not see before. In my case, one of the big things that came during my training was single-cell RNA-seq. It made a huge difference! Suddenly, we could see whether cells were dividing at the time of sequencing, we could easily sort cells into types, and we could study the heterogeneity that we knew was there before but we just couldn't get at previously.

Today, it is easy to perform single-cell RNA-seq to get answers. And yet, I find myself recommending single-cell RNA-seq less and less to my wet lab biologists. Why? It's not because single-cell RNA-seq isn't useful. It's because computational biologists have learned how to analyze the single-cell RNA-seq data, and we have learned how signals in single-cell data correspond to signals in bulk RNA-seq data. Bulk RNA-seq remains much cheaper and technically easier than single-cell, allows for far more biological replicates, and much more convoluted experimental designs.

We shouldn't give up on single-cell RNA-seq. We should continue to use it, learn from it and develop it. At the same time, there are powerful ways to augment bulk RNA-seq by using imaging or other phenotyping methods and machine learning (read: regressions) to imbue it with qualities that give it a single-cell flavor. Think about it: What is the main use of single-cell RNA seq? To identify different cell types and learn about how they signal. If we could computationally do this using bulk RNA-seq at 10x lower cost, isn't this the right way to go? I think often, the answer is yes. More generally, I think soon we will see the rise of a new kind of multi-modal data--data where expensive modalities are done in bulk cells to minimize cost and maximize measurement depth, and cheap modalities are measured at single-cell or few cell resolution. By combining these methods, we can "augment" the bulk methods with cluster information, and link otherwise 'orphan' measurements to gene expression pathways.

What do you think?
