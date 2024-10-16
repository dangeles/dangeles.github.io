---
layout: post
title: A toy Neural Network and an introduction to Tensorflow
categories: ML
author: David
description: I wanted to take a dive into companion coding using ChatGPT, so I asked it to help me write a blog post on an introduction to ML methods in python, specifically, I wanted to build a Neural Network using tensorflow to analyze a toy dataset (I even let Chat pick the dataset!).
---

I'm currently exploring ChatGPT and while I'm doing this, I am revisiting common ML concepts, and exploring libraries like the tensorflow library.

For the purposes of this blogpost, I gave ChatGPT the following prompt:
```
Please help me write a blog post on an introduction to ML methods in 
python, building increasingly complex Neural Networks to analyze a toy
dataset. Please find an appropriate toy dataset (with preference towards
gene expression methods) and begin the blog post by installing the
appropriate packages in a new conda environment with Python 3.x
```

Chat's response was more than adequate:
```
Welcome to our blog post on an introduction to Machine Learning (ML)
methods in Python, specifically focused on building neural networks for
analyzing gene expression data.

First things first, let's get our environment set up.

Setting up the Environment
To start, we're going to use Conda, a powerful package manager and
environment management system. If you don't have it installed, you can
download it from...
```

The blog post follows a fairly standard format: We generate a python 3.9 environment, and populate it with standard python libraries like pandas, numpy, matplotlib. Then we `pip install tensorflow`. ChatGPT suggested a publicly available dataset ([the breast cancer wisconsin diagnostic dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))), and we fit a neural network to it.

Here's the notebook, in the [jupyter notebook](https://dangeles.github.io/jupyter/intro_to_tensorflow.html).
