from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

my_dna = Seq("AGTACACTGGT")
print(my_dna.transcribe())