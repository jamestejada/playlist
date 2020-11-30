FULL_ATTR_LIST = [
    'cut', 'delay', 'plays', 'sec', 'ter',
    'segue', 'function', 'time', 'begend',
    'chain', 'rotate', 'type', 'comment', 'line_id',
    'start_time', 'end_time', 'fostart', 'folength',
    'libloc', 'libname', 'guid', 'order_id'
]

def to_text(line_generator, output_path):
    output_list = [make_line(line) for line in line_generator]

    with open(output_path, 'w+') as outfile:
        outfile.writelines(output_list)


def add_defaults(line_dict):
    for attr in FULL_ATTR_LIST:
        line_dict.update(
            {attr: line_dict.get(attr, '') if line_dict.get(attr) is not None else ''}
        )
    return line_dict

def unpack(cut='', function='', delay='', plays='', sec='', ter='', segue='',
                time='', begend='', chain='', rotate='', type='', comment='',
                line_id='', start_time='', end_time='', fostart='', folength='',
                libloc='', libname='', guid='', order_id=''):
    return (
    cut, function, delay, plays, sec, ter, segue, time,
    begend, chain, rotate, type, comment,
    line_id, start_time, end_time, fostart, folength,
    libloc, libname, guid, order_id
    )

def make_line(line_dict):
    full_dict = add_defaults(line_dict)

    (
    cut, function, delay, plays, sec, ter, segue, time,
    begend, chain, rotate, type, comment,
    line_id, start_time, end_time, fostart, folength,
    libloc, libname, guid, order_id
    ) = unpack(**full_dict)

    return (
        f'{cut:5}{function:1}{delay:8}{plays:2}{sec:1}{ter:1}{segue:1}{time:8}{begend:1}'
        + f'{chain:8}{rotate:8}{type:1}{comment:35}{line_id:10}{start_time:7}{end_time:7}'
        + f'{fostart:7}{folength:7}{libloc:2}{libname:8}{guid:36}{order_id:5}\n'
        )
