# Dikshya Acharya
# CS-327-1, Spring 2018

from count_patterns import count

def frequent_words(dna_string, k):
    k_mer_dict = {}
    most_frequent_k_mer = []

    for element in range(len(dna_string)-k):
        pattern = dna_string[element: element+k]
        k_mer_count = count(dna_string, pattern)
        k_mer_dict[pattern] = k_mer_count

    k_mer_frequency_list = k_mer_dict.values()
    maximum_k_mer_value = max(k_mer_frequency_list)

    for key_pattern in k_mer_dict:
        if k_mer_dict[key_pattern] == maximum_k_mer_value:
            most_frequent_k_mer.append(key_pattern)

    most_frequent_k_mer.sort()
    return most_frequent_k_mer


def read_input(filename):
    my_file = open(filename)
    dna_string = my_file.readline().rstrip('\n')
    k_val = int(my_file.readline().rstrip('\n'))
    correct_max_kmer = my_file.readline().rstrip('\n')
    correct_max_kmer_list = correct_max_kmer.split()
    max_kmer_list_test = frequent_words(dna_string, k_val)

    if correct_max_kmer_list == max_kmer_list_test:
        print('Test passed.')
        print('The correct frequent words in the given DNA string with length ', k_val, ' is: ', max_kmer_list_test)
    else:
        print('Test Failed.')
        print('The incorrect frequent words in the given DNA string with length ', k_val, ' is: ', max_kmer_list_test)
    print()


def main():
    read_input("P1_short.txt")
    read_input("P1_long.txt")


if __name__ == "__main__":
    main()








