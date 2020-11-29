from pathlib import Path
import pandas as pd
from pandas import ExcelWriter

# Move this later
OUTPUT_PATH = Path.cwd().joinpath('output')


def to_excel(df_dict, file_name):

    dataframe = pd.DataFrame.from_dict(df_dict)
    
    with ExcelWriter(OUTPUT_PATH.joinpath(file_name), engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, f'{file_name}.xlsx')

# def none_to_blank()