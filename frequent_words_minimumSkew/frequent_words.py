# Dikshya Acharya
# CS-327-1, Spring 2018


def pattern_to_number(dna_string):
    number_value_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if len(dna_string) == 0:
        return 0
    else:
        letter = dna_string[len(dna_string)-1]
        prefix = dna_string[0: len(dna_string)-1]
        return 4 * pattern_to_number(prefix) + number_value_dict[letter]


def read_input_P2a(filename):
    my_file = open(filename)
    pattern = my_file.readline().rstrip('\n')
    index = int(my_file.readline().rstrip('\n'))
    my_index = pattern_to_number(pattern)
    if index == my_index:
        print('Test passed.')
        print('The correct index for ', pattern, ' is: ', my_index)
    else:
        print('Test Failed.')
        print('The incorrect index for ', pattern, ' is: ', my_index)
    print()


def number_to_pattern(index, k_mer_size):
    number_value_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if k_mer_size == 1:
        for number in str(index):
            for kee in number_value_dict:
                if number == str(number_value_dict[kee]):
                    return kee
    else:
        letter = ''
        prefix_index = index // 4
        remainder = index % 4
        for kee in number_value_dict:
            if remainder == number_value_dict[kee]:
                letter = kee
        prefix_pattern = number_to_pattern(prefix_index, k_mer_size - 1)
        return prefix_pattern + letter


def read_input_P2b(filename):
    my_file = open(filename)
    index = int(my_file.readline().rstrip('\n'))
    k_mer_size = int(my_file.readline().rstrip('\n'))
    pattern = my_file.readline().rstrip('\n')
    my_pattern = number_to_pattern(index, k_mer_size)
    if pattern == my_pattern:
        print('Test passed.')
        print('The correct pattern for the index ', str(index), ' is: ', my_pattern)
    else:
        print('Test Failed.')
        print('The incorrect pattern for the ', str(index), ' is: ', my_pattern)
    print()


def main():
    read_input_P2a('P2a_short.txt')
    read_input_P2a('P2a_long.txt')
    read_input_P2b('P2b_short.txt')
    read_input_P2b('P2b_long.txt')


if __name__ == "__main__":
    main()


