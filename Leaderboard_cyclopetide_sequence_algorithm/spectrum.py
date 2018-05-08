# Dikshya Acharya
# CS-327-1, Spring 2018


def cyclic_spectrum(amino_acid_seq):
    cyclic_seq_list = [0];
    num_list = amino_acid_seq.split("-")
    num_list = [int(i) for i in num_list]
    for element in range(len(num_list)):
        x = num_list[element]
        cyclic_seq_list.append(x)
        for j in range(element+1, len(num_list)):
            x += num_list[j]
            cyclic_seq_list.append(x)
        if element >= 2:
            for k in range(0, element-2+1):
                x += num_list[k]
                cyclic_seq_list.append(x)

    cyclic_seq_list.sort()
    return cyclic_seq_list


def read_input(filename):
    my_file = open(filename, 'r')
    amino_acid_seq = my_file.readline().rstrip('\n')
    answer_str = my_file.readline().rstrip('\n').split(' ')
    answer = [int(i) for i in answer_str]
    output = cyclic_spectrum(amino_acid_seq)
    if output == answer:
        print("Test passed.\nThe correct cyclic theoretical spectrum is: ", output)

    else:
        print("The correct list is : ", answer)
        print("What you got is : ", output)
    print()


def main():
    read_input('cyclic_short.txt')
    read_input('cyclic_long.txt')


if __name__ == '__main__':
    main()
