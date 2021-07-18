class TextDataProcessor:

    @staticmethod
    def load_from_resource(file):
        list_from_resource = []
        for line in file:
            line = line.replace("\n", ",")
            line = line.replace("#", "")
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("--", "")
            line = line.replace("!", "")
            line = line.lstrip()
            list_from_resource.append(line)
        return list_from_resource
