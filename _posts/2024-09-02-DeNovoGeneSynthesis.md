---
layout: post
title: The central dogma, broken
categories: science biology genetics
author: David
description: Two labs have discovered a new mechanism in bacteria that allows them to synthesize a new gene from an RNA element. A gene that writes a gene. Wow.
---


There is this awesome pair of papers that just came out in Science. Briefly, these labs described a mechanism wherein a system in bacteria encodes a retrotransposase and an RNA. These elements are inactive until the bacteria are infected, at which point the infected cell transcribes these elements. The retrotransposase is then active, and binds to the RNA element. The RNA element is a little bit weird--it can self-hybridize and essentially makes a loop. 

The really awesome part about this is that the retrotransposase creates DNA out of the RNA, but once it finishes the loop... it does not stop! It keeps going, and going, and going. It synthesizes one enormous new gene called Neo that is then translated into a repetitive protein. This repetitive protein acts as a toxin, and sends the bacterial cell into hibernation. In other words, the bacteria reads its own DNA, makes some RNA and makes some Protein, to make some DNA to make some RNA to make some protein to do something. That hurt your head? It sure hurt mine.

The levels of ingenuity in this thing are amazing. Since the retrotransposase is making a gene, this gene needs a promoter. It has a promoter! Not only does it have a promoter--it has the exact consensus sequence for a promoter (insert optimality statement here). But the entire loop also cannot contain a single in-frame stop codon, so it doesn't. And the mechanism for strand switching so that the loop can continue indefinitely has to be in-frame, so of course it involves exactly three bases. It is a fascinating finding that deeply challenges the way we understand how genomes encode information. In essence, this is a program that contains the instructions for how to write a new program. That is something we had never seen before. 

Finally, the bioinformatics in this are simply amazing. The authors first identified systems containing retrotransposases that are adjacent to non-coding RNAs. They looked specifically for immune-associated systems. In one case, the authors took a system from one bacterial species and placed it into E. coli, showing that it confers immunity to a couple of viruses. They then characterized this system, and let's just say the bioinformatics are wild. 

I like these papers because none of the experiments individually are unbelievably difficult, but rather because the logical sequence is so captivatingly clear, the analyses are incisive and lead to falsifiable tests, which are taken seriously and then taken to their logical conclusions. The result is a beautiful dissection of a circuit that nobody has ever seen before, with wide-ranging implications for our conceptual understanding of biology.

I strongly invite you to read these two papers:

 * __De novo gene synthesis by an antiviral reverse transcriptase__

 * __Phage-triggered reverse transcription assembles a toxic repetitive gene from a non-coding RNA__