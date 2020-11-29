from modules.transform.xml_playlist_to_excel import XML_Playlist_Transform


class XML_Cuts_Transform(XML_Playlist_Transform):
    """ Transforms cut information for writing to database.
    Output is XML_Cuts_Transform.dataframe_dict which can be
    used to build a pandas dataframe for writing output.
    """
    # defaults that override super class.
    FIND_LIST = ['encoCutDatabase', 'encoCutRecord']
    ATTR_LIST = [
        'cut', 'title', 'group', 'tot_length', 'startdate', 'lastpldate',
        'recorddate', 'killdate'
    ]
    # set with all possible cut numbers (as integers)
    COMPARE_SET = set(x for x in range(100000))
    
    # These methods may be in another class later that
    # interacts with the database.
    @property
    def unused_cuts(self) -> list:
        used_cuts_str = self.dataframe_dict.get('cut')
        used_cuts_int = [int(x) for x in used_cuts_str]
        unused_cuts_int = self.COMPARE_SET.difference(set(used_cuts_int))
        return [f"{x:05}" for x in unused_cuts_int]

    def is_cut_available(self, cut_no):
        _cut_no = cut_no if type(cut_no) is str else f"{int(cut_no):05}"
        return 'AVAILABLE' if _cut_no in self.unused_cuts else 'UNAVAILABLE'
    
    def find_empty_cut_range(self, no_of_empty_cuts):
        """finds x number of available sequential cut numbers 
        """
        # Write this later.
        raise NotImplementedError

