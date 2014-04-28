#! /usr/local/bin/python
import xml.etree.ElementTree as ET
def main():
    tree = ET.parse('bsb00009126.xml')
    root = tree.getroot()
    for child in root:
        print child.tag, child.attrib
    header = root[0]
    for child in header:
        print child.tag, child.attrib
    for foo in root.iter('lg'):
        print foo.tag, foo.attrib, foo.text
    xml.etree.ElementTree.dump(header)
if __name__ == '__main__':
    main()
