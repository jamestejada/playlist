from modules.settings import OUTPUT_DIRECTORY


def to_xml(xml_tree_dict_list: list):
    full_dict = merge_dicts(xml_tree_dict_list)

    for output_file_name, xml_tree in full_dict.items():
        output_file = OUTPUT_DIRECTORY.joinpath(f'{output_file_name}.xml')
        xml_tree.write(output_file)

def merge_dicts(dict_list):
    output_dict = {}
    for dictionary in dict_list:
        output_dict.update(dictionary)
    return output_dict