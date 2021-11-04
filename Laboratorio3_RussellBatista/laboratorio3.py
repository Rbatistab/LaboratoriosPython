#!/usr/bin/python3

import sys
import time
import enum

# -------------- Enum for cases: -------------------------------------------


class UserCase(enum.Enum):
    """
    Enum for cases to evaluate user arguments in executor of program
    """
    just_number = 1
    number_and_time = 2
    number_and_complete = 3
    number_time_and_complete = 4


# -------------- Program Exceptions: ----------------------------------------
class InvalidUserArguments(Exception):
    """
    Exception for not suficient user arguments
    """

    def __init__(self):
        usage_message = "usage: laboratorio3.py [-h] [--tiempo] [--completa]"\
                        " posicion"
        error_info = "laboratorio3.py: error: the following arguments are "\
            "required: pocision"
        print(usage_message + "\n" + error_info)


# -------------- Program validators: ----------------------------------------
def validate(user_arguments):
    """
    Validates that the user put at least 1 argument
    """
    if 0 == len(user_arguments):
        raise InvalidUserArguments


# -------------- Time controller: ------------------------------------------
def get_initial_time():
    """
    Gets the current time from epoch
    """
    return time.time()


def get_total_time(initial_time):
    """
    Gets the total elapsed time since inintial time
    """
    total_time = time.time() - initial_time
    return total_time


def print_total_execution_time(initial_time):
    """
    Prints total execution time since the initial time in get_initial_time()
    """
    total_time = get_total_time(initial_time)
    print("Tiempo total de ejecucion: {}s".format(total_time))

# -------------- Program utils: --------------------------------------------


def calculate_fibonacci(N):
    """
    Calculates recursively a fibonacci number and stores the track of the
    numbers into list fibonacci_list
    """
    if 0 == N:  # base case
        fibonacci_number = 0
    elif 1 == N:
        calculate_fibonacci(0)
        fibonacci_number = 1
    else:
        fibonacci_number = calculate_fibonacci(
            N - 1) + calculate_fibonacci(N - 2)
    return fibonacci_number


def add_next_non_recursive_fibonacci(fibonacci_list):
    """
    Given a list of M fibonacci numbers, it adds the M + 1 number to the list
    """
    next_number = fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list.append(next_number)


def create_fibonacci_list(N, fibonacci_list):
    """
    Creates a list of fibonacci numbers up to index N (non-recursively)
    """
    if (0 == N):
        fibonacci_list[:] = [1]
    else:
        fibonacci_list[:] = [1, 1]
        for n in range(2, N):
            add_next_non_recursive_fibonacci(fibonacci_list)


def print_fibonacci_list(N, fibonacci_list):
    """
    Prints the fibonacci list
    """
    print(
        "La serie Fibonacci hasta indice {} es:".format(
            N))
    for number in (fibonacci_list):
        print(number)


def print_fibonacci_for_index_N(N, fibonacci_for_index_N):
    """
    Prints the fibonacci final number for and index N
    """
    print(
        "El numero de Fibonacci del indice {} es: {}".format(
            N, fibonacci_for_index_N))


def set_case(user_arguments):
    """
    Returns the user case based on the arguments
    """
    time_wanted = ('-t' in user_arguments) or ('-tiempo' in user_arguments)
    complete_wanted = (
        '-c' in user_arguments) or ('-completa' in user_arguments)
    time_and_complete_wanted = time_wanted and complete_wanted
    if time_and_complete_wanted:
        return UserCase.number_time_and_complete
    if time_wanted:
        return UserCase.number_and_time
    if complete_wanted:
        return UserCase.number_and_complete
    return UserCase.just_number


# -------------- Program controllers: ----------------------------------------
def exec(user_arguments, initial_time):
    fibonacci_list = []
    N = int(user_arguments.pop(0))
    fibonacci_number_for_N = calculate_fibonacci(N)
    user_case = set_case(user_arguments)
    if user_case == UserCase.just_number:
        print_fibonacci_for_index_N(N, fibonacci_number_for_N)
    if user_case == UserCase.number_and_time:
        print_fibonacci_for_index_N(N, fibonacci_number_for_N)
        print_total_execution_time(initial_time)
    if user_case == UserCase.number_and_complete:
        create_fibonacci_list(N, fibonacci_list)
        print_fibonacci_list(N, fibonacci_list)
    if user_case == UserCase.number_time_and_complete:
        create_fibonacci_list(N, fibonacci_list)
        print_fibonacci_list(N, fibonacci_list)
        print_total_execution_time(initial_time)


def main():
    initial_time = get_initial_time()
    user_arguments = sys.argv[1:]
    try:
        validate(user_arguments)
        exec(user_arguments, initial_time)
    except InvalidUserArguments:
        pass


if __name__ == "__main__":
    print("Laboratorio 3 IE-0117 - Russell Batista")
    main()
