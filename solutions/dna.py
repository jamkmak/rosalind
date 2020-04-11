'''
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

'''

# Counting DNA Nucleotides (DNA)
def DNA(string):
    s = string.upper()
        A = s.count('A')
        C = s.count('C')
        G = s.count('G')
        T = s.count('T')
        output = str(A)+' '+str(C)+' '+str(G)+' '+str(T)
    return output
# Returns a string of the number of ACGT nucleotides 
# counted, separated by spaces.
