---
layout: post
title: Building your own neural network
categories: ML
---
## So what's the big deal with AI?

It feels like everywhere you turn these days, you hear about Artificial Intelligence (AI). From our phones and laptops to smart home devices, and even in sectors like healthcare, transportation, and finance, AI has ingrained itself into every aspect of our daily lives. But why is AI suddenly such a hot topic? And why is it becoming increasingly important? This post will shed light on these questions and guide you through an example of building a basic Neural Network, one of the powerful algorithms behind AI, from scratch.

Before we dive into the details, let's start by illustrating what a neural network actually is. A neural network is a set of **NODES** (neurons), arranged in **LAYERS**, where each layer is connected to the next layer by **EDGES** between the nodes in each layer. The simplest neural network architecture is an input layer, where the number of nodes is equal to the number of features we will give as an input, and an output layer, where the number of nodes is equivalent to the number of outputs we wish to compute from the input data. When there are more layers sandwiched between the input and output layers, we call these *hidden layers**.

The neural network game, then, is to find the **WEIGHTS** that allows the network architecture to compute the optimal outputs based on the inputs. We do this by 'training' the network on some data, and we assess performance on a 'test' or 'held out' set.

Here is the [link](https://dangeles.github.io/jupyter/NeuralNetwork.html) to a Jupyter notebook, where ChatGPT 4.0 and I built our own single layer neural network from scratch.