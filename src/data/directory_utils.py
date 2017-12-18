import os

class DirectoryUtils:
    @staticmethod
    def find_in_directory(dir, extension = None):
        files = {}
        for file in os.listdir(dir):
            if extension == None or file.endswith(extension):
                files[file] = os.path.join(dir, file)

        return files