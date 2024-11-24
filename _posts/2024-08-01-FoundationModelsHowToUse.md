---
layout: post
title: Are overfitted models useful?
categories: AI ML biotech
author: David
description: A thought experiment on the utility of overfitted models in biological research.
---


I think about foundation models a fair amount these days: how to build them, how to test them, and how to use them. Recently, I’ve been pondering the following thought experiment that highlights how differently we may need to think about foundation models in biological research compared to applications in tech. I don’t have a right or wrong answer to this thought experiment, but I believe it is valuable to consider.

Assume everything is done using best practices except where otherwise specified.

Imagine we trained a powerful model (model A) on a set of training data using an auxiliary task—one designed to help the model learn about variation in our datasets. After training, model A is evaluated on a test dataset and is found to be significantly overfitted—its performance on the training dataset is much better than on the test dataset. For most applications, this would be a death sentence for our model, correct? In fact, we would probably train a model B that is not overfitted.

Now, let’s imagine that a researcher uses the embedding of this overfitted model A to study the biological properties of another dataset or experiment. Furthermore, imagine that clustering on this embedding suggests biological hypotheses of great interest in this dataset. These clusters are not visible using any other models (such as model B); they are uniquely present in this embedding and could therefore be artifacts of the overfitting. However, upon experimentally testing these hypotheses in the lab, the team is pleasantly surprised to discover new biology that aligns with the predictions made with model A’s embedding. This process is repeated multiple times, and each time the embedding of model A (which was overfitted on the auxiliary task) is found to reliably identify new biological signals, whereas model B (which was not overfitted) does not lead to new hypotheses.

Which model should we use as a foundation model for biological discovery? Which model is more useful for task prediction? And lastly, is model B over-specialized to the training task at the cost of understanding biological data? How likely is it that this scenario may actually play out?
