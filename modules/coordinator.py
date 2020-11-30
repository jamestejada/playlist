from modules.settings import (
    CUTS_TO_DB_DIR, EXCEL_TO_PLAYLIST_DIR, XML_TO_EXCEL_DIR
    )
from modules.transform.excel_to_lines import Excel_Playlist_Transform
from modules.transform.xml_cuts_to_df_list import XML_Cuts_Transform
from modules.transform.xml_playlist_to_df_list import XML_Playlist_Transform
from modules.write.to_text import to_text
from modules.write.to_excel import to_excel
from modules.settings import (
    OUTPUT_DIRECTORY, EXCEL_TO_PLAYLIST_DIR, XML_TO_EXCEL_DIR, CUTS_TO_DB_DIR
    )


""" coordinates different execution paths based on input folder.
"""

class Pipeline_Control:
    """This class' get_function() method returns a function that will
    take only the input path and choose correct pipeline based on that.
    """
    PIPELINES = {
        # directory stem(key)
        XML_TO_EXCEL_DIR.stem: (
            # transformer_class    write function     target extension
            XML_Playlist_Transform, to_excel, '.xlsx'),
        CUTS_TO_DB_DIR.stem: (XML_Cuts_Transform, to_excel, '.xlsx'),
        EXCEL_TO_PLAYLIST_DIR.stem: (Excel_Playlist_Transform, to_text, '.txt')
    }
    OUTPUT_DIR = OUTPUT_DIRECTORY

    def __init__(self, input_dir):
        self.input_dir = input_dir

        (
            self.transformer_class,
            self.write_func,
            self.ext 
        ) = self.PIPELINES.get(self.input_dir.stem)

        self.return_func = self.transform_and_write
    
    def get_function(self):
        return self.return_func

    def transform_and_write(self, input_path):
        output_path = self.OUTPUT_DIR.joinpath(f'{input_path.stem}{self.ext}')
        transformer_instance = self.transformer_class(file_path=input_path)
        self.write_func(transformer_instance.output(), output_path)
