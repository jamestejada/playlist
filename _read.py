import re
import pandas as pd
from pathlib import Path



jz1_hol_hard_branches = [
    '23:59:00',
    '01:59:00',
    '02:59:00',
    '03:30:00',
    '03:58:59',
    '04:30:00',
    '04:59:00',
    '05:19:00',
    '05:33:00',
    '05:49:35',
    '05:59:00',
    '06:19:00',
    '06:33:00',
    '06:42:30',
    '06:49:35',
    '06:59:00',
    '07:19:00',
    '07:33:00',
    '07:42:30',
    '07:49:35',
    '07:59:00',
    '08:19:00',
    '08:33:00',
    '08:42:30',
    '08:49:35',
    '08:59:00',
    '09:04:00',
    '09:05:40',
    '09:06:00',
    '10:06:00',
    '10:19:00',
    '10:31:30',
    '10:39:00',
    '10:50:30',
    '10:58:30',
    '11:06:00',
    '11:19:00',
    '11:31:30',
    '11:39:00',
    '11:50:30',
    '11:58:30',
    '12:06:00',
    '13:06:00',
    '14:01:00',
    '14:06:00',
    '14:20:00',
    '14:29:30',
    '14:49:00',
    '14:59:00',
    '15:34:00',
    '15:48:00',
    '15:59:00',
    '16:18:00',
    '16:29:00',
    '16:34:00',
    '16:48:00',
    '16:59:00',
    '17:18:00',
    '17:29:00',
    '17:34:00',
    '17:48:00',
    '17:59:00',
    '18:18:00',
    '18:29:00',
    '18:34:00',
    '18:48:00',
    '18:59:00',
    '19:06:00',
    '20:06:00',
    '21:01:00',
    '21:06:00',
    '21:29:30',
    '21:59:00',
    '22:01:00',
    '22:06:00',
    '22:29:30',
    '22:59:00',
    '23:01:00',
    '23:06:00',
    '23:29:30',
    '23:55:44' # SOFT
]


def get_time():
    for time_str in jz1_hol_hard_branches:
        yield time_str


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

    file_path = Path.cwd().joinpath('files', 'JZ1-HOL.txt')
    file_contents = get_file_contents(file_path)

    times = get_time()
    output = [
        (
            line[1:6].strip(),  # cut
            line[7:33].strip(), # comment
            line[40].strip(),   # typ
            line[45].strip(),    # func
            next(times) if re.search('HARD\s|SOFT\s', line) else '', # time
            2 if re.search('HARD\s|SOFT\s', line) else '', # begend
            0 if re.search('HARD\s|SOFT\s', line) else ''    # chain
        ) 
        for line in file_contents
        if re.search('(\d{5}|HARD\s|SOFT\s)', line)
        ]

    df = create_dataframe(output, ['cut', 'comment', 'typ', 'func', 'time', 'begend', 'chain'])

    # write to excel
    write_dataframe(df, 'test_output.xlsx')


if __name__ == '__main__':
    main()
