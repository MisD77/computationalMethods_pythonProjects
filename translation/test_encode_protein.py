#Dikshya Acharya
#CS-327-1, Spring 2018

from encode_protein import translate, codon_table

def test_mrna_to_peptide(input, output):
    peptide_chain = translate(input)
    if peptide_chain == output:
        print('Test passed.')
        print('Peptide Chain: ' + peptide_chain)
    else:
        print('Test failed.')
        print('Incorrect Peptide Chain: ' + peptide_chain)


def run_tests():
    file1 = open('shortRNA.txt')
    short_rna = file1.readline().rstrip('\n')
    peptide_chain1 = file1.readline().rstrip('\n')
    test_mrna_to_peptide(short_rna, peptide_chain1)
    print()
    file2 = open('longRNA.txt')
    long_rna = file2.readline().rstrip('\n')
    peptide_chain2 = file2.readline().rstrip('\n')
    test_mrna_to_peptide(long_rna, peptide_chain2)


def main():
    run_tests()


if __name__ == "__main__":
    main()


