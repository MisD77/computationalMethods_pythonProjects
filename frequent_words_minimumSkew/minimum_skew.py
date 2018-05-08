# Dikshya Acharya
# CS-327-1, Spring 2018

import matplotlib.pyplot as plt


def print_skew(dna_string):
    diff = 0
    diff_d_c_list = [diff]
    g_count = 0
    c_count = 0
    for letter in dna_string:
        if letter == 'G':
            g_count += 1
        elif letter == 'C':
            c_count += 1
        diff = g_count - c_count
        diff_d_c_list.append(diff)

    min_diff = min(diff_d_c_list)
    index_list = []
    for index in range(len(diff_d_c_list)):
        if diff_d_c_list[index] == min_diff:
            index_list.append(index)

    return diff_d_c_list, index_list


def plot_skew(g_c_diff_list):
    plt.plot(g_c_diff_list)
    plt.ylabel('skew')
    plt.xlabel('position')
    plt.title('Minimum Skew Chart')
    plt.show()


def read_input(filename):
    my_file = open(filename)
    dna_string = my_file.readline().rstrip('\n')
    output = my_file.readline().rstrip('\n')
    output_list = output.split()
    output_list = list(map(int, output_list))
    my_output = print_skew(dna_string)
    if  my_output[1] == output_list:
        print("The test passed. The correct index list is: " , my_output[1])
        plot_skew(my_output[0])

    else:
        print("The test failed. The incorrect index list is: ", my_output[1])
        plot_skew(my_output[0])
    print()


def main():
    read_input("P3_short.txt")
    read_input("P3_long.txt")


if __name__ == "__main__":
    main()






