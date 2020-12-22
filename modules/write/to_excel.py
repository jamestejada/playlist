import json
import pandas as pd
from pandas import ExcelWriter
from modules.settings import CUT_TITLE_PATH


def to_excel(df_dict, output_path):
    dataframe = pd.DataFrame.from_dict(df_dict)

    # create cut-title json database (to be able to look up title by cut number)
    if output_path.stem == 'cuts':
        cut_title_df = dataframe.filter(['cut', 'title'], axis=1)
        cut_title_df.set_index(['cut'], inplace=True)
        with open(CUT_TITLE_PATH.joinpath('cut_titles.json'), 'w') as outfile:
            json.dump(cut_title_df.to_dict(orient='index'), outfile)

    with ExcelWriter(output_path, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, sheet_name=output_path.stem, index=False)
