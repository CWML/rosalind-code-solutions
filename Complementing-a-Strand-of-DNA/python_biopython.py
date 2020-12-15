from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

data = open("rosalind_revc.txt")
d = data.readline()

my_dna = Seq(d)
print(my_dna.reverse_complement())