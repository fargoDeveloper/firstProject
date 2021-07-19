class ResourceLoader:
    """
    This is class load data from the input resource
    """

    @staticmethod
    def load_from_file(name_file):
        list_from_resource = []
        try:
            file = open(name_file, "rt")

            for line in file:
                if len(line) != 0:
                    list_from_resource.append(line)
            file.close()
            return list_from_resource
        except OSError:
            print("     ----------     ")
            print("--- FileNotFound ---")
            print("     ----------     ")
