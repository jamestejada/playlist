import pytest
from modules.coordinators.chain_coordinator import Chain_Control
from modules.coordinators.find_replace_coordinator import Find_Replace_Control
from modules.coordinators.pipe_coordinator import Pipeline_Control
from modules.settings import INPUT_DIR_LIST, CHAIN, FIND, TESTING

    # TO DO:
    #   - ***Implement `INJECT XML PLAYLIST` into program
    #   - FEATURE IDEA: add ability to get 
    #       1. x number of sequential cuts
    #       2. list of unused cuts.
    #           - add SQLite Database to speed this feature up.
    #   DONE - Make sure chain events work. After importing playlist.
    #   - Create module that automatically copies files from
    #     from network drive.
    #   DONE- See if you can send raw UDP commands to DAD to export
    #     XML files. IT WORKS!!! ASCII -> bytes


# Add this comment to readme instead of a note in the entry point file.

    # NOTE: After rewriting the top level for asynchronous code, 
    #       I have found that the synchronous code was actually faster.
    #       The bottleneck in this program is in opening cuts.xml (~5.6s)
    #       because it is 1,786,116 lines. Writing to "cuts.xlsx" takes ~5.4s.
    #       The actual processing takes ~0.16 seconds


def main():
    if TESTING:
        pytest.main()
    elif CHAIN:
        Chain_Control().create_chain_playlists()
    elif FIND:
        Find_Replace_Control().replace_cuts()
    else:
        for each_directory in INPUT_DIR_LIST:
            process_directory(each_directory)
        print('DONE')


def process_directory(directory):
    print(f'Getting pipeline from Pipeline_Control for {directory.stem}...')
    pipeline = Pipeline_Control(directory)
    pipeline_func = pipeline.get_function()

    for each_file in directory.iterdir():
        print(f'processing {each_file.name}')
        pipeline_func(each_file)


if __name__ == '__main__':
    main()