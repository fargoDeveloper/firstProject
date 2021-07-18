class DataExtractor:
    """
    This is class extract special characters from input data
    """

    @staticmethod
    def extract_special_char(list_from_resource):
        data_list = []
        for line in list_from_resource:
            line = line.replace("\n", ",")
            line = line.replace("#", "")
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("--", "")
            line = line.replace("!", "")
            line = line.lstrip()
            data_list.append(line)
        return data_list
