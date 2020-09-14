from collections import defaultdict


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

test_input = [
    {
        'cut': 'HARD',
        'func': 'L',
        'time': '12:00:00',
        'begend': '2',
        'chain': '0',
        'typ': 'T'
    },
    {
        'cut': '12000',
        'func': 'A',
        'typ': 'P'
    },
    {
        'cut': '00007',
        'func': 'A',
        'typ': 'P'
    },
    {
        'cut': '98523',
        'func': 'L',
        'typ': 'P'
    }
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


output = []
for line in test_input:
    new_line = {}
    print(line)
    for key in attr_list:
        new_line[key] = line.get(key, '')
    output.append(make_line(**new_line))
print(output)

with open('playlist.txt', 'w+') as outfile:
    outfile.writelines(output)