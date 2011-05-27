__author__ = 'joemellor'


import Bio
from Bio import pairwise2

from ABIFReader import *

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


#file = open('4.ab1', 'r')
#reader = ABIFReader('/Users/joemellor/Downloads/sequences/4.ab1') # creates an instance of ABIFReader
#reader.version # version of ABIF file
#reader.showEntries() # print all entries of ABIF file "<name> (<num>) / <type> (<size>)"
#template = reader.getData('PBAS') # read data for entry named <name> with number <num>, by default <num> is 1
#reader.close() # close the file, since it is kept open
#print(data)

s1 = ""
s2 = "ATCGATGAATTCGAGCTCGTATCAC"
s3 = "CCGTCGACCTGCAGCGTACG"
s4 = "CGGTGTCGGTCTCGTAG"
s5 = "GATGTCCACGAGGTCTCT"
#align = pairwise2.align.localds(template,s1,scoredict,-2,-2)
#seq1, seq2, score, Lstart, Lend = align[0]

align = pairwise2.align.localds(s1,s2,scoredict,-3,-3)
seq1, seq2, score, Rstart, Rend = align[0]
print(seq2)
print(seq1)
align = pairwise2.align.localds(s1,s3,scoredict,-3,-3)
seq1, seq2, score, Rstart, Rend = align[0]
print(seq2)
align = pairwise2.align.localds(s1,s4,scoredict,-3,-3)
seq1, seq2, score, Rstart, Rend = align[0]
print(seq2)
align = pairwise2.align.localds(s1,s5,scoredict,-3,-3)
seq1, seq2, score, Rstart, Rend = align[0]
print(seq2)