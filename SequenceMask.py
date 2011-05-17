__author__ = 'joemellor'

import Bio

from Bio import pairwise2


scoredict = {}
scoredict[('A','A')] = 2
scoredict[('A','C')] = -1
scoredict[('A','G')] = -1
scoredict[('A','T')] = -1
scoredict[('A','R')] = 2
scoredict[('A','Y')] = -1
scoredict[('A','S')] = -1
scoredict[('A','W')] = 2
scoredict[('A','K')] = -1
scoredict[('A','M')] = 2

scoredict[('C','A')] = -1
scoredict[('C','C')] = 2
scoredict[('C','G')] = -1
scoredict[('C','T')] = -1
scoredict[('C','R')] = -1
scoredict[('C','Y')] = 2
scoredict[('C','S')] = 2
scoredict[('C','W')] = -1
scoredict[('C','K')] = -1
scoredict[('C','M')] = 2

scoredict[('G','A')] = -1
scoredict[('G','C')] = -1
scoredict[('G','G')] = 2
scoredict[('G','T')] = -1
scoredict[('G','R')] = 2
scoredict[('G','Y')] = -1
scoredict[('G','S')] = 2
scoredict[('G','W')] = -1
scoredict[('G','K')] = 2
scoredict[('G','M')] = -1

scoredict[('T','A')] = -1
scoredict[('T','C')] = -1
scoredict[('T','G')] = -1
scoredict[('T','T')] = 2
scoredict[('T','R')] = -1
scoredict[('T','Y')] = 2
scoredict[('T','S')] = -1
scoredict[('T','W')] = 2
scoredict[('T','K')] = 2
scoredict[('T','M')] = -1

template = "AMWGAMWTGGGGGCGGKCKCGTCGTGGCSAAGTGYCKCATAAGCTTKATATCSACTGTGGAATTCGCCCTKCAAGCAGAAGAGGGGATACGAGATCYGTCTMCCWTWCSTGCTGAACCGATCTTCCGAKCTCTTAKWTTACTAGCATGCTCRGYTAGSGCTATGAACGAATGYTTTACCWTGGCTWCGCRGMTWAWTGATAATGTGCCGKTAGKATTATCCTARGRAGAAGMCCCTYATARGCMGAMAACRAGGMTWGTGATTTCKTGGRGWAAAGYWAGGYAYYYTTGARATTKARCRGCWAACTYCCAATCWAGMCMSWAAGAGGMAAAACTAYGTWGWAGYTGTSMTTCYGGRCMKCTYTTTYAATTTTWAGATYGRAAGAGCGTCGWGWAGGRMAASARCGWMMKAGTGGWCCCWTCTWYGGRYTTATWTKGRGGGTGTSCGAYWCAATCYGCGGGGSCCCYAGTTTACWCYTMAGAATAGAAWWGAATGGGTGKTTTTTATAAAKACGTACTCYTYAGGAAATACTTTCACMAGTTTATGTCWAYAGYAGGCGAGGATAAACTATTGCKCCRWTACCCRTGCTAGKAGCSCAATCYMAYGCATATATSAGMTCGTASACKCKTYTRGCTRRGRTRSCRGTGTMGATCTCGKAKGCCGYCKTMTSMTTRAGGGCGRATTYCACAWGGTMKMTSAGCTYGKSGAAACCRCYAAYYTAGAGSGGGSCASGKRKYAYTTTTWGTTCGCCATAGAGAGTYC"

s1 = "CCAATGTGGAATTCGCCCTT"
s2 = "AAGGGCGAATTCCACAGTGGA"

align = pairwise2.align.localds(template,s1,scoredict,-2,-2)
seq1, seq2, score, start, end = align[0]
print(seq1)
print(seq2)
print(start)
print(end)

align = pairwise2.align.localds(template,s2,scoredict,-2,-2)
seq1, seq2, score, start, end = align[0]
print(seq1)
print(seq2)
print(start)
print(end)

