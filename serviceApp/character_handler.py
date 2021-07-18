import re


class CharacterHandler:
    """
    This is class handler the characters from the input resource
    """

    @staticmethod
    # Count of letter 'c' into sentence
    def count_letter(data_list, letter):
        dict_letters = {}
        list_characters = []

        for line_list in data_list:
            list_characters.extend(re.findall(r'\w', line_list))

        for unit in list_characters:
            if unit in dict_letters:
                dict_letters[unit] += 1
            else:
                dict_letters[unit] = 1
        return dict_letters[letter]

    @staticmethod
    # Get the most unpopular character
    def unpopular_character(data_list):
        dict_characters = {}
        dict_unpopular_character = {}
        list_characters = []

        for line_list in data_list:
            list_characters.extend(re.findall(r'\w', line_list))

        for unit in list_characters:
            if unit in dict_characters:
                dict_characters[unit] += 1
            else:
                dict_characters[unit] = 1

        for unit in dict_characters:
            if dict_characters[unit] == dict_characters[min(dict_characters, key=dict_characters.get)]:
                dict_unpopular_character[unit] = dict_characters[min(dict_characters, key=dict_characters.get)]
        return dict_unpopular_character

    @staticmethod
    # Longest sentence by number of letters
    def longest_sentence_by_letters(data_list):
        dict_letters = {}
        dict_result = {}

        for line in data_list:
            line_list = re.findall(r'\w', line)
            dict_letters[line] = len(line_list)

        for unit in dict_letters:
            if dict_letters[unit] == dict_letters[max(dict_letters, key=dict_letters.get)]:
                dict_result[unit] = dict_letters[max(dict_letters, key=dict_letters.get)]
        return dict_result
