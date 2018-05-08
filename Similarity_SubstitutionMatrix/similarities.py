# Dikshya Acharya
# CS-327-1, Spring 2018

from Bio.SubsMat import MatrixInfo
from decimal import Decimal
import math


def similarity(aa_seq_1, aa_seq_2):
    available_matrix = MatrixInfo.blosum55
    score = 0
    similarity_percent = 0
    for i in range (len(aa_seq_1)):
        if aa_seq_1[i] == aa_seq_2[i]:
            similarity_percent += 1

        a = (aa_seq_1[i], aa_seq_2[i])
        if a in available_matrix:
            score += available_matrix[a]

        else:
            a = (aa_seq_2[i], aa_seq_1[i])
            score += available_matrix[a]

    score_percent = similarity_percent/len(aa_seq_2)
    score_percent = math.ceil(score_percent * 100)
    return score, score_percent


def read_input(filename):
    f = open(filename, 'r')
    seq_1 = f.readline().rstrip('\n')
    seq_2 = f.readline().rstrip('\n')
    similarity_score = f.readline().rstrip('\n')
    similarity_score = int(similarity_score)
    similarity_percent = f.readline().rstrip('\n')
    similarity_percent = math.ceil(Decimal(similarity_percent))
    score, score_percent = similarity(seq_1, seq_2)
    check(score, score_percent, similarity_score, similarity_percent)


def check(answer_score, answer_percent, similarity_score, similarity_percent):
    if (answer_score == similarity_score) and (answer_percent == similarity_percent):
        print("Test passed.")
        print("The correct similarity score is : ", answer_score)
        print('The correct similarity percentage is: ', answer_percent)
    else:
        print("Test failed")
        print("The correct similarity score is : ", similarity_score)
        print('The correct similarity percentage is: ', math.ceil(similarity_percent))
    print()


def main():
    read_input('P1_short.txt')
    read_input('P1_long.txt')


if __name__ == "__main__":
    main()