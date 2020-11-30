import asyncio
from modules.coordinator import Pipeline_Control
from modules.settings import INPUT_DIR_LIST


def main():

    # await asyncio.gather(*[process_directory(directory) for directory in INPUT_DIR_LIST])
    for each_directory in INPUT_DIR_LIST:
        process_directory(each_directory)
    print('DONE')
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

def process_directory(directory):
    print(f'Getting pipeline from Pipeline_Control for {directory.stem}...')
    pipeline = Pipeline_Control(directory)
    pipeline_func = pipeline.get_function()

    for each_file in directory.iterdir():
        print(f'processing {each_file.name}')
        pipeline_func(each_file)

if __name__ == '__main__':
    # asyncio.run(main())
    main()