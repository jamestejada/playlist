#! bin/env python3
import pandas as pd
import numpy as np
from dateutil.parser import parse
from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path.cwd().joinpath('data', 'input_sample.xlsx')


attr_list = [
    'cut',
    'func',
    'delay',
    'plays',
    'sec',
    'ter',
    'segue',
    'time',
    'begend',
    'chain',
    'rotate',
    'typ',
    'comment',
    'line_id',
    'start_time',
    'end_time',
    'fostart',
    'folength',
    'libloc',
    'libname',
    'guid',
    'order_id'
]


def make_line(cut='', func='', delay='', plays='', sec='', ter='', segue='',
                time='', begend='', chain='', rotate='', typ='', comment='',
                line_id='', start_time='', end_time='', fostart='', folength='',
                libloc='', libname='', guid='', order_id=''):
    return (
        f'{cut:5}{func:1}{delay:8}{plays:2}{sec:1}{ter:1}{segue:1}{time:8}{begend:1}'
        + f'{chain:8}{rotate:8}{typ:1}{comment:35}{line_id:10}{start_time:7}{end_time:7}'
        + f'{fostart:7}{folength:7}{libloc:2}{libname:8}{guid:36}{order_id:5}\n'
        )


def get_dataframe_row_list(path=INPUT_PATH):
    dataframe = pd.read_excel(path)
    dataframe = dataframe.where(dataframe.notnull(), '')
    df_dict = dataframe.to_dict(orient='records')
    return list(map(correct_types_each_line, df_dict))


def correct_types_each_line(line: dict) -> dict:
    # {'cut': 'HARD ', 'comment': '', 'typ': 'T', 'func': 'A', 'time': datetime.time(23, 59), 'begend': 2.0, 'chain': 0.0}
    outdict = {}
    for key, value in line.items():
        if key in ['begend', 'chain'] and not value == '':
            try:
                outdict[key] = int(value)
            except ValueError:
                outdict[key] = value
        elif key in ['time'] and not value == '':
            outdict[key] = value.strftime('%H:%M:%S')
        else:
            outdict[key] = value

    return outdict


def main():
    
    rows = get_dataframe_row_list()

    write_list = []
    for row in rows:
        write_list.append(make_line(**row))

    with open('test_playlist.txt', 'w+') as outfile:
        outfile.writelines(write_list)


if __name__ == '__main__':
    main()
