# Dikshya Acharya
# CS-327-1, Spring 2018


from backtrack import backtrack_matrix


# Gives the longest common sequence
def find_lcs(b_matrix, dna_v, dna_w):
    n = len(b_matrix)
    m = len(b_matrix[0])
    i = n-1
    j = m-1
    max_match = ""
    while i > 0 and j > 0:
        if b_matrix[i][j] == -1:
            i -= 1
        elif b_matrix[i][j] == 1:
            j -= 1
        elif b_matrix[i][j] == 0 and dna_v[i-1] == dna_w[j-1]:
            max_match += dna_w[j-1]
            i -= 1
            j -= 1

    max_match_rev = max_match[::-1]

    return max_match_rev


# Gives the alignment of v and w
def find_lcs_alignment(b_matrix, dna_v, dna_w):
    n = len(b_matrix)
    m = len(b_matrix[0])
    i = n - 1
    j = m - 1
    v_sub = ''
    w_sub = ''
    while i > 0 and j > 0:
        if b_matrix[i][j] == -1:
            v_sub += dna_v[i-1]
            w_sub += '-'
            i -= 1
        elif b_matrix[i][j] == 1:
            v_sub += '-'
            w_sub += dna_w[j-1]
            j -= 1
        elif b_matrix[i][j] == 0:
            v_sub += dna_v[i-1]
            w_sub += dna_w[j-1]
            i -= 1
            j -= 1

    if i == 1 and j == 0:
        v_sub += dna_v[i - 1]
        w_sub += '-'

    if i == 0 and j == 1:
        v_sub += '-'
        w_sub += dna_w[j - 1]

    v_sub_rev = v_sub[::-1]
    w_sub_rev = w_sub[::-1]

    return v_sub_rev, w_sub_rev


def read_input_lcs(filename):
    f = open(filename, 'r')
    dna_v = f.readline().rstrip('\n')
    dna_w = f.readline().rstrip('\n')
    b_matrix = backtrack_matrix(dna_v, dna_w)
    answer_sequence = f.readline().rstrip('\n')
    output_sequence = find_lcs(b_matrix, dna_v, dna_w)
    check(answer_sequence, output_sequence)


def read_input_lcs_alignment(filename):
    f = open(filename, 'r')
    dna_v = f.readline().rstrip('\n')
    dna_w = f.readline().rstrip('\n')
    answer_v_sub = f.readline().rstrip('\n')
    answer_w_sub = f.readline().rstrip('\n')
    b_matrix = backtrack_matrix(dna_v, dna_w)
    output_v_sub, output_w_sub = find_lcs_alignment(b_matrix, dna_v, dna_w)
    check_alignment(answer_v_sub, answer_w_sub, output_v_sub, output_w_sub)


def check(answer_sequence, output_sequence):
    if answer_sequence == output_sequence:
        print("Test passed. The correct longest common sequence is: ", output_sequence)
    else:
        print("Test failed. The correct longest common sequence is: ", answer_sequence)
    print()


def check_alignment(answer_v_sub, answer_w_sub, output_v_sub, output_w_sub):
    if answer_v_sub == output_v_sub and answer_w_sub == output_w_sub:
        print("Test passed. The correct alignment is: ", output_v_sub,' and ', output_w_sub)
    else:
        print("Test failed. The correct longest common sequence is: ", answer_v_sub, ' and ',answer_w_sub)
        print("Test failed. your alignment is: ", output_v_sub,' and ', output_w_sub)
    print()


def main():
    print("Longest common sequences:")
    print()
    print("The shorter text:")
    read_input_lcs('P2a_short.txt')
    print("The longer text:")
    read_input_lcs('P2a_long.txt')
    print()
    print("Alignments:")
    print()
    print("The shorter text:")
    read_input_lcs_alignment('P2b_short.txt')
    print("The longer text:")
    read_input_lcs_alignment('P2b_long.txt')


if __name__ == "__main__":
    main()