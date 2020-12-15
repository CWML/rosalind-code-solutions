library(stringr)
file = read.delim("small_dna_sample.txt", sep = "")
string_dna = colnames(file)
print(paste(str_count(string_dna, pattern = "A"), str_count(string_dna, pattern = "G"), str_count(string_dna, pattern = "C"), str_count(string_dna, pattern = "T")), sep = " ")