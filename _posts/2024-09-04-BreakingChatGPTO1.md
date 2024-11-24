---
layout: post
title: Breaking ChatGPT-O1
categories: chatgpt
author: David
description: OpenAI claims O1 is their most advanced model. I broke it on a simple math problem.
---

OpenAI just released ChatGPT-o1 and the world is aflame with claims of how good it is. Claims are that it is comparable to the 500 top students in math. 

I tested ChatGPT-o1 on a fuzzy logical problem. In my opinion, it failed at the task. It misinterpreted my prompt in two significant ways and made a number of logical mistakes in its computations. Ultimately, through a multi-shot approach, ChatGPT eventually got to the answer. I would have expected a top 500 student in math to solve this without blinking an eye.

A more in-depth dissection below, starting with my prompt.

PROMPT:
Envision a function, f(x), such that f(x) is approximately quadratic for all positive values of x. Write a reasonable taylor approximation for f(x) for x > 0. Select the correct number of taylor expansion terms. Give a good analytic guess for the integral of f(x) from 0 to 10.

ANSWER:
For its answer, O1 selected an arbitrary function, f(x) = x^2 + exp(-x).

Next, it found the second order Taylor approximation for only exp(-x), rather than f(x). It then added this approximation to x^2 to create a new function (why...?).

It correctly integrated this new function, and determined that an analytic expression for the integral of f(x) from 0 to 10 = 1000/3 + 1.

To me, an acceptable answer would be to approximate f(x) as an arbitrary quadratic function, a + bx + cx^2, and integrate this function over the desired interval, leaving us with a net cubic function. My prompt even tried to gently guide the answer by insisting on first approximating f(x) as a Taylor expansion. 

I re-read my prompt and reasoned that the word 'envision' could be misunderstood as 'pick', so I re-worded the prompt using the more classical mathematical term 'consider'. This time, O1 incorrectly decided that the Taylor expansion for f(x) was x^2, and proceeded from there.

I thought a bit more deeply about what was going wrong, and I decided that the error is likely coming from an over-emphasis of ChatGPT on giving a "precise" answer. In other words, ChatGPT misinterpreted the term 'analytic'. When I reminded the LLM that 'analytic' meant the answer could be expressed entirely in symbols, it performed the task perfectly.

On the other hand, when I prompted ChatGPT to help my friend prepare for a chemist position at Apple, O1 gave a thorough answer that included a couple of creative suggestions, such as browsing Apple's environmental policies and commitments ahead of an interview to be able to talk about how such policies could be taken into account in the lab.

ChatGPT-O1 isn't a top 500 math student yet, but it is an altogether impressive model.
