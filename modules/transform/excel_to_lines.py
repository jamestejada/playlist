import pandas as pd



class Excel_Playlist_Transform:
    """Builds a list of dictionaries in the order of execution
    for ENCO DAD software. Each dictionary refers to one
    cut of a playlist. This list of dictionaries is meant to
    be passed to an output module where it will be formatted
    and written into a text file.
    """
    ESSENTIAL_ATTR_LIST = [
        'cut', 'type', 'function', 'time', 'begend', 'chain'
        ]

    def __init__(self, dataframe_dict=None, excel_path=None):
        # At least one parameter is required.
        if all(x is None for x in [dataframe_dict, excel_path]):
            raise Exception(
            """Either a dataframe dictionary or a path to a playlist
            Excel file is required"""
            )
        self.file_path = excel_path
        self.dataframe_list = dataframe_dict or self.get_dataframe_list()

    def get_dataframe_list(self):
        if self.file_path:
            df = pd.read_excel(self.file_path)
            no_nan_df = self._clean_nan(df)
            dict_list = no_nan_df.to_dict(orient='records')
            return self._clean_excel_dict_list(dict_list)
        # else:
        #   deal with condition where dataframe dict is passed
        #   into class.

    def _clean_nan(self, df):
        return df.where(df.notnull(), None)

    def _clean_excel_dict_list(self, dict_list):
        """Cleans dataframe from an excel file
        """
        for cut_dict in dict_list:
            self.essential_attr_check(cut_dict)
            cut_dict.update(self._check_floats(cut_dict))
        return dict_list

    def _check_floats(self, cut_dict):
        return {
            int_attribute: self._float_to_int(cut_dict, int_attribute)
            for int_attribute in ['begend', 'chain']    
            }
    
    def _float_to_int(self, cut_dict, int_attr):
        original_value = cut_dict.get(int_attr)
        return (
            int(original_value)
            if type(original_value) is float
            else original_value
            )

    def essential_attr_check(self, cut_dict, _attr_list=None):
        attr_list = _attr_list or self.ESSENTIAL_ATTR_LIST
        for attribute in attr_list:
            try:
                assert attribute in cut_dict.keys()
            except AssertionError:
                raise KeyError(
                f"""Input dictionary or file does not have all essential columns\n
                {', '.join(self.ESSENTIAL_ATTR_LIST)}
                """
            )

    def _clean_param_df_dict(self, df_dict):
        """cleans dataframe dictionaries passed to class directly.
        """

    def __str__(self):
        return str(self.dataframe_list)
    
    def output(self):
        """A generator that yields cut dictionaries for each line
        of the playlist
        """
        for line_dict in self.dataframe_list:
            yield line_dict


"""
SAMPLE OUTPUT:

[
    {
        'cut': '99988', 
        'comment': ':10 sec countdown', 'type': 'P', 'function': 'L', 'time': None, 'begend': None, 'chain': None},
    {
        'cut': '98571', 
        'comment': 'Place-holder', 'type': 'P', 'function': 'N', 'time': None, 'begend': None, 'chain': None
    },
    {
        'cut': 'HARD', 
        'comment': None, 'type': 'T', 'function': 'A', 'time': '23:59:00', 'begend': 2, 'chain': 0
    },
    ...
    
"""