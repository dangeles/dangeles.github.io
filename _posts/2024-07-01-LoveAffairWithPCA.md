---
layout: post
title: Why I love PCA for AI
categories: AI ML PCA 
author: David
description: Some thoughts on why I think linear methods like PCA are more important than ever in an ML world
---

Folks who know me know that I have a love affair with PCA. Why? In the age of LLMs, neural networks and so forth, why do I insist on being in love with such a simple, linear method?

First, it is increasingly clear that one of the most important outputs of AI is what we call its 'embedding'--the form in which it represents data and its intrinsic covariances. There is a notion that a good embedding is an embedding that can be useful for many downstream tasks. PCA exposes us directly and natively to the concept of an embedding, so it provides a fertile ground where we can play with embeddings and explore how they can link to downstream tasks.

Second, good embeddings will span a subspace. Arguably, a good AI embedding should not be easily linearly compressed--in other words, all the features should be orthogonal to each other--just like in PCA! If your embedding is easily linearly compressible, you probably have too many features in your hidden layer (I sometimes wonder if the converse is true, if your embedding is not compressible at all, do you have too few features?). Thus, I always recommend that people PCA their hidden layer embeddings to better understand how our ML engines are performing.

Finally, I find that the simplicity and mathematical elegance of SVD is soothing when working with complex data. I appreciate that PCA is invertible, that there is a rich theory for working with it, and that it is a versatile tool that has led to many discoveries. 

I am not opposed to switching. As I told my ML colleagues at some point, the day there is an ML engine in genomics that can outperform what I can do with PCA, I will switch. That day hasn't come. That said, it is clear that better tools are on the horizon--when that day comes, PCA will remain a valuable testing ground with which to learn how to think about embeddings.

