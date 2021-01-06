from modules.settings import FIND_REPLACE_PATH, OUTPUT_DIRECTORY
from modules.transform.xml_playlist_to_df_list import XML_Playlist_Transform
import xml.etree.ElementTree as ET
import json


class XML_Replace(XML_Playlist_Transform):

    OUTPUT_DIR = OUTPUT_DIRECTORY

    # override
    def build_dict(self):
        return None
    
    # override
    def __str__(self):
        return ET.tostring(self.tree)
    
    def replace(self, find_cut, replace_cut):
        for record in self.xml_record_list:
            current_cut_number = record.find('cut').text
            if current_cut_number == find_cut:
                current_cut_number = replace_cut
                if self.cut_titles:
                    record.find('comment').text = self.cut_titles.get(
                        current_cut_number
                        ).get('title')

        return {self.file_path.name: self.tree}


