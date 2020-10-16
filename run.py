from pathlib import Path
from modules.read import Read


def main():
    input_file = Path.cwd().joinpath('files', 'JZ1-MON.txt')
    output_file = Path.cwd().joinpath('JZ1-MON-TEST.xlsx')
    playlist_report = Read(input_file, output_file)
    print(playlist_report)
    playlist_report.write_to_excel()


if __name__ == '__main__':
    main()
