import sys
from enum import Enum


def main(args):
    file_path = args[0] if args else "input.txt"
    try:
        # Count valid passphrases using two different validation functions
        total_passphrases_general = count_valid_passphrases(file_path, ValidationType.GENERAL)
        total_passphrases_python = count_valid_passphrases(file_path, ValidationType.PYTHON)

        # Print the results for each validation function
        print(f"{ValidationType.GENERAL.name}")
        print(f"Correct passphrases in total:  {total_passphrases_general}")
        print(f"\n{ValidationType.PYTHON.name}")
        print(f"Correct passphrases in total:  {total_passphrases_python}\n")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as ex:
        print(f"An IO error occurred: {ex}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        print("Passphrases checking finished.")


def count_valid_passphrases(file_path: str, validation_type: Enum) -> int:
    """
    Counts the number of valid passphrases in the file based on the specified validation type.

    :param file_path: str - Input file location.
    :param validation_type: str - The type of validation to apply ('General' or 'Python').
    :return: int - Sum of valid passphrases.
    """
    passphrases_counter = 0
    lines = read_file_lines(file_path)
    for line in lines:
        if line.strip() and is_valid_passphrase(line.strip(), validation_type):
            passphrases_counter += 1
    return passphrases_counter


def read_file_lines(file_path: str) -> list:
    """
    Reads lines from a file.

    :param file_path: str - Path to the file to be read.
    :return: list - A list of lines from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise
    except IOError as ex:
        print(f"An IO error occurred: {ex}")
        raise


# region Methods based on validation type
def is_valid_passphrase(line: str, validation_type: Enum) -> bool:
    """
    Checks if a single line is a valid passphrase based on the specified validation type.

    :param line: str - The line to validate as a passphrase.
    :param validation_type: str - The type of validation to apply ('General' or 'Python').
    :return: bool - True if valid, False otherwise.
    """
    words = line[:-1].split()
    # Check if the last character is valid, there is more than one word,
    # all characters are valid, and there are no duplicate occurrences
    return (is_last_char_valid(line, validation_type) and
            len(words) > 1 and
            is_all_valid(line, validation_type) and
            check_occurrences(words, validation_type))


def is_last_char_valid(line: str, validation_type: Enum) -> bool:
    """
    Determines if the last character of a given line is valid based on the specified validation type.

    :param line: str - The line to be checked.
    :param validation_type: str - The validation type ('General' or 'Python').
    :return: bool - True if the last character is valid, False otherwise.
    """
    return is_last_char_valid_general(line) if validation_type == ValidationType.GENERAL \
        else is_last_char_valid_python(line)


def is_all_valid(line: str, validation_type: Enum) -> bool:
    """
    Determines if all characters are valid based on the validation type.

    :param line: str - The line to be checked.
    :param validation_type: str - The validation type ('General' or 'Python').
    :return: bool - True if all characters are valid, False otherwise.
    """
    return is_all_valid_general(line) if validation_type == ValidationType.GENERAL \
        else is_all_valid_python(line)


def check_occurrences(words: [str], validation_type: Enum) -> bool:
    """
    Checks if there are any duplicate words in the given array based on the specified validation type.

    :param words: list - The array of words to be checked.
    :param validation_type: str - The validation type ('General' or 'Python').
    :return: bool - True if no duplicates, False otherwise.
    """
    return check_occurrences_general(words) if validation_type == ValidationType.GENERAL \
        else check_occurrences_python(words)


# endregion

# region Python specific functions
def is_last_char_valid_python(line):
    """
    Checks if the last character of a line is one of the specified valid punctuation marks.
    The function determines if the last character matches the valid characters.
    Time Complexity: O(1)
    Space Complexity: O(1)

    :param line: str - The line to be checked.
    :return: bool - True if the last character is a valid punctuation mark. Otherwise, false.
    """
    return line[-1] in ['!', '?', '.']


def is_all_valid_python(line):
    """
    Checks if all characters in a line, except the last, are lowercase letters or whitespace.
    This function ensures that the line, up to the second-to-last character, adheres to the criteria.
    Time Complexity: O(n)
    Space Complexity: O(n)

    :param line: str - The line to be validated.
    :return: bool - True if all characters, excluding the last punctuation mark, are lowercase or whitespace.
    Otherwise, false.
    """
    # Using a comprehension to check each character, excluding the last punctuation mark.
    return all(ch.islower() or ch.isspace() for ch in line[:-1])


def check_occurrences_python(words):
    """
    Determines if all words in a given array are unique.
    This function uses set and len to check if any word appears more than once.
    Time Complexity: O(n)
    Space Complexity: O(n)

    :param words: list - The array of words to be checked.
    :return: bool - True if there are no duplicate words in the array. Otherwise, false.
    """
    return len(words) == len(set(words))


# endregion

# region General functions
def is_last_char_valid_general(line: str) -> bool:
    """
    Checks if the last character of a line is a valid punctuation mark.
    This method uses a loop to check if the last character matches any of the valid characters.
    Time Complexity: O(1)
    Space Complexity: O(1)

    :param line: str - The line to be checked.
    :return: bool - True if the last character is a valid punctuation mark. Otherwise, false.
    """
    last_char = line[-1]
    valid_chars = ['!', '?', '.']
    index = 0
    while index < len(valid_chars):
        if last_char == valid_chars[index]:
            return True
        index += 1
    return False


def is_all_valid_general(line: str) -> bool:
    """
    Checks if all characters in a line, except the last character, are lowercase letters or whitespace.
    This function ensures that the line, up to the second-to-last character, adheres to the criteria.
    Time Complexity: O(n)
    Space Complexity: O(1)

    :param line: str - The line to be validated.
    :return: bool - True if all characters, excluding the last punctuation mark, are lowercase or whitespace.
    Otherwise, False.
    """
    index = 0
    # The '-2' in the loop condition is because:
    #    - The last character of the line is a punctuation mark, which is not being checked here.
    #    - Python uses zero-based indexing, so 'len(line) - 1' is the last character,
    #    and 'len(line) - 2' is the second-to-last character.
    # This ensures the loop checks all characters up to (but not including) the final punctuation mark.
    while index < len(line) - 2:
        char = line[index]
        if char.isspace() or char.islower():
            index += 1
        else:
            return False
    return True


def check_occurrences_general(words: [str]) -> bool:
    """
    Determines if all words in a given array are unique.
    This function compares each word against every other word in the array to check for duplicates.
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    :param words: list - The array of words to be checked.
    :return: bool - True if there are no duplicate words in the array. Otherwise, false.
    """
    for i in range(len(words) - 1):
        for k in range(i + 1, len(words)):
            if words[i] == words[k]:
                return False
    return True


# endregion

# Enumeration to distinguish between General and Python validation types
class ValidationType(Enum):
    GENERAL = 1
    PYTHON = 2


if __name__ == "__main__":
    main(sys.argv[1:])
