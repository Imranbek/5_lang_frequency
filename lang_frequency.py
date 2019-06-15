import string
import sys
from collections import Counter


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        exit('Try again with right format "$ python lang_frequency.py <path to file>"')

    file_data = load_file_data(file_path=path)
    if file_data is None:
        exit('File was not found')

    word_frequency_list = get_number_ot_most_frequent_words(text=file_data,
                                                            number_of_entries=10)
    print_word_frequency_list(word_frequency_list)


def print_word_frequency_list(word_frequency_list: list):
    print('List of the most frequency words:')
    row_number = 0
    for item in word_frequency_list:
        row_number += 1
        output_string = f'{row_number}: Word - {item[0]}, frequency - {item[1]}'
        print(output_string)


def get_number_ot_most_frequent_words(text: str,
                                      number_of_entries: int = 10):
    list_of_words = get_word_list_from_string(text)
    word_frequency_counter = Counter(list_of_words).most_common(number_of_entries)

    return word_frequency_counter


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
