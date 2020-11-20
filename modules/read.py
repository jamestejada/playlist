import re
import pandas as pd

# TO DO:
#   -   Figure out a system for adding the correct times to Hard Branches
#       in spreadsheet

class Read:
    """ Reads a DAD ENCO text report of a playlist
    and converts it into a dataframe and excel spreadsheet
    """
    HEADERS = ['cut', 'comment', 'typ', 'func']

    def __init__(self, input_file, output_file):
        self.file_path = input_file
        self.output_path = output_file
        self.file_contents = self.get_file_contents()
        self.row_tuple_list = self.process_contents()
        self.dataframe = self.create_dataframe()

    def get_file_contents(self) -> list:
        with open(self.file_path, 'r') as f:
            return f.readlines()
    
    def process_contents(self, line_list=None):
        lines = line_list or self.file_contents

        return [
            (
                line[1:6].strip(),  # cut
                line[7:33].strip(), # comment
                line[40].strip(),   # typ
                line[45].strip()    # func
            )
            for line in lines
            if re.search('(\d{5}|HARD\s|SOFT\s|CHAIN\s)', line)
        ]

    def create_dataframe(self, line_tuples_list=None, headers=None):
        line_tuples = line_tuples_list or self.row_tuple_list
        header_list = headers or self.HEADERS
        assert len(line_tuples[0]) == len(header_list)

        return pd.DataFrame(line_tuples, columns=header_list)
    
    def __str__(self):
        return str(self.dataframe)

    def write_to_excel(self, sheet_name=None):
        sheet_title = sheet_name or self.file_path.stem
        
        with pd.ExcelWriter(self.output_path, engine='xlsxwriter') as writer:
            self.dataframe.to_excel(writer, sheet_title, index=False)