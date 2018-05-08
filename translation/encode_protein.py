#Dikshya Acharya
#CS-327-1, Spring 2018

def translate(mRNA_string):
    peptide_chain = ''
    for index in range(0, len(mRNA_string), 3):
        rna_codon = mRNA_string[index:index+3]
        peptide_chain += codon_table(rna_codon)

    return peptide_chain


def codon_table(codon):
    amino_acid_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
                        "UCU":"S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
                        "UAG": "*", "UGA": "*", "UAA": "*", "UGU": "C","UGC": "C", "UGG": "W",
                        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P",
                        "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I",
                        "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S",
                        "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
			            "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D",
                        "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    return amino_acid_table[codon]

