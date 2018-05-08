# Dikshya Acharya
# CS-327-1, Spring 2018


import numpy as np


def backtrack_matrix(dna_v, dna_w):
    m = len(dna_w) + 1
    n = len(dna_v) + 1
    score_matrix = np.zeros((n, m), dtype=int)
    b_matrix = np.zeros((n, m), dtype=int)

    for i in range(1, n):
        for j in range(1, m):
            top = score_matrix[i-1][j]
            side = score_matrix[i][j-1]
            if dna_w[j-1] == dna_v[i-1]:
                diagonal = score_matrix[i-1][j-1] + 1
            else:
                diagonal = score_matrix[i-1][j-1]

            score_matrix[i][j] = max(top, side, diagonal)
            #putting values in backtracking matrix accordingly

            if score_matrix[i][j] == score_matrix[i-1][j]:
                b_matrix[i][j] = -1

            elif score_matrix[i][j] == score_matrix[i][j-1]:
                b_matrix[i][j] = 1

            else:
                b_matrix[i][j] = 0
    return b_matrix


def read_input(filename):
    f = open(filename, 'r')
    dna_v = f.readline().rstrip('\n')
    dna_w = f.readline().rstrip('\n')
    n = len(dna_v) + 1
    m = len(dna_w) + 1
    answer_matrix = np.zeros((n, m), dtype=int)
    for i in range(n):
        answer_matrix[i] = f.readline().rstrip('\n').split(" ")
        answer_matrix[i] = [int(j) for j in answer_matrix[i]]
    output_matrix = backtrack_matrix(dna_v, dna_w)

    check(answer_matrix, output_matrix)


def check(answer_matrix, output_matrix):
    if np.all(answer_matrix) == np.all(output_matrix):
        print('Test passed. The correct backtracking matrix is\n', output_matrix)
        print()

    else:
        print('Test failed. The correct backtracking matrix is\n', answer_matrix)
        print('What you have is\n', output_matrix)
    print()


def main():
    read_input('P1_short.txt')


if __name__ == "__main__":
    main()