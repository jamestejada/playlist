import re
import pandas as pd
from pathlib import Path


def get_file_contents(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

def create_dataframe(list_of_tuples: list, headers_list: list):
    assert len(list_of_tuples[0]) == len(headers_list)
    return pd.DataFrame(list_of_tuples, columns=headers_list)

def write_dataframe(dataframe, output_file, log_name='test_output'):
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, log_name, index=False)


def main():

    file_path = Path.cwd().joinpath('files', 'JZ1-MON.txt')
    file_contents = get_file_contents(file_path)

    # output = []
    # for line in file_contents:
    #     if re.search('(\d{5}|HARD\s|SOFT\s)', line):
    #         #                cut,      comment,     typ,     func
    #         output.append(
    #             (
    #                 line[1:6].strip(),  # cut
    #                 line[7:33].strip(), # comment
    #                 line[40].strip(),   # typ
    #                 line[45].strip()    # func
    #             )
    #         )
    output = [
        (
            line[1:6].strip(),  # cut
            line[7:33].strip(), # comment
            line[40].strip(),   # typ
            line[45].strip()    # func
        ) 
        for line in file_contents
        if re.search('(\d{5}|HARD\s|SOFT\s)', line)
        ]

    df = create_dataframe(output, ['cut', 'comment', 'typ', 'func'])

    # write to excel
    write_dataframe(df, 'test_output.xlsx')


if __name__ == '__main__':
    main()
