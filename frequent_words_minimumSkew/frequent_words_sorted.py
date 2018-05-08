# Dikshya Acharya
# CS-327-1, Spring 2018

from frequent_words import pattern_to_number, number_to_pattern


#  functions that returns the list of mostly occurring kmers using sorted version of indices list
def frequent_words_sorted(dna_string, k):
    indices_list = find_indices(dna_string, k)
    indices_list.sort()     # sorts the indices list in increasing order
    count_list = [1] * len(indices_list)    # creates a count_list of 1 value corresponding to the indices list
    calculate_counts(indices_list, count_list)
    frequent_words = find_max_patterns(count_list, indices_list, k)
    return frequent_words


#  gives the indices for all the patterns in the string
def find_indices(dna_string, k):
    indices_list = []
    for index in range(len(dna_string) - (k-1)):
        pattern = dna_string[index: index+k]
        value = pattern_to_number(pattern)
        indices_list.append(value)

    return indices_list


#  calculates the total count for each pattern
def calculate_counts(indices_list, count_list):
    for element in range(1,len(indices_list)):
        if indices_list[element] == indices_list[element- 1]:
            count_list[element] = count_list[element - 1] + 1


#  from the count_list, gives the list of the patterns that has maximum count, could be one or more
def find_max_patterns(count_list, index_list, k):
    freq_words = []
    maximum_count = max(count_list)
    for element in range(len(index_list)):
        if count_list[element] == maximum_count:
            pattern = number_to_pattern(index_list[element], k)
            freq_words.append(pattern)

    return freq_words


def read_input(filename):
    my_file = open(filename)
    dna_text = my_file.readline().rstrip('\n')
    k_num = int(my_file.readline().rstrip('\n'))
    output = my_file.readline().rstrip('\n')
    output_list = output.split()
    my_test_output = frequent_words_sorted(dna_text, k_num)

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

