# Dikshya Acharya
# CS-327-1, Spring 2018

def rev_comp(dna_string):
    reverse_dna = ''
    for element in range(len(dna_string) - 1, -1, -1):
        if dna_string[element] == 'A':
            reverse_dna += 'T'
        elif dna_string[element] == 'T':
            reverse_dna += 'A'
        elif dna_string[element] =='C':
            reverse_dna += 'G'
        else:
            reverse_dna += 'C'

    return reverse_dna


def read_input(text_file):
    data_file = open(text_file)
    dna_string = data_file.readline().rstrip('\n')
    reverse_dna_file = data_file.readline().rstrip('\n')
    reverse_dna_test = rev_comp(dna_string)
    if reverse_dna_file == reverse_dna_test:
        print('Test passed.')
        print('Complementary DNA in reverse: ' + reverse_dna_test)
    else:
        print('Test Failed.')
        print('Incorrect complementary DNA: ' + reverse_dna_test)


def main():
    read_input('short_dna.txt')
    read_input('long_dna.txt')


if __name__ == '__main__':
    main()

