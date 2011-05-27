__author__ = 'joemellor'

import Bio
from Bio import SeqIO
from Bio import pairwise2

s2 = "ATCGATGAATTCGAGCTCGTATCAC"
s3 = "CCGTCGACCTGCAGCGTACG"
s4 = "CGGTGTCGGTCTCGTAG"

for record in SeqIO.parse("/Users/joemellor/Downloads/ion.sff", "sff"):

    s1 = record.seq[:100]

    align = pairwise2.align.localms(s1,s2, 2, -1, -2, -2)
    seq1, seq2a, score1, Rstart, Rend = align[0]

    align = pairwise2.align.localms(s1,s3, 2, -1, -2, -2)
    seq1, seq2b, score2, Rstart, Rend = align[0]

    align = pairwise2.align.localms(s1,s4, 2, -1, -2, -2)
    seq1, seq2c, score3, Rstart, Rend = align[0]

    score = score1 + score2 + score3
    if score > 110:
        print(s1)
        print(seq2a)
        print(seq2b)
        print(seq2c)
        print(score)
        print("\n")
    