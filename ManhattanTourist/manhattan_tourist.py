# Dikshya Acharya
# CS-327-1, Spring 2018

import numpy as np


def mtp(n, m, vertical_edge, horizontal_edge):
    m_matrix = np.zeros((n, m))
    # getting leftmost values of matrix
    for i in range(1,n):
        m_matrix[i][0] = m_matrix[i-1][0] + vertical_edge[i-1][0]

    # getting leftmost values of matrix
    for j in range(1,m):
        m_matrix[0][j] = m_matrix[0][j-1] + horizontal_edge[0][j-1]

    # for each other node, getting the maximum of m_matrix[i][i-1] or m_matrix[i-1][j]
    for i in range(1, n):
        for j in range(1, m):
            m_matrix[i][j] = max(m_matrix[i][j-1]+horizontal_edge[i][j-1], m_matrix[i-1][j]+vertical_edge[i-1][j])

    return m_matrix[n-1][m-1]


def read_input(filename):
    f = open(filename, 'r')
    size = f.readline().rstrip('\n').split(" ")
    size = [int(i) for i in size]
    n = size[0]
    m = size[1]
    vertical_edge = np.zeros((n-1, m))
    horizontal_edge = np.zeros((n, m-1))

    #reading n-1 lines from the file
    for i in range(n-1):
        vertical_edge[i] = f.readline().rstrip('\n').split(' ')
        vertical_edge[i] = [int(j) for j in vertical_edge[i]]

    dash = f.readline().rstrip('\n')

    #reading n lines from the file
    for i in range(n):
        horizontal_edge[i] = f.readline().rstrip('\n').split(' ')
        horizontal_edge[i] = [int(j) for j in horizontal_edge[i]]

    output = int(f.readline().rstrip('\n'))
    max_answer = mtp(n, m, vertical_edge, horizontal_edge)
    check(max_answer, output)


def check(answer, output):
    if answer == output:
        print('Test passed. The correct longest path is: ', answer)
    else:
        print('Test failed. The correct longest path is: ', output)
    print()


def main():
    read_input('P2_short.txt')
    read_input('P2_long.txt')


if __name__ == "__main__":
    main()