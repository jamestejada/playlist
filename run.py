import os
from pathlib import Path
from modules.read import Read

# Next:
#   - Make sure the chain event works.

def main():
    # input_file = Path.cwd().joinpath('files', 'JZ1-MON.txt')
    # output_file = Path.cwd().joinpath('JZ1-MON-TEST.xlsx')
    # playlist_report = Read(input_file, output_file)
    # print(playlist_report)
    # playlist_report.write_to_excel()

    input_dir = Path('/mnt/n/Tejada/20201016')
    dir_list = os.listdir(input_dir)

    for file_name in dir_list:
        full_path = input_dir.joinpath(file_name)
        output_file = Path.cwd().joinpath('output', f'{full_path.stem}.xlsx')
        playlist_report = Read(full_path, output_file)
        playlist_report.write_to_excel()


if __name__ == '__main__':
    main()
