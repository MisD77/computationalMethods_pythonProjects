# Dikshya Acharya
# CS-327-1, Spring 2018

def count(text, pattern):
    count = 0
    for index in range(len(text)-(len(pattern)-1)):
        element = text[index: index + len(pattern)]
        if element == pattern:
            count += 1

    return count


def read_input(text_file):
    data_file = open(text_file)
    dna_string = data_file.readline().rstrip('\n')
    dna_pattern = data_file.readline().rstrip('\n')
    total_count = int(data_file.readline().rstrip('\n'))
    test_count = count(dna_string, dna_pattern)
    if total_count == test_count:
        print('Test passed.')
        print('The correct total number of times the pattern is repeated in DNA string: ' + str(test_count))
    else:
        print('Test Failed.')
    print()


def main():
    read_input('pattern1.txt')
    read_input('pattern2.txt')

if __name__ == '__main__':
    main()