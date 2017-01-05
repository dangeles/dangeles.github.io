---
layout: post
title: Some thoughts before the new year
---

There's no better time to start blogging seriously, I suppose than when it's the end.
2016 is finally ending, and I guess I feel like I've gained enough... thoughts to
warrant writing them down in a screen. Who knows, someone might even read them.

First things first: What the heck 2016?

2016 was a bad year for statisticians. It was a year we dislike thouroughly: An outlier.
Usually, what scientists and statisticians like to do with outliers is to ignore them. We like to
take them, look at them for a second and then say, repeat the experiment. Or, if you can't do that,
use a robust method to make it *less informative*.

I suppose that's the difference between statistics and life. Statistics conforms to a certain
set of rules that follow from a certain set of axioms, and the path of a particle is viewed as unimportant except
insofar as it contributes to the greater whole of its distribution. Only changes that lead to altering
the variables that rule over a system are important.
Life also conforms to a certain
set of rules that must be adhered, but the trajectory of the particle (read: me, you) is important. So important
that a very small number of living organisms can profoundly alter the evolution of their future species. Indeed
so important are individuals in our history that our hierarchies are pyramidal structures.

Of course, most of life conforms to statistics, but we experience life exclusively through the lens of a
singularly biased path, from which we derive certain rules that we treat as facts.

The fact that two sides of the same coin, a mathematical formulation of a situation and the experience of that same situation can feel so different, as particularly interesting. An example that
many of us have been thinking about: Why is it that, at a time of statistical improvement in wages and jobs,
so many people seem angry at the governments that has brought about those improvements? Why would people vote
against their statistical success in favor of approaches that are scant on details on how to bring about further improvement
in the variables that govern the statistical framework?

Experience matters. Studying people (and biology) exclusively through the lens of a simple number of variables
is necessarily a reductive approach and some approaches are bound to fail under certain situations. Maybe this
is why biologists like to say that they need to have a 'feeling for the organism'; that is to say, they need to accrue enough experience to intuit what is actually happening on the ground.
Many biologists understand that life has had only two rules, to change and to adapt, for a very long time. They understand that this rule has a corollary: All other rules can change.

The tension between a reductionist (statistical) approach and a holistic approach that brings experience into the question
is one that I am sure every scientist feels. I started out studying biochemistry and molecular biology as an undergrad
at Cornell, where I was taught about the essentiality of single genes. Thus, single genes became very important early
on in my education. Later on, and particularly now that I am in graduate school I have begun studying genomics where
single genes are, well, they are not disdained, but they are less important than the ensemble. This tension between approaches brings me to the following question:

**How do we understand genomics through the point of view of genetics?**

Clearly every transcribed gene is doing something (whether that something is adaptive or not is not important to me).
Some genes are very important. Experience working with a particular system (a phosphatase, for example) or a single
gene can give us a feeling for what that gene behaves like and what its functions are. However, the lens of experience
can also be blinding. We often forget that single genes are studied through assays that are tailor-made to study them.
The effects of certain genes are understood in situations where the phenotype has been observed, and where the
signal-to-noise has been improved as much as possible. Thus, single gene studies, although they provide intuition for a
system, also make us more vulnerable to over-estimating the importance of a system.

On the other hand, studying genomics affords us a birds-eye view of the genetic interactions of an organism. However,
these genetic interactions are typically studied as an ensemble. On average, what happens? What is the most common change? What is the variation in the effects? These questions disregard single genes and emphasize ensembles. By mixing
many genes, however, we sacrifice the intuition about how different compartments in the cell may be working individually to create the whole.

At the end of the day, which one is better? I get the feeling that many biologists distinctly prefer to study single-genes. Genomics is widely viewed as an exclusively descriptive science that provides genetic targets but not answers. I myself feel that genomics had a lot of promise at the turn of the century and almost two decades later the number of successes that genomics can claim in the biomedical field seem to remain both scarce and largely unknown (to me). On the other hand, molecular biologists can claim a small but well-known number of victories against specific diseases. Genetics works, but is also a century older than genomics.

So, **how do we understand genomics through the point of view of genetics?**. How do we bring to bear the power of genetics into genomics? It is clear, at least to me, that genomics has to pierce beyond description and enumeration and be able to perform the analytic work that geneticists are known for. Description and enumeration are important facets of science that are essential, but analytic work is equally important.

**Why has genomics been so description-driven in the past?** I have a couple of ideas (I don't know that they are absolutely right, so please let me know if you disagree...):

 * Cost - It was only recently that sequencing costs have gone down enough so that many labs could do many genomics experiments.
 * Technical Difficulty - Computational biologists who are capable of analyzing genomic data are in short supply (not every lab has one) and they can't always communicate with wet-lab biologists (different training, different background and different skill-set).
 * Tradition - Genome-wide experiments have not been traditionally designed for hypothesis-testing, so people haven't thought about how these experiments would be set up, how they would work and what a positive/negative result would look like.
 * Novelty - Seriously, it's only been a couple of decades.

But I continue to dodge the question. The fact is that we are probably now at a place where tools to analyze genome-wide data are widely available and the expertise to use them is becoming increasingly common. It is only a matter of time until we understand the experiments and the field well-enough to pursue hypothesis-driven questions again.

So: *how*? I think the answer is relatively straight-forward. As a first step, we should think about genetic pathway analysis between genes as a method that can be applied to genomic data. This is what our lab has been working on over the past six months (with surprising ease and success) and other labs are beginning to do this as well, notably Aviv Regev at the Broad Institute.

After an appropriate genetic pathway experiment has been designed, and a genome-wide measurement is selected, we must select a metric through which to compare phenotypes. The simplest and most straight-forward measurement is to perform total correlations between two mutants via some robust linear regression. Correlations with a magnitude near 1 predict interaction between mutants and correlations with magnitude near 0 indicate a low probability of interaction.

Once these metrics and experiments have been decided on, we have two options:
 * Automate - Perform genome-wide correlations and make a statement about total genetic interaction between two genes
 * Hand-curated list analysis - Take into consideration the biochemistry and cellular biology of the genes, and look for multiple interactions between two genes for example. Try to go deeper by analysing subsets (beware of the multiple testing demon!).

That should do it! Simple as that. Just design your experiment, measure it using RNA-seq (probably the best choice for a genome-wide technology at the moment given it is highly quantitative and gene expression has excellent dynamic range), then use align and measure differential expression (using simple, powerful software like Kallisto and Sleuth) and measure correlations in the way you most prefer. Then dig into your data in whatever way you want, realizing that in a single experiment you have performed all the qPCRs your heart could have possible desired, without suffering from the drawbacks qPCR suffers from (namely, what gene do you use as a normalization factor?). There. A descriptive experiment that also tests hypotheses. (And now I just have to publish my preprint...)
