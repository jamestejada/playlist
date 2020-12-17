import sys
from pathlib import Path

def from_cwd(*path_list):
    directory = Path.cwd().joinpath(*path_list)
    directory.mkdir(exist_ok=True, parents=True)
    return directory


def check_flags(flags) -> bool:
    return any([(arg in flags) for arg in sys.argv[1:]])


CHAIN = check_flags(['chain'])

CUTS_TO_DB_DIR = from_cwd('input', 'xml_cuts_to_database')
XML_TO_EXCEL_DIR = from_cwd('input', 'xml_to_excel')
EXCEL_TO_PLAYLIST_DIR = from_cwd('input', 'excel_to_text_playlist')

INPUT_DIR_LIST = [
    CUTS_TO_DB_DIR,
    XML_TO_EXCEL_DIR, 
    EXCEL_TO_PLAYLIST_DIR
    ]

OUTPUT_DIRECTORY = from_cwd('output')
DEFAULT_PLAYLISTS = from_cwd('input', 'default_playlists_xml')