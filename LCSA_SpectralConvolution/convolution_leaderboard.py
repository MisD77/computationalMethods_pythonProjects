# Dikshya Acharya
# CS-327-1, Spring 2018


from spectrum import cyclic_spectrum
from scoring import scoring
from spectral_convolution import convolution
import collections
import heapq


def leaderboard(m, n, exp_spectrum):
    my_bldg_blocks = convolution(m, exp_spectrum)
    leader_board = my_bldg_blocks
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
        if len(top_scorers_peptide) <= n:
            peptide_for_that_score = dict_cyclic_peptide[scores]
            top_scorers_peptide.extend(peptide_for_that_score)

    return top_scorers_peptide


def branch(bldg_blocks):
    integer_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    candidate_peptides = []
    for i in bldg_blocks:
        for j in integer_masses:
            candidate_peptides.append(str(i) + '-' + str(j))

    return candidate_peptides


def read_input(filename):
    f = open(filename, 'r')
    m = int(f.readline().rstrip('\n'))
    n = int(f.readline().rstrip('\n'))
    exp_str = f.readline().rstrip('\n').split(' ')
    exp = [int(i) for i in exp_str]
    ans = f.readline().rstrip('\n')
    return m, n, exp, ans

def sum_allMasses(sequence):
    sum = 0;
    for mass in sequence:
        sum += mass
    return sum

def check_answer(leaderboard, answer):
    leaderboard_sum = sum_allMasses(leaderboard)
    answer_sum = sum_allMasses(answer)
    if leaderboard_sum == answer_sum:
        print('Test passed. The leader peptide from convolution leaderboard algorithm is : ', answer)
    else:
        print('Test failed. The leader peptide from convolution leaderboard algorithm is : ', answer)
    print()


def run_leaderboard(file_name):
    m, n, exp, ans = read_input(file_name)
    leader_output = leaderboard(m, n, exp)
    leader_output = sorted([int(i) for i in leader_output.split('-')])
    ans = sorted([int(i) for i in ans.split('-')])
    check_answer(leader_output, ans)


def main():
    run_leaderboard('P2_short.txt')
    run_leaderboard('P2_long.txt')


if __name__ == '__main__':
    main()

