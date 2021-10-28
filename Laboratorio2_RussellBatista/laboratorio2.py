#!/usr/local/bin/python3

import sys
# This is an exception to avoid finish the execution loop from child functions


class LoopReady(Exception):
    pass
# This is an exception to avoid finish the processing of a name if a digit
# is found


class DigitsFound(Exception):
    pass


# -------------- Program utils: ----------------------------------------
def get_name():
    """
    Gets the input name from the user
    """
    name = input("Escriba un nombre, o SALIR para salir: ")
    return name


def process_name(words):
    """
    Process a name word by word to validate and returns a valid
    final name(string)
    """
    output_name_array = []
    for word in words:
        check_word_for_digits(word)
        corrected_word = correct_word(word)
        output_name_array.append(corrected_word)
    return ' '.join(output_name_array)


def correct_word(word):
    """
    Puts a word into first capital letter and the rest to lower
    """
    return word[0].upper() + word[1:].lower()


def print_names(names):
    """
    Pretty prints an array of names to the user
    """
    for name in names:
        print(name)


# -------------- Program validators: ----------------------------------------
def is_name_valid_length(words):
    """
    Validates the quantity of words to 3 or 4
    """
    word_count = len(words)
    is_valid = False
    # For python 3.10 (CDM)
    # match word_count:
    #   case 1:
    #     if "SALIR" == words[0]: terminate_loop()
    #   case [3,4]:
    #     is_valid = True

    # For python lower than 3.10:
    if 1 == word_count:
        if "SALIR" == words[0]:
            terminate_loop()
    elif 3 == word_count or 4 == word_count:
        is_valid = True
    return is_valid


def check_word_for_digits(word):
    """
    Validates that words have no digits
    """
    for letter in word:
        if letter.isdigit():
            raise DigitsFound


# -------------- Program terminators: ----------------------------------------
def terminate_loop():
    """
    Finishes a loop by an exeption
    """
    raise LoopReady


def terminate_program():
    """
    Finishes the program by an exception
    """
    print("Finalizando ejecucion")
    sys.exit()


# -------------- Program controllers: ----------------------------------------
def exec(output_names):
    """
    Executes the main loop by controlling a single execution and updating and
    output_name array with the new name if valid.
    Logic:
    It calls out to the logic to get the name, split it into an array, validate
    the word count in the name, process the name to correct the words form and
    appends the corrected name to the ouput name
    """
    name = get_name()
    name_words = name.split()
    if is_name_valid_length(name_words):
        try:
            corrected_name = process_name(name_words)
            output_names.append(corrected_name)
        except DigitsFound:
            print("ERROR: hay digitos en el nombre")
    else:
        print("ERROR: debe digitar nombres de 3 o 4 componentes")


def main():
    """
    Controls the main execution
    """
    output_names = []
    try:
        while(True):
            exec(output_names)
    except LoopReady:
        pass
    print_names(output_names)


if __name__ == "__main__":
    print("Laboratorio 2 IE-0117 - Russell Batista")
    main()
