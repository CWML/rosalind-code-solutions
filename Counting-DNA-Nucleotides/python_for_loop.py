countA = 0
countC = 0
countG = 0
countT = 0

data = open("rosalind_dna.txt", "r")
d = data.readline()

#print(d)

for i in d:
	if i == "A":
		countA = countA + 1
	elif i == "C":
		countC = countC + 1
	elif i == "G":
		countG = countG + 1
	elif i == "T":
		countT = countT + 1
print('first answer using for loop')
print(countA, countC, countG, countT)
print('\nsecond answer using count function')
print(d.count("A"), d.count("C"), d.count("G"), d.count("T"))
