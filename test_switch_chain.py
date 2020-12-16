from dateutil.parser import parse
from modules.write.chain import Chain_Day


def main():
    this_year = Chain_Day(parse('12/26'))
    this_year.create_chain_playlists()

    next_year = Chain_Day(parse('01/20'))
    next_year.create_chain_playlists()
    


if __name__ == '__main__':
    main()
