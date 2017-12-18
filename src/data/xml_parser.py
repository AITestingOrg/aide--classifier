import xml.etree.ElementTree

class XmlParser:
    @staticmethod
    def parse(file):
        return xml.etree.ElementTree.parse(file).getroot()