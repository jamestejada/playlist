import pytest
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from modules.transform.switch_chain_xml import Chain_Day, Chain_Music
from modules.settings import TEST_DATA_PATH


input_files = [
    TEST_DATA_PATH.joinpath(file_name)
    for file_name in TEST_DATA_PATH.iterdir()
    ]

today = datetime.today()
one_year = relativedelta(years=1)
end_of_year = today.replace(month=12, day=28)

test_dates_this_week = [
    today + timedelta(days=x) for x in range(7) 
    if (today + timedelta(days=x)).weekday() in [0, 4, 5]
]
test_dates_next_year = [
    date + relativedelta(years=1) for date in test_dates_this_week
]
test_dates_for_playlists = [*test_dates_this_week, *test_dates_next_year]

test_range_this_week = [today + timedelta(days=x) for x in range(7)]
test_range_end_of_year = [end_of_year + timedelta(days=x) for x in range(7)]
test_range = [*test_range_this_week, *test_range_end_of_year]

negative_test_range_this_week = [today - timedelta(days=x) for x in range(7)]
negative_test_range_end_of_year = [
    end_of_year - timedelta(days=x) for x in range(7)
    ]
negative_test_range = [*negative_test_range_this_week, *negative_test_range_end_of_year]

full_test_range = [*test_range, *negative_test_range]


@pytest.mark.parametrize("input_file", input_files)
@pytest.mark.parametrize("date_obj", test_dates_for_playlists)
@pytest.mark.parametrize("station", ['JZ', 'OP', 'TOQ'])
def test_Chain_Day_replace_chain(date_obj, input_file, station):
    test_obj = Chain_Day(date_obj)
    chain_to = test_obj.default_playlists.get(station)[0].get('chain')
    test_xml = test_obj.replace_chain(input_file, chain_to)
    test_root = test_xml.getroot()

    expected_xml = ET.parse(input_file)
    expected_root = expected_xml.getroot()
    playlist = expected_root.find('encoPlaylistDatabase')
    records = playlist.findall('encoPlaylistRecord')
    chain_record = [record for record in records if record.find('cut').text == 'CHAIN']

    for chain in chain_record:
        chain.find('chain').text = chain_to
    
    assert len(chain_record) == 1
    assert ET.tostring(test_root) == ET.tostring(expected_root)


@pytest.mark.parametrize('date_obj', test_range)
def test_Chain_Day_get_chain_to_date(date_obj):
    chain_to_date = Chain_Day(date_obj).get_chain_to_date()

    assert chain_to_date == date_obj + timedelta(days=1)


@pytest.mark.parametrize('date_obj', full_test_range)
def test_Chain_Day_get_playlist_date(date_obj):
    playlist_date = Chain_Day(date_obj).get_playlist_date(date_obj)

    assert playlist_date == (
            date_obj 
            if (date_obj - today) > timedelta(days=-1)
            else date_obj + relativedelta(years=1)
        )

@pytest.mark.parametrize('date_obj', full_test_range)
def test_Chain_Day_get_day_string(date_obj):
    day_of_week_string = Chain_Day(date_obj).get_day_string(date_obj)

    assert date_obj.strftime('%A')[:3].upper() == day_of_week_string


@pytest.mark.parametrize("date_obj", test_range)
def test_Chain_Day_get_defaults(date_obj):
    test_dict = Chain_Day(date_obj).get_defaults()

    day_number = date_obj.weekday() + 1
    date_string = date_obj.strftime('%m%d')

    chain_to_date = date_obj + timedelta(days=1)

    chain_to_number = chain_to_date.weekday() + 1
    chain_to_date_string = chain_to_date.strftime('%m%d')

    day_of_week = date_obj.strftime('%A')[:3].upper()

    if day_number == 5:
        expected_dict = {
            'JZ': [{
                'input': f'JZ{day_number}-{day_of_week}',
                'output': f'JZ{day_number}-{date_string}',
                'chain': f'JZ{chain_to_number}{chain_to_date_string}A'
                }],
            'OP': [{
                'input': f'OP{day_number}-{day_of_week}',
                'output': f'OP{day_number}-{date_string}',
                'chain': f'OP{chain_to_number}{chain_to_date_string}A'
                }],
            'TOQ': [{
                'input': f'TOQ{day_number}{day_of_week}',
                'output': f'TOQ-{date_string}',
                'chain': f'TOQ{chain_to_date_string}A'
                }]
        }
    elif day_number == 6:
        expected_dict = {
            'JZ': [
                {
                    'input': f'JZ{day_number}-{day_of_week}A',
                    'output': f'JZ{day_number}{date_string}A',
                    'chain': f'JZ{day_number}{date_string}B'
                },
                {
                    'input': f'JZ{day_number}-{day_of_week}B',
                    'output': f'JZ{day_number}{date_string}B',
                    'chain': f'JZ{chain_to_number}-{chain_to_date_string}'
                }
            ],
            'OP': [
                {
                    'input': f'OP{day_number}-{day_of_week}A',
                    'output': f'OP{day_number}{date_string}A',
                    'chain': f'OP{day_number}{date_string}B'
                },
                {
                    'input': f'OP{day_number}-{day_of_week}B',
                    'output': f'OP{day_number}{date_string}B',
                    'chain': f'OP{chain_to_number}-{chain_to_date_string}'
                }
            ],
            'TOQ': [
                {
                    'input': f'TOQ{day_number}{day_of_week}A',
                    'output': f'TOQ{date_string}A',
                    'chain': f'TOQ{date_string}B'
                },
                {
                    'input': f'TOQ{day_number}{day_of_week}B',
                    'output': f'TOQ{date_string}B',
                    'chain': f'TOQ-{chain_to_date_string}'
                }
            ]
        }
    else:
        expected_dict = {
            'JZ': [{
                'input': f'JZ{day_number}-{day_of_week}',
                'output': f'JZ{day_number}-{date_string}',
                'chain': f'JZ{chain_to_number}-{chain_to_date_string}'
                }],
            'OP': [{
                'input': f'OP{day_number}-{day_of_week}',
                'output': f'OP{day_number}-{date_string}',
                'chain': f'OP{chain_to_number}-{chain_to_date_string}'
                }],
            'TOQ': [{
                'input': f'TOQ{day_number}{day_of_week}',
                'output': f'TOQ-{date_string}',
                'chain': f'TOQ-{chain_to_date_string}'
                }]
        }

    assert expected_dict == test_dict

    # Write Tests for Chain_Music