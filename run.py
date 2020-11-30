import asyncio
from modules.coordinator import Pipeline_Control
from modules.settings import INPUT_DIR_LIST


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



# async generator for process_directory
async def files_in_dir(directory):
    for each_file in directory.iterdir():
        await asyncio.sleep(0.01)
        yield each_file


async def process_directory(directory):
    print(f'Getting pipeline from Pipeline_Control for {directory.stem}...')
    pipeline = Pipeline_Control(directory)
    pipeline_func = await pipeline.get_function()

    async for each_file in files_in_dir(directory):
        print(f'processing {each_file.name}')
        await pipeline_func(each_file)

# async generator for main
async def directories():
    for directory in INPUT_DIR_LIST:
        await asyncio.sleep(0.01)
        yield directory


async def main():
    await asyncio.gather(
        *[
            process_directory(directory) 
            async for directory in directories()
        ]
    )
    print('DONE')


if __name__ == '__main__':
    asyncio.run(main())
