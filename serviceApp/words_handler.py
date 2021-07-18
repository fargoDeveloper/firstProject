class WordsHandler:
    """
    This is class handler the words from the input resource
    """

    @staticmethod
    # Longest sentence by word count
    def longest_sentence_by_words(data_list):
        dict_words = {}
        dict_result = {}

        for line in data_list:
            line_list = line.split(" ")
            dict_words[line] = len(line_list)

        for unit in dict_words:
            if dict_words[unit] == dict_words[max(dict_words, key=dict_words.get)]:
                dict_result[unit] = dict_words[max(dict_words, key=dict_words.get)]
        return dict_result

    # Count of duplicate word into text
    @staticmethod
    def count_duplicate_word(data_list):
        list_words = []
        dict_words = {}
        sorted_dict = {}

        for line_list in data_list:
            line_list = line_list.lower()
            line_list = line_list.split(" ")
            list_words.extend(line_list)

        for word in list_words:
            if word in dict_words:
                dict_words[word] += 1
            else:
                dict_words[word] = 1

        # sort dictionary words
        sorted_keys = sorted(dict_words, key=dict_words.get)
        for k in sorted_keys:
            sorted_dict[k] = dict_words[k]
        return sorted_dict
