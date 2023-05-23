---
layout: post
title: Hyperparameter tuning and ChatGPT's first failure mode!
categories: ML
---

In the previous post, we used ChatGPT to build a toy neural network model that classifies diagnostic aspirates into 'Malignant' or 'Benign' diagnoses. That toy model worked really well, being able to classify the data with 94% accuracy with default choices of parameters. However, when we see such impressive accuracy (especially when we see such impressive accuracy), we really have to wonder if we couldn't push our performance even higher with some easy tweaks. The process of searching for these tweaks is called 'hyperparameter tuning'. 

In the following notebook, I used the toy model we made before and fed it to ChatGPT, and asked it to write a hyperparameter tuning function, with some choices of a couple of different parameters. It worked! We boosted our performance to 98%!

Having achieved 98% performance, I wondered if we could boost performance further by tweaking not just the number of training epochs, the batch size, and the choice of optimizer, but also by tweaking **the neural network architecture itself**. In theory, doing this is as simple as what we did before. In reality, a small technical glitch in the code meant that the code chatGPT wrote did not run. However, this technical glitch had an eminently readable mistake--fixing the bug was as simple as reading the error message, which included a recommendation for how to fix the code. When I fed chatGPT this error, it failed! It began to contort itself into more and more complex code, none of which worked. 

At first, I was happy enough to implement the solution myself. But it kept bothering me that chatGPT was unable to fix such an easy mistake. Then it hit me: This was a great opportunity for something called **prompt engineering**. Briefly, **prompt engineering** is the process of priming LLMs with a prompt that helps guide the algorithm down the desired solution. **Prompt engineering** can be as simple as providing a more detailed prompt than initially suggested (zero-shot prompt engineering) or it can include asking the large language model (LLM) to reason with you (multi-shot prompt engineering). I decided to explore whether I could zero-shot prompt engineer my conversation with ChatGPT into fixing the bug.

I had read previously that successful zero-shot prompts asked LLMs to enumerate their reasoning and break the logic down into pieces. Thus, I gave ChatGPT the following prompt:

```
hi chat! This code gives an error message:
[python code here]

The error message is:
[Value Error here]

Please reason about this message by breaking it
into pieces. Then suggest a solution based on
your reasoning.
```

This prompt successfully worked! ChatGPT reasoned through the message, and based on its reasoning, it implemented a successful solution to the error. It still did not implement the solution provided in the code, but the solution compiled and ran, which I consider an absolute success given the time investment I made. Conclusion: With machines, as with people, communication is key.

See the [jupyter notebook](https://dangeles.github.io/jupyter/cross_val_tutorial.html).