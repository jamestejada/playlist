import os
from pathlib import Path
from modules.transform.xml_playlist_to_excel import XML_Playlist_Transform
from modules.transform.xml_cuts_to_database import XML_Cuts_Transform
from modules.transform.excel_to_text_playlist import Excel_Playlist_Transform
from modules.write.to_excel import to_excel
from modules.write.to_text import to_text

def main():
    # - find all input files by looking in input directories
    #   EXAMPLE:
    #       excel_to_text_playlist = os.listdir(excel_to_text_playlist_dir)
    # - apply corresponding module to each file in the input directory
    # - apply output module depending on input dir


    # TO DO:
    # - maybe organize modules by "pipe"
    #       - input dir
    #       - processing
    #       - output
    # - add SQLite Database
    # - create XML_Cuts_Transform.find_empty_cut_range()
    # - Make sure chain events work.


    # temp
    import pandas as pd

    playlist_transformer = XML_Playlist_Transform(
        Path.cwd().joinpath('input', 'xml_to_excel', 'JZ2-TUE.xml')
    )
    to_excel(playlist_transformer.dataframe_dict, 'JZ2-TUE.xlsx')

    cut_transformer = XML_Cuts_Transform(
        Path.cwd().joinpath('input', 'xml_cuts_to_database', 'cuts.xml')
    )
    to_excel(cut_transformer.dataframe_dict, 'cuts.xlsx')

    excel_transformer = Excel_Playlist_Transform(
        excel_path=Path.cwd().joinpath('data', 'sample_input.xlsx')
    )
    to_text(excel_transformer.lines(), 'sample_playlist.txt')
    # for line in excel_transformer.lines():
    #     print(line)


if __name__ == '__main__':
    main()
