# Dikshya Acharya
# CS-327-1, Spring 2018

import collections


def scoring(theo_spec, exp_spec):
    score = 0
    theo_count = collections.Counter(theo_spec)  # gives the count of each integer in the list
    exp_count = collections.Counter(exp_spec)  # gives the count of each integer in the list
    for key in theo_count:  # iterating over the dictionary
        if theo_count[key] == exp_count[key]:
            score = score + exp_count[key]  # add the count to the score if both list has equal count of certain integer
        else:
            score = score + min(theo_count[key], exp_count[key])  # else add the minimum count of each list

    return score


def read_input(filename):
    my_file = open(filename, 'r')
    theoretical_spec = my_file.readline().rstrip('\n').split(' ')
    theoretical_spec = [int(i) for i in theoretical_spec]
    experimental_spec = my_file.readline().rstrip('\n').split(' ')
    experimental_spec = [int(i) for i in experimental_spec]
    answer = int(my_file.readline().rstrip('\n'))
    output = scoring(theoretical_spec, experimental_spec)
    if output == answer:
        print("Test passed. \nThe correct scoring is ", output)

    else:
        print("Test failed. \nYour scoring is ", output+ "\nThe correct scoring is", answer)

    print()


def main():
    read_input('score_short.txt')
    read_input('score_long.txt')


if __name__ == '__main__':
    main()
