"""
This is module load data from the input resource
"""


class ResourceLoader:

    def __init__(self, name_file: str):
        self.name_file = name_file

    def load_from_file(self):
        list_from_resource = []
        try:
            file = open(self.name_file, "rt")
            for line in file:
                if len(line) != 0:
                    list_from_resource.append(line)
            file.close()
            return list_from_resource
        except OSError:
            print("     ----------     ")
            print("--- FileNotFound ---")
            print("     ----------     ")
