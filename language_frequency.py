import string
import sys
from collections import Counter


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        exit('Try again with right format "$ python language_frequency.py <path to file>"')

    file_data = load_file_data(file_path=path)
    if file_data is None:
        exit('File was not found')

    word_frequency_list = get_number_of_most_frequent_words(text=file_data,
                                                            number_of_entries=10)
    print_word_frequency_list(word_frequency_list)


def print_word_frequency_list(word_frequency_list: list):
    print('List of the most frequently used words:')
    for row_number, (word, counter) in enumerate(word_frequency_list, start=1):
        output_string_draft = '{}: Word - {}, frequency - {}'
        print(output_string_draft.format(row_number, word, counter))


def get_number_of_most_frequent_words(text: str,
                                      number_of_entries: int = 10):
    list_of_words = get_word_list_from_string(text)
    word_counter = Counter(list_of_words)
    word_counter_order_by_frequency = word_counter.most_common(number_of_entries)

    return word_counter_order_by_frequency


def get_word_list_from_string(current_string: str):
    current_string_lower = current_string.lower()
    string_with_no_punctuation = remove_punctuation_from_string(current_string_lower)
    list_of_words = string_with_no_punctuation.split()

    return list_of_words


def remove_punctuation_from_string(current_string: str):
    string_with_no_punctuation = ''
    for symbol in current_string:
        if symbol not in string.punctuation + '–':
            string_with_no_punctuation += symbol
        else:
            string_with_no_punctuation += ' '

    return string_with_no_punctuation


def load_file_data(file_path: str):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None


if __name__ == '__main__':
    main()
