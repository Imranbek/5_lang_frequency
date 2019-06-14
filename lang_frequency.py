import string
import sys


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        exit('Try again with right format "$ python pprint_json.py <path to file>"')

    file_data = load_file_data(file_path=path)
    if file_data is None:
        exit('File was not found')

    word_frequency_list = get_most_frequent_words_list(file_data)
    print_first_rows(word_frequency_list)


def print_first_rows(word_frequency_list: list,
                     number_of_rows: int = 10):
    output_rows_number = min(number_of_rows, len(word_frequency_list))
    print('List of the most frequency words:')
    for i in range(output_rows_number):
        output_string = '{}: Word - {}, frequency - {}'.format(i + 1, word_frequency_list[i][0], word_frequency_list[i][1])
        print(output_string)


def get_most_frequent_words_list(text: str):
    list_of_words = get_word_list_from_string(text)
    word_frequency_dict = {}

    for word in list_of_words:
        if word in word_frequency_dict:
            word_frequency_dict[word] = word_frequency_dict[word] + 1
        else:
            word_frequency_dict.update({word: 1})

    word_frequency_list_sorted = sorted(word_frequency_dict.items(),
                                        key=lambda x: x[1],
                                        reverse=True)
    return word_frequency_list_sorted


def get_word_list_from_string(current_string: str):
    string_with_no_punctuation = remove_punctuation_from_string(current_string.lower())
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
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None


if __name__ == '__main__':
    main()
