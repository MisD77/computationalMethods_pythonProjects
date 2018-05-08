# Dikshya Acharya
# CS-327-1, Spring 2018

from frequent_words import pattern_to_number, number_to_pattern


def computing_frequencies(dna_string, k):
    freq_list = [0] * (4 ** k)
    for index in range(len(dna_string) - (k - 1)):
        k_pattern = dna_string[index: index+k]
        pattern_num = pattern_to_number(k_pattern)
        freq_list[pattern_num] += 1

    return freq_list


def frequent_words_faster(dna_string, k):
    freq_word_list = []
    freq_list = computing_frequencies(dna_string, k)
    max_count = max(freq_list)
    for index in range(len(freq_list)):
        if freq_list[index] == max_count:
            pattern = number_to_pattern(index, k)
            freq_word_list.append(pattern)

    return freq_word_list


def read_input(filename):
    my_file = open(filename)
    dna_text = my_file.readline().rstrip('\n')
    k_num = int(my_file.readline().rstrip('\n'))
    output = my_file.readline().rstrip('\n')
    output_list = output.split()
    my_test_output = frequent_words_faster(dna_text, k_num)

    if output_list == my_test_output:
        print('Test passed.')
        print('The correct list is: ', my_test_output)
    else:
        print('Test Failed.')
        print('The incorrect list is: ', my_test_output)
    print()

def main():
    read_input('P12_short.txt')
    read_input('P12_long.txt')


if __name__ == "__main__":
    main()