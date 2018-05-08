# Dikshya Acharya
# CS-327-1, Spring 2018


from spectrum import cyclic_spectrum
from scoring import scoring
import collections
import heapq


def leaderboard(n, exp_spectrum):
    leader_board = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    leader_peptide = "0"
    while len(leader_board) != 0:
        dict_cyclic_peptide = collections.defaultdict(list)
        leader_board = branch(leader_board)
        iter_candidate = list(leader_board)
        for peptide in iter_candidate:
            cyclic_theo = cyclic_spectrum(peptide)
            max_cyclic_theo = max(cyclic_theo)
            max_exp_spectrum = max(exp_spectrum)
            if max_cyclic_theo > max_exp_spectrum:
                leader_board.remove(peptide)
            elif max_cyclic_theo <= max_exp_spectrum:
                score_peptide = scoring(cyclic_theo, exp_spectrum)
                dict_cyclic_peptide[score_peptide].append(peptide)
                leader_cyclic = cyclic_spectrum(leader_peptide)
                score_leader = scoring(leader_cyclic, exp_spectrum)
                if score_peptide > score_leader:
                    leader_peptide = peptide
        top_N_list = get_top_N_scores(dict_cyclic_peptide, n)
        leader_board = get_top_scorers(dict_cyclic_peptide, top_N_list, n)

    return leader_peptide


def get_top_N_scores(dict_cyclic_peptide, n):
    req_top_scores = heapq.nlargest(n, dict_cyclic_peptide.keys())
    return req_top_scores


def get_top_scorers(dict_cyclic_peptide, top_n_score, n):
    top_scorers_peptide = []
    for scores in top_n_score:
        if len(top_scorers_peptide) < n:
            peptide_for_that_score = dict_cyclic_peptide[scores]
            top_scorers_peptide.extend(peptide_for_that_score)

    return top_scorers_peptide


def branch(bldg_block):
    integer_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    candidate_peptides = []
    for i in bldg_block:
        for j in integer_masses:
            candidate_peptides.append(str(i) + '-' + str(j))

    return candidate_peptides


def check(leaderboard_output, answer):
    leaderboard_list = leaderboard_output.split('-')
    leaderboard_list = [int(i) for i in leaderboard_list]
    leaderboard_list.sort()
    answer_list = answer.split('-')
    answer_list = [int(i) for i in answer_list]
    answer_list.sort()
    if leaderboard_list == answer_list:
        print("Test passed.\nThe correct leaderboard cyclopeptide sequence is : ", leaderboard_list)

    else:
        print("The correct leaderboard cyclopeptide sequence is : ", answer_list)
        print("What you got is : ", leaderboard_list)

    print()


def read_input(filename):
    my_file = open(filename, 'r')
    n_val = int(my_file.readline().rstrip('\n'))
    exp_spectrum = my_file.readline().rstrip('\n').split(' ')
    exp_spectrum = [int(i) for i in exp_spectrum]
    answer = my_file.readline().rstrip('\n')
    output = leaderboard(n_val, exp_spectrum)
    check(output, answer)


def main():
    read_input('P1_short.txt')
    read_input('P1_long.txt')


if __name__ == '__main__':
    main()

