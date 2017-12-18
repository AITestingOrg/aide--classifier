from .directory_utils import DirectoryUtils
from .xml_parser import XmlParser
import re

class Loader:
    def __load_spaadia_xml(self, dir):
        data = []
        questions = 0
        files = DirectoryUtils.find_in_directory(dir, '.xml')
        for file in files:
            root = XmlParser.parse(files[file])
            for child in root:
                for frag in child:
                    label = 1 if frag.attrib['sp-act'] == 'reqInfo' else 0
                    data.append((re.sub('<[^>]+>', 'a', frag.text).strip(), label))
                    if label == 1:
                        questions += 1

        print(str(questions) + ' found out of ' + str(len(data)))
        return data

    def load_spaadia(self, version = 'v02'):
        dir = './data/data-sets/spaadia_release_' + version
        return self.__load_spaadia_xml(dir)