
data = open("rosalind_revc.txt")
d = data.readline()
print(d)
print("\n")
d = d.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(d)