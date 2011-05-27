__author__ = 'joemellor'

from weblogolib import *
fin = open('cap.fa')
seqs = read_seq_data(fin)
data = LogoData.from_seqs(seqs)
options = LogoOptions()
options.title = "A Logo Title"
format = LogoFormat(data, options)
fout = open('cap.eps', 'w')
eps_formatter( data, format, fout)