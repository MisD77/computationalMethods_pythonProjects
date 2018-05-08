# Dikshya Acharya
#  CS-327-1, Spring 2018

integer_mass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
            'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


# linear_spectrum
def linear_spectrum(amino_acid_seq):
    numbers = integer_mass_amino_seq(amino_acid_seq, integer_mass) # gives a list of integer values for each amino acid
    li_list = linear_lists(numbers)
    return li_list


def linear_lists(numbers):
    linear_seq_list = [0]
    for element in range(len(numbers)):
        x = numbers[element]
        linear_seq_list.append(x)
        for i in range(element+1, len(numbers)):
            x += numbers[i]
            linear_seq_list.append(x)

    linear_seq_list.sort()
    return linear_seq_list


# cyclic_spectrum
def cyclic_spectrum(amino_acid_seq):
    numbers = integer_mass_amino_seq(amino_acid_seq, integer_mass) # gives a list of integer values for each amino acid
    cyclic_seq_list = [0]
    for element in range(len(numbers)):
        x = numbers[element]
        cyclic_seq_list.append(x)
        for j in range(element+1, len(numbers)):
            x += numbers[j]
            cyclic_seq_list.append(x)
        if element >= 2:
            for k in range (0, element-2+1):
                x += numbers[k]
                cyclic_seq_list.append(x)

    cyclic_seq_list.sort()
    return cyclic_seq_list


# Helper methods
def integer_mass_amino_seq(amino_acid_seq, spectrum):
    numbers = []
    for element in amino_acid_seq:
        numbers.append(spectrum[element])

    return numbers


# Testing
def read_input1(filename):
    my_file = open(filename, 'r')
    amino_acid = my_file.readline().rstrip('\n')
    answer_str = my_file.readline().rstrip('\n').split(' ')
    answer = [int(i) for i in answer_str]
    output = linear_spectrum(amino_acid)

    if output == answer:
        print("Test passed. The correct linear theoretical spectrum is: ", output)

    else:
        print("Test failed.")
        print("The correct list is : ", answer)
        print("What you got is : ", output)


def read_input2(filename):
    my_file = open(filename, 'r')
    amino_acid = my_file.readline().rstrip('\n')
    answer_str = my_file.readline().rstrip('\n').split(' ')
    answer = [int(i) for i in answer_str]
    output = cyclic_spectrum(amino_acid)
    if output == answer:
        print("Test passed. The correct cyclic theoretical spectrum is: ", output)

    else:
        print("The correct list is : ", answer)
        print("What you got is : ", output)


def main():
    read_input1('P1a_short.txt')
    read_input1('P1a_long.txt')
    print()
    read_input2('P1b_short.txt')
    read_input2('P1b_long.txt')


if __name__ == '__main__':
    main()
