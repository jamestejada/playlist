from pathlib import Path

def from_cwd(*path_list):
    return Path.cwd().joinpath(*path_list)


CUTS_TO_DB_DIR = from_cwd('input', 'xml_cuts_to_database')
XML_TO_EXCEL_DIR = from_cwd('input', 'xml_to_excel')
EXCEL_TO_PLAYLIST_DIR = from_cwd('input', 'excel_to_text_playlist')

OUTPUT_DIRECTORY = from_cwd('output')