from modules.settings import FIND_REPLACE_PATH, OUTPUT_DIRECTORY
from modules.transform.xml_playlist_to_df_list import XML_Playlist_Transform

# temp?
import json
from modules.settings import CUT_TITLE_PATH
with open(CUT_TITLE_PATH.joinpath('cut_titles.json'), 'r') as infile:
    CUT_TITLES = json.load(infile)

class XML_Replace(XML_Playlist_Transform):

    OUTPUT_DIR = OUTPUT_DIRECTORY

    # override
    def build_dict(self):
        return None
    
    def replace(self, find_cut, replace_cut):
        for record in self.xml_record_list:
            current_cut_number = record.find('cut')
            if record.find('cut').text == find_cut:
                record.find('cut').text = replace_cut
                # temp?
                record.find('comment').text = CUT_TITLES.get(record.find('cut').text).get('title')
        
        self.tree.write(self.OUTPUT_DIR.joinpath(self.file_path.name))


def replace_cut(find_cut, replace_cut):
    for each_file in FIND_REPLACE_PATH.iterdir():
        parser = XML_Replace(each_file)
        parser.replace(find_cut, replace_cut)
