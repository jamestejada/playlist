from pathlib import Path
import pandas as pd
from pandas import ExcelWriter

# Move this later
OUTPUT_PATH = Path.cwd().joinpath('output')


def to_excel(df_dict, output_path):

    dataframe = pd.DataFrame.from_dict(df_dict)
    
    with ExcelWriter(output_path, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, sheet_name=output_path.stem, index=False)

# def none_to_blank()