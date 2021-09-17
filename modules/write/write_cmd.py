from pathlib import Path

CMD_PATH = Path('/').joinpath('mnt', 'ffa', 'Tejada', 'COMMAND_OUTPUT')
DEFAULT_PLAYLIST_DIR = Path('/').joinpath('mnt', 'ffa', 'Tejada', 'XML', 'Default')
# INPUT_XML_PATH = Path('/mnt/ffa/Tejada/XML_OUTPUT/')
HELPER_OUTPUT = Path('../playlist-helper/output')


def write_cmd_cut(command_cut_file_name: str, lines: list, extract_xml: bool = False, extract_default: bool = False):
    with open(CMD_PATH.joinpath(f'{command_cut_file_name}.CMD'), 'w+') as outfile:
        outfile.write('\"')
        outfile.write('SYSTEM \'DEL C:\\DAD\\*.xml\'\r\n')
        if not extract_xml:
            outfile.write('SYSTEM \'COPY V:\\Tejada\\XML_OUTPUT\\*.xml C:\\DAD\\*.*\'\r\n')
        for line in lines:
            outfile.write(f'{line}\r\n')
        if extract_xml:
            # outfile.write('SYSTEM \'COPY C:\\DAD\\*.xml V:\\Tejada\\XML\\Default\\*.*\'')
            out_path = 'V:\\Tejada\\XML\\Default' if extract_default else 'V:\\Tejada\\XML'
            outfile.write(f'SYSTEM \'DEL {out_path}\\*.xml\'\r\n')
            outfile.write(f'SYSTEM \'COPY C:\\DAD\\*.xml {out_path}\\Default\\*.*\'')
        outfile.write('\"')


def main():
    line_list = [
        f'INJECT XML PLAYLIST {playlist.stem}'
        for playlist in HELPER_OUTPUT.iterdir()
    ]
    print(line_list)
    write_cmd_cut('00456', line_list)


if __name__ == '__main__':
    main()
