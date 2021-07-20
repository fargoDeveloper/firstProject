"""
This is class extract special characters from input data
"""


class DataExtractor:

    def __init__(self, list_from_resource):
        self.list_from_resource = list_from_resource

    def extract_special_char(self):
        data_list = []
        for line in self.list_from_resource:
            line = line.replace("\n", ",")
            line = line.replace("#", "")
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("--", "")
            line = line.replace("!", "")
            line = line.lstrip()
            data_list.append(line)
        return data_list
