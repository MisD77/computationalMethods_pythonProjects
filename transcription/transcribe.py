#Dikshya Acharya
#CS-327-1, Spring 2018

def dna_to_rna(DNASeq):
    mRNA = ''
    for element in DNASeq:
        if element == 'A':
            mRNA += 'U'
        elif element == 'T':
            mRNA += 'A'
        elif element == 'C':
            mRNA += 'G'
        else:
            mRNA += 'C'

    return mRNA

