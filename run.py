import os
from pathlib import Path
from modules.xml_playlist_extract import XML_Playlist_Extract
from modules.xml_cuts_to_database import XML_Cuts_Extract

# Next:
#   - Make sure the chain event works.

def main():
    pass
    # - find all input files by looking in input directories
    #   EXAMPLE:
    #       excel_to_text_playlist = os.listdir(excel_to_text_playlist_dir)
    # - apply corresponding module to each file in the input directory
    # - apply output module depending on input dir


    # NOTES:
    # - maybe organize modules by "pipe"
    #   - input dir
    #   - processing
    #   - output


    playlist_extractor = XML_Playlist_Extract(
        Path.cwd().joinpath('input', 'xml_to_excel', 'JZ2-TUE.xml')
    )
    # print(playlist_extractor)

    cut_extractor = XML_Cuts_Extract(
        Path.cwd().joinpath('input', 'xml_cuts_to_database', 'cuts.xml')
    )
    for cut_no in ['64862', 64862, '64863', 64863, 100, '100']:
        print(cut_extractor.is_cut_available(cut_no))

if __name__ == '__main__':
    main()
