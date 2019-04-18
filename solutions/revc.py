'''
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

# Complementing a Strand of DNA (REVC)
def complement(string):
    DNA = string.upper()
    comp = ''
    comp_list = []
    for n in DNA:           
        if n == 'A':
            comp += 'T'
        elif n == 'C':
            comp += 'G'
        elif n == 'G':
            comp += 'C'
        elif n == 'T':
            comp += 'A'
    comp_list = list(comp)           # converts string comp to a list
    comp_list.reverse()              # reverses the list
    comp_final = "".join(comp_list)  # rejoins the list
    return comp_final                # returns final complementary strand of DNA

	                             # (could have also done comp[::-1] to reverse list)