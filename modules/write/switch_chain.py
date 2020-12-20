from modules.settings import OUTPUT_DIRECTORY, DEFAULT_PLAYLISTS
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import xml.etree.ElementTree as ET


class Chain_Day:
    """ Creates dated playlists that have only require the chain event changed
    """
    STATIONS = ['JZ', 'OP', 'TOQ']
    INPUT = DEFAULT_PLAYLISTS
    OUTPUT = OUTPUT_DIRECTORY

    def __init__(self, playlist_date: object):
        self._today = datetime.today()
        self.playlist_date = self.get_playlist_date(playlist_date)
        self.chain_to_date = self.get_chain_to_date()
        self.day_of_week = self.get_day_string(self.playlist_date)
        self.chain_to_day_of_week = self.get_day_string(self.chain_to_date)
        self.default_playlists = self.get_defaults()

    def create(self):
        for station in self.STATIONS:
            for io_dict in self.default_playlists.get(station):

                input_file = self.INPUT.joinpath(f'{io_dict.get("input")}.xml')
                output_file = self.OUTPUT.joinpath(f'{io_dict.get("output")}.xml')
                chain_to = io_dict.get('chain')

                self.replace_chain(input_file, output_file, chain_to)
    
    def replace_chain(self, input_file, output_file, chain_to):
        xml = ET.parse(input_file)
        enco = xml.getroot()
        playlist = enco.find('encoPlaylistDatabase')
        records = playlist.findall('encoPlaylistRecord')

        chain_record = [record for record in records if record.find('cut').text == 'CHAIN']
        assert len(chain_record) == 1

        for chain in chain_record:
            chain.find('chain').text = chain_to
        
        xml.write(output_file)
    
    def get_playlist_date(self, input_date):
        """Takes in datetime object (input_date) and returns datetime
        object adjusted for only future dates
        """
        if (input_date - self._today) < timedelta(days=-1):
            # days=-1 allows us to create playlists for today also
            return input_date + relativedelta(years=1)
            # relativedelta is used to avoid errors caused by leap years
        return input_date

    def get_chain_to_date(self):
        return self.playlist_date + timedelta(days=1)

    def get_day_string(self, date_obj):
        """ Gets only the first 3 letters of the day of week
        and capitalizes all letters.
        """
        return date_obj.strftime('%A')[:3].upper()
    
    def get_defaults(self):
        day_number = self.playlist_date.weekday() + 1
        date_string = self.playlist_date.strftime('%m%d')

        chain_to_number = self.chain_to_date.weekday() + 1
        chain_to_date_string = self.chain_to_date.strftime('%m%d')

        if day_number == 5:
            return {
                'JZ': [{
                    'input': f'JZ{day_number}-{self.day_of_week}',
                    'output': f'JZ{day_number}-{date_string}',
                    'chain': f'JZ{chain_to_number}{chain_to_date_string}A'
                    }],
                'OP': [{
                    'input': f'OP{day_number}-{self.day_of_week}',
                    'output': f'OP{day_number}-{date_string}',
                    'chain': f'OP{chain_to_number}{chain_to_date_string}A'
                    }],
                'TOQ': [{
                    'input': f'TOQ{day_number}{self.day_of_week}',
                    'output': f'TOQ-{date_string}',
                    'chain': f'TOQ{chain_to_date_string}A'
                    }]
            }
        if day_number == 6:
            return {
                'JZ': [
                    {
                        'input': f'JZ{day_number}-{self.day_of_week}A',
                        'output': f'JZ{day_number}{date_string}A',
                        'chain': f'JZ{day_number}{date_string}B'
                    },
                    {
                        'input': f'JZ{day_number}-{self.day_of_week}B',
                        'output': f'JZ{day_number}{date_string}B',
                        'chain': f'JZ{chain_to_number}-{chain_to_date_string}'
                    }
                ],
                'OP': [
                    {
                        'input': f'OP{day_number}-{self.day_of_week}A',
                        'output': f'OP{day_number}{date_string}A',
                        'chain': f'OP{day_number}{date_string}B'
                    },
                    {
                        'input': f'OP{day_number}-{self.day_of_week}B',
                        'output': f'OP{day_number}{date_string}B',
                        'chain': f'OP{chain_to_number}-{chain_to_date_string}'
                    }
                ],
                'TOQ': [
                    {
                        'input': f'TOQ{day_number}{self.day_of_week}A',
                        'output': f'TOQ{date_string}A',
                        'chain': f'TOQ{date_string}B'
                    },
                    {
                        'input': f'TOQ{day_number}{self.day_of_week}B',
                        'output': f'TOQ{date_string}B',
                        'chain': f'TOQ-{chain_to_date_string}'
                    }
                ]
            }
        return {
            'JZ': [{
                'input': f'JZ{day_number}-{self.day_of_week}',
                'output': f'JZ{day_number}-{date_string}',
                'chain': f'JZ{chain_to_number}-{chain_to_date_string}'
                }],
            'OP': [{
                'input': f'OP{day_number}-{self.day_of_week}',
                'output': f'OP{day_number}-{date_string}',
                'chain': f'OP{chain_to_number}-{chain_to_date_string}'
                }],
            'TOQ': [{
                'input': f'TOQ{day_number}{self.day_of_week}',
                'output': f'TOQ-{date_string}',
                'chain': f'TOQ-{chain_to_date_string}'
                }]
        }


class Chain_Music(Chain_Day):
    STATIONS = [
        'CLA',
        'JAZ',
        # 'PSJ',
        # 'CLST'
        ]
    
    # override
    def get_defaults(self):
        day_number = self.playlist_date.weekday() + 1
        date_string = self.playlist_date.strftime('%m%d')

        chain_to_number = self.chain_to_date.weekday() + 1
        chain_to_date_string = self.chain_to_date.strftime('%m%d')

        default_dict = {
            'PSJ': [{
                'input': f'PSJ{day_number}-{self.day_of_week}',
                'output': f'PSJ-{date_string}',
                'chain': f'PSJ-{chain_to_date_string}'
                }],
            'CLST': [{
                'input': f'CLST{day_number}{self.day_of_week}',
                'output': f'CLST{date_string}',
                'chain': f'CLST{chain_to_date_string}'
                }],
            'JAZ': [{
                'input': f'JAZ{day_number}-{self.day_of_week}',
                'output': f'JAZ-{date_string}',
                'chain': f'JAZ-{chain_to_date_string}'
                }],
            'CLA': [{
                'input': f'CLA{day_number}-{self.day_of_week}',
                'output': f'CLA-{date_string}',
                'chain': f'CLA-{chain_to_date_string}'
                }]
        }

        if day_number == 5:
            default_dict.update({
                'PSJ': [{
                    'input': f'PSJ{day_number}-{self.day_of_week}',
                    'output': f'PSJ-{date_string}',
                    'chain': f'PSJ{chain_to_date_string}A'
                    }]
            })
        if day_number == 6:
            default_dict.update({
                'PSJ': [
                    {
                        'input': f'PSJ-{day_number}A',
                        'output': f'PSJ{date_string}A',
                        'chain': f'PSJ{date_string}B'
                    },
                    {
                        'input': f'PSJ-{day_number}B',
                        'output': f'PSJ{date_string}B',
                        'chain': f'PSJ{chain_to_date_string}A'
                    }
                ]
            })
        if day_number == 7:
            default_dict.update({
                'PSJ': [
                    {
                        'input': f'PSJ-{day_number}A',
                        'output': f'PSJ{date_string}A',
                        'chain': f'PSJ-{chain_to_date_string}'
                    }
                ]
            })
        return default_dict


