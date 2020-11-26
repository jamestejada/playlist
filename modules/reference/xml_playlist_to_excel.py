from pathlib import Path
import xml.etree.ElementTree as ET

import pandas as pd
from pandas import ExcelWriter


xml_path = Path.cwd().joinpath('data', 'JZ2-TUE.xml')
output_path = Path.cwd().joinpath('JZ2-TUE.xlsx')

def find_attr(attribute, encoPlaylistRecord):
    return encoPlaylistRecord.find(attribute).text or ''


def main():
    tree = ET.parse(xml_path)
    enco = tree.getroot()
    db = enco.find('encoPlaylistDatabase')
    records = db.findall('encoPlaylistRecord')

    cut_list = []
    typ_list = []
    func_list = []
    time_list = []
    begend_list = []
    chain_list = []
    comment_list = []

    for record in records:
        cut_list.append(find_attr('cut', record))
        typ_list.append(find_attr('type', record))
        func_list.append(find_attr('function', record))
        time_list.append(find_attr('time', record))
        begend_list.append(find_attr('begend', record))
        chain_list.append(find_attr('chain', record))
        comment_list.append(find_attr('comment', record))

    playlist_dict = {
        'cut': cut_list,
        'comment': comment_list,
        'typ': typ_list,
        'func': func_list,
        'time': time_list,
        'begend': begend_list,
        'chain': chain_list
    }


    df = pd.DataFrame.from_dict(playlist_dict)
    print(df)
    with ExcelWriter(output_path) as writer:
        df.to_excel(writer, 'JZ2-TUE', index=None)


if __name__ == '__main__':
    main()


