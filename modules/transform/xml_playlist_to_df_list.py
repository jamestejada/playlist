from pathlib import Path
import xml.etree.ElementTree as ET

class XML_Playlist_Transform:
    """ Transforms XML playlist for writing to excel.
    These excel files can then be edited and used to create
    text files to be imported as playlists in ENCO DAD.
    """
    # defaults
    FIND_LIST = ['encoPlaylistDatabase', 'encoPlaylistRecord']
    ATTR_LIST = [
        'cut', 'comment', 'type', 'function', 'time', 'begend', 'chain'
        ]

    def __init__(self, file_path, find_list=None, attr_list=None):
        self.file_path = file_path
        self.root = self.get_xml_root()
        self.find_list = find_list or self.FIND_LIST
        self.attr_list = attr_list or self.ATTR_LIST
        self.xml_record_list = self.get_records()
        self.dataframe_dict = self.build_dict()

    def output(self):
        return self.dataframe_dict

    def get_xml_root(self):
        """parses file and returns xml root"""
        tree = ET.parse(self.file_path)
        return tree.getroot()

    def get_records(self):
        """parses elements to get to list of enco records or (cuts)"""
        db = self.root.find(self.find_list[0])
        return db.findall(self.find_list[1])
    
    def build_dict(self):
        dataframe_dict = {attr: [] for attr in self.attr_list}

        for record in self.xml_record_list:
            for attribute in self.attr_list:
                one_attr_list = dataframe_dict.get(attribute)
                one_attr_list.append(self._find_attr(attribute, record))
        
        return dataframe_dict

    def _find_attr(self, attribute, record):
        return record.find(attribute).text or ''
    
    def __str__(self):
        return str(self.dataframe_dict)