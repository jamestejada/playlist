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
            current_cut_number = record.find('cut').text
            if current_cut_number == find_cut:
                current_cut_number = replace_cut
                record.find('comment').text = CUT_TITLES.get(
                    current_cut_number
                    ).get('title')

        return {self.file_path.name: self.tree}


def replace_cut(find_cut, replace_cut, input_dir):
    print(
        [
            XML_Replace(each_file).replace(find_cut, replace_cut)
            for each_file in input_dir.iterdir()
        ]
    )
    # file_name_tree_dict = {}
    # for each_file in input_dir.iterdir():
    #     parser = XML_Replace(each_file)
    #     parser.replace(find_cut, replace_cut)
    #     file_name_tree_dict.update()
    # return file_name_tree_dict

