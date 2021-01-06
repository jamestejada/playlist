from dateutil.parser import parse
from datetime import datetime, timedelta
from dateutil.parser._parser import ParserError
from dateutil.relativedelta import relativedelta
from modules.settings import MUSIC
from modules.transform.switch_chain_xml import Chain_Day, Chain_Music
from modules.write.to_xml import to_xml


class Chain_Control:

    CHAIN_CLASS = Chain_Music if MUSIC else Chain_Day
    EXIT_FLAGS = ['quit', 'q', 'exit']

    def __init__(self, start_date=None, end_date=None):
        # print("Enter 'q' to Exit...")
        self.start_date = self.parse_date(
            start_date or
            input('Please Enter start date for chain sequence: ')
            )
        self.end_date = self.parse_date(
            end_date or
            input('Please Enter an end date: ')
            )
        self.date_range = self.get_date_range()
        print(
            'Chain Playlists will be created for: ', 
            [date.strftime('%m/%d/%y') for date in self.date_range]
            )
        self.write = to_xml

    # main
    def create_chain_playlists(self):
        playlist_dict_list = [
            self.CHAIN_CLASS(each_date).create()
            for each_date in self.date_range
            ]
        self.write(playlist_dict_list)

    def get_date_range(self):
        delta = self.end_date - self.start_date
        return [
            (self.start_date + timedelta(days=x))
            for x in range(delta.days + 1)
            ]

    def parse_date(self, raw_date_string):
        self.check_exit(raw_date_string)
        
        raw_date_string = raw_date_string.strip()

        try:
            _date_obj = parse(raw_date_string)
        except ParserError:
            # Possible RecursionError, but you really have to be
            # trying hard to break it.
            _date_obj = self.parse_date(
                input('Please Enter a Valid Date: ')
            )
        
        date_obj = self.fix_year(_date_obj)
        return date_obj
    
    def fix_year(self, raw_date_obj):
        today = datetime.today()
        date_obj = raw_date_obj.replace(year=today.year)
        # days=-1 allows us to create playlists for today also
        if (date_obj - today) < timedelta(days=-1):
            # relativedelta is used to avoid errors caused by leap years
            return date_obj + relativedelta(years=1)
        return date_obj

    def check_exit(self, console_input) -> bool:
        if any([(arg in self.EXIT_FLAGS) for arg in console_input]):
            exit()
