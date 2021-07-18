import re

from text_data_processor import TextDataProcessor


def run_app():
    file = open("testFile.txt", 'rt')
    list_from_resource = TextDataProcessor.load_from_resource(file)
    file.close()

    new_list = []
    for line in list_from_resource:
        if len(line) != 0:
            new_list.append(line)

    #  самое длинное предложение (по количеству слов)
    print()

    dict_word1 = {}
    new_dict_word1 = {}

    for line in new_list:
        new_line1 = line.split(" ")
        dict_word1[line] = len(new_line1)

    for k in dict_word1:
        if dict_word1[k] == dict_word1[max(dict_word1, key=dict_word1.get)]:
            new_dict_word1[k] = dict_word1[max(dict_word1, key=dict_word1.get)]

    print("№4. Longest sentence by word count: ", new_dict_word1)
    print("--------------------------------------------------")

    #   самое длинное предложение (по количеству букв)
    print()

    dict_word2 = {}
    new_dict_word2 = {}

    for line in new_list:
        new_line2 = re.findall(r'\w', line)
        dict_word2[line] = len(new_line2)

    for k in dict_word2:
        if dict_word2[k] == dict_word2[max(dict_word2, key=dict_word2.get)]:
            new_dict_word2[k] = dict_word2[max(dict_word2, key=dict_word2.get)]

    print("№3. Longest sentence by number of letters: ", new_dict_word2)
    print("--------------------------------------------------")

    # Most unpopular character
    print()

    dict_word3 = {}
    new_dict3 = {}
    list_characters3 = []

    for line in new_list:
        list_characters3.extend(re.findall(r'\w', line))

    for unit in list_characters3:
        if unit in dict_word3:
            dict_word3[unit] += 1
        else:
            dict_word3[unit] = 1

    for k in dict_word3:
        if dict_word3[k] == dict_word3[min(dict_word3, key=dict_word3.get)]:
            new_dict3[k] = dict_word3[min(dict_word3, key=dict_word3.get)]

    print("№2. Most unpopular character is ", new_dict3, ".")
    print("--------------------------------------------------")

    # Count of letter 'c' into sentence
    print()

    dict_latter4 = {}
    list_characters4 = []

    for line in new_list:
        list_characters4.extend(re.findall(r'\w', line))

    for unit in list_characters4:
        if unit in dict_latter4:
            dict_latter4[unit] += 1
        else:
            dict_latter4[unit] = 1

    print("№1. Count of letter 'c' into sentence: ", dict_latter4["c"], "pc")
    print("--------------------------------------------------")

    # Count of duplicate word into text
    print()

    list_words = []
    dict_words = {}
    sorted_dict = {}

    for line in new_list:
        line = line.lower()
        new_line = line.split(" ")
        list_words.extend(new_line)

    for word in list_words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    # sorted dictionary words
    sorted_keys = sorted(dict_words, key=dict_words.get)

    for k in sorted_keys:
        sorted_dict[k] = dict_words[k]

    print("№5. Count of duplicate word into text: ", sorted_dict)
    print("--------------------------------------------------")
    pass


run_app()
