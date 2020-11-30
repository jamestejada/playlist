import pandas as pd
from pandas import ExcelWriter


def to_excel(df_dict, output_path):
    dataframe = pd.DataFrame.from_dict(df_dict)

    with ExcelWriter(output_path, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, sheet_name=output_path.stem, index=False)
