# Dikshya Acharya
# CS-327-1, Spring 2018


from Bio.SubsMat import MatrixInfo
from subsequences import find_lcs_alignment
import numpy as np


def score_backtrack(dna_v, dna_w):
    sigma = 5
    available_matrix = MatrixInfo.blosum62
    m = len(dna_w) + 1
    n = len(dna_v) + 1
    score_matrix = np.zeros((n, m), dtype=int)
    b_matrix = np.zeros((n, m), dtype=int)
    score_matrix[0][0] = 0
    for i in range(1, n):
        score_matrix[i][0] = -i*sigma

    for j in range(1, m):
        score_matrix[0][j] = -j*sigma

    for i in range(1, n):
        for j in range(1, m):
            a = (dna_v[i - 1], dna_w[j - 1])
            if a in available_matrix:
                s = available_matrix[a]
            else:
                a = (dna_w[j - 1], dna_v[i - 1])
                s = available_matrix[a]

            top = score_matrix[i - 1][j] - sigma
            side = score_matrix[i][j - 1] - sigma
            diagonal = score_matrix[i - 1][j - 1] + s

            score_matrix[i][j] = max(top, side, diagonal)

            if score_matrix[i][j] == score_matrix[i - 1][j] - sigma:
                b_matrix[i][j] = -1

            elif score_matrix[i][j] == score_matrix[i][j - 1] - sigma:
                b_matrix[i][j] = 1
            else:
                b_matrix[i][j] = 0

    return score_matrix[n-1][m-1], b_matrix


def read_input(filename):
    f = open(filename, 'r')
    dna_v = f.readline().rstrip('\n')
    dna_w = f.readline().rstrip('\n')
    score_answer = int(f.readline().rstrip('\n'))
    v_align_answer = f.readline().rstrip('\n')
    w_align_answer = f.readline().rstrip('\n')
    score, b_matrix = score_backtrack(dna_v, dna_w)
    check(dna_v, dna_w, score, score_answer, v_align_answer, w_align_answer, b_matrix)


def check(dna_v, dna_w, score, score_file, v_align_file, w_align_file, b_matrix):
    v_align_output, w_align_output = find_lcs_alignment(b_matrix, dna_v, dna_w)
    if score == score_file and v_align_file == v_align_output and w_align_file == w_align_output:
        print("Test passed.")
        print("The output score is: ", score)
        print("The correct alignment: ")
        print(v_align_output)
        print(w_align_output)
    else:
        print("Test failed.")
        print("The correct score is: ", score_file)
        print("The correct alignment: ")
        print(v_align_file)
        print(w_align_file)
    print()


def main():
    read_input('P3_short.txt')
    read_input('P3_long.txt')


if __name__ == '__main__':
    main()

