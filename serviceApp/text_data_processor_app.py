from resource_loader import ResourceLoader as rl
from data_extractor import DataExtractor as de
from character_handler import CharacterHandler as ch
from words_handler import WordsHandler as wh


class TextDataProcessorApp:
    """
    This class launches the application for execution.
    """

    @staticmethod
    def run_app():
        name_file = "file.txt"
        letter = "c"
        data_list = de.extract_special_char(rl.load_from_file(name_file))

        # Count of letter 'c' into sentence
        print()
        print("№1. Count of letter", "\'", letter, "\'", "into sentence: ", ch.count_letter(data_list, letter), "pc.")
        print("--------------------------------------------------")

        # Get the most unpopular character
        print()
        print("№2. Most unpopular character is ", ch.unpopular_character(data_list), ".")
        print("--------------------------------------------------")

        # Longest sentence by number of letters
        print()
        print("№3. Longest sentence by number of letters: ", ch.longest_sentence_by_letters(data_list))
        print("--------------------------------------------------")

        # Longest sentence by word count
        print()
        print("№4. Longest sentence by word count: ", wh.longest_sentence_by_words(data_list))
        print("--------------------------------------------------")

        # Count of duplicate word into text
        print()
        print("№5. Count of duplicate word into text: ", wh.count_duplicate_word(data_list))
        print("--------------------------------------------------")

        print()
        return "***** Data processing is over *****"


tdpa = TextDataProcessorApp()
print(tdpa.run_app())
