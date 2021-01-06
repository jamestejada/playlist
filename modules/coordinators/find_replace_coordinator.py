from modules.settings import DEFAULT_PLAYLISTS, FIND_REPLACE_PATH
from modules.transform.find_replace_xml import XML_Replace
from modules.write.to_xml import to_xml


class Find_Replace_Control:
    EXIT_FLAGS = ['quit', 'q', 'exit']

    def __init__(self, find_cut=None, replace_cut=None, change_defaults=False):
        self.find_cut = self.verify_cut(
            find_cut or input('Find: ')
            )
        self.replace_cut = self.verify_cut(
            replace_cut or input('Replace With: ')
            )
        self.input_dir = DEFAULT_PLAYLISTS if change_defaults else FIND_REPLACE_PATH
        self.write = to_xml
    
    def replace_cuts(self):
        self.write( 
            [
                XML_Replace(each_file).replace(self.find_cut, self.replace_cut)
                for each_file in self.input_dir.iterdir()
            ]
        )
    
    def verify_cut(self, cut_input):
        if self.check_exit(cut_input):
            exit()

        try:
            assert 0 < int(cut_input) <= 99999, 'Cut Number is out of range'
            assert len(cut_input) == 5, 'Cut Number must be 5 digits'
            return str(cut_input)

        except AssertionError as e:
            print(e)
            self.retry()
        except ValueError:
            print('A Cut Number must be, well....a number.')
            self.retry()

    def retry(self):
        new_cut_input = input('Please enter a valid Cut Number: ')
        return self.verify_cut(new_cut_input)
    
    def __str__(self):
        return f'Finding {self.find_cut} and replacing it with {self.replace_cut}'

    def check_exit(self, console_input) -> bool:
        return any([(arg in self.EXIT_FLAGS) for arg in console_input])


def main():
    finder = Find_Replace_Control().replace_cuts()



if __name__ == '__main__':
    main()
