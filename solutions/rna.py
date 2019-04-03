'''
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

'''

# Transcribing DNA into RNA (RNA)
def RNA(string):
    DNA = string.upper()
    RNA = ''
    RNA = DNA.replace('T','U')
    return RNA
	
# Replaces every instance of 'T' with 'U' and stores result as RNA. Returns RNA.