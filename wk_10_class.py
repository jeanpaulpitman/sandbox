

def main():
    filename = 'songs.csv'
    print(get_longest_line(filename))
    # print(max(open(filename, 'r'), key=len))


def get_longest_line(filename):
    with open(filename, 'r') as in_file:
        line_record = 0
        line_index = 0
        for i, line in enumerate(in_file):
            length = len(line)
            if length > line_record:
                line_record = length
                line_index = i

    return line_index + 1, line_record




main()
