from pathlib import Path
import xml.etree.ElementTree as ET

import pandas as pd
from pandas import ExcelWriter


xml_cuts_path = Path.cwd().joinpath('data', 'cuts.xml')
output_path = Path.cwd().joinpath('CUTS_DATABASE.xlsx')

def find_attr(attribute, encoPlaylistRecord):
    return encoPlaylistRecord.find(attribute).text or ''

def main():
    tree = ET.parse(xml_cuts_path)
    enco = tree.getroot()
    db = enco.find('encoCutDatabase')
    records = db.findall('encoCutRecord')

    # To find unused cuts
    # possible_cuts = [x for x in range(100000)]
    # actual_cuts = []

    # for record in records:
    #     actual_cuts.append(int(record.find('cut').text))
    
    # print(set(possible_cuts).difference(set(actual_cuts)))

    # BUILD DATABASE
    (
        cut_list, 
        title_list, 
        group_list, 
        length_list, 
        tot_length_list, 
        startdate_list, 
        lastpldate_list, 
        recorddate_list, 
        killdate_list
    ) = ([] for _ in range(9))

    for record in records:
        cut_list.append(find_attr('cut', record))
        title_list.append(find_attr('title', record))
        group_list.append(find_attr('group', record))
        length_list.append(find_attr('length', record))
        tot_length_list.append(find_attr('tot_length', record))
        startdate_list.append(find_attr('startdate', record))
        lastpldate_list.append(find_attr('lastpldate', record))
        recorddate_list.append(find_attr('recorddate', record))
        killdate_list.append(find_attr('killdate', record))

    dataframe_dict = {
        'cut': cut_list,
        'title': title_list,
        'group': group_list,
        'length': length_list,
        'tot_length': tot_length_list,
        'startdate': startdate_list,
        'lastpldate': lastpldate_list,
        'recorddate': recorddate_list,
        'killdate': killdate_list

    }

    df = pd.DataFrame.from_dict(dataframe_dict)
    print(df)
    with ExcelWriter(output_path) as writer:
        df.to_excel(writer, 'ALL CUTS', index=None)


if __name__ == '__main__':
    main()
