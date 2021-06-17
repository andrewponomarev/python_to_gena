import csv
import xml.etree.ElementTree as ET


def get_numbers_from_csv(csv_file_name):
    with open(csv_file_name, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        return [int(row[0]) for row in reader]


def change_numbers_in_xml(xml_file_name, numbers_list, xml_path):
    tree = ET.parse(xml_file_name)
    root = tree.getroot()
    element = root.find(xml_path)
    for num in numbers_list:
        num_element = ET.SubElement(element, f'num id = \"{num}\"')
    tree.write(xml_file_name)


CSV_FILE_NAME = "nums.csv"
XML_FILE_NAME = "nums.xml"

## путь до списка с числами не считая корневого элемента
XMl_PATH_TO_NUMBER_LIST_ELEMENT = "nums"


if __name__ == '__main__':
    number_list = get_numbers_from_csv(CSV_FILE_NAME)
    change_numbers_in_xml(XML_FILE_NAME, number_list, XMl_PATH_TO_NUMBER_LIST_ELEMENT)
