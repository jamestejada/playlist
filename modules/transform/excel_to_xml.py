from pathlib import Path
import xml.etree.ElementTree as ET

XML_ENCODING = 'ISO-8859-1'

test_input_file = Path.cwd().joinpath('input', 'xml_to_excel', 'CLA3-WED.xml')

# UNDER CONSTRUCTION
def get_xml_tree():
    xml = ET.parse(test_input_file)
    enco = xml.getroot()
    playlist = enco.find('encoPlaylistDatabase')
    records = playlist.findall('encoPlaylistRecord')
    for record in records:
        if record.find('cut').text == 'CHAIN':
            chain_to = record.find('chain')
            chain_to.text = 'CLA-1215'
    
    xml.write('sample_output.xml')

