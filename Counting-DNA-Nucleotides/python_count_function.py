data = open("rosalind_dna.txt", "r")
d = data.readline()
print('\nsecond answer using count function')
print(d.count("A"), d.count("C"), d.count("G"), d.count("T"))
