# Dikshya Acharya
# CS-327-1, Spring 2018

import collections
import heapq


def convolution(most_M, exp_spectrum):
    diff_list = []
    # For every integer exp_spectrum, finding the difference between it and every other value.
    for integer_mass_i in exp_spectrum:
        for integer_mass_j in exp_spectrum:
            diff = integer_mass_i - integer_mass_j
            if (diff >= 57) and (diff <= 200):  # add to the list only if diff is greater than 57 and less than 200
                diff_list.append(diff)
    diff_list_count = collections.Counter(diff_list)  # gives the count of each difference in the list
    dict_diff = collections.defaultdict(list)  # creating a dict that can hold list as values
    for key, val in diff_list_count.items():  # add to this dictionary the diff as values and count as keys
        dict_diff[val].append(key)

    top_m_count = top_count_list(dict_diff, most_M)  # get the list of top m counts

    m_mass = highest_m_mass(dict_diff, most_M, top_m_count)  # get the m list of top diff(masses)
    return m_mass


# get the list of top m counts
def top_count_list(dict_diff, m):
    return heapq.nlargest(m, dict_diff.keys())


# get the m list of top diff(masses)
def highest_m_mass(dict_diff, most_M, top_m_count):
    top_m_masses = []
    for count in top_m_count:
        if len(top_m_masses) < most_M:
            mass = dict_diff[count]
            top_m_masses.extend(mass)
    return top_m_masses


def read_input(filename):
    my_file = open(filename, 'r')
    M_val = my_file.readline().rstrip('\n')
    M_val = int(M_val)
    exp_spectrum = my_file.readline().rstrip('\n').split(' ')
    exp_spectrum = [int(i) for i in exp_spectrum] # changing exp_spectrum list to integers
    correct_answer = my_file.readline().rstrip('\n').split(' ')
    correct_answer = [int(i) for i in correct_answer]
    test_output = convolution(M_val, exp_spectrum)
    check(correct_answer, test_output, M_val)


def check(answer, output, M):
    answer.sort()
    output.sort()

    if answer == output:
        print('Test passed. The correct top ', M,' values are : ', output)
    else:
        print('Test failed. The correct top ', M,' values are: ', answer,'\nYou got is:', output)
    print()


def main():
    read_input('P1_short.txt')
    read_input('P1_long.txt')


if __name__ == "__main__":
    main()