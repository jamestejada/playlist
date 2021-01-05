from modules.transform.find_replace_xml import replace_cut


class Find_Replace_Control:
    def __init__(self, find_cut=None, replace_cut=None):
        self.find_cut = self.verify_cut(
            find_cut or input('Enter cut to find and replace: ')
            )
        self.replace_cut = self.verify_cut(
            replace_cut or input('Enter the replacement cut: ')
            )
    
    def verify_cut(self, cut_input):
        assert len(cut_input) == 5
        assert 0 < int(cut_input) <= 99999

# Pick up here. 1/4/2021

def main():
    replace_cut('00017', '98851')


if __name__ == '__main__':
    main()
