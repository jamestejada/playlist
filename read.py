import re
from pathlib import Path


def get_file_contents(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def main():

    file_path = Path.cwd().joinpath('files', 'JZ1-MON.txt')
    file_contents = get_file_contents(file_path)

    output = []
    for line in file_contents:
        if re.search('(\d{5}|HARD\s|SOFT\s)', line):
            #                cut,      comment,     typ,     func
            output.append(
                (
                    line[1:6].strip(),
                    line[7:33].strip(),
                    line[40].strip(),
                    line[45].strip())
            )

    for line in output:
        print(line)


if __name__ == '__main__':
    main()
