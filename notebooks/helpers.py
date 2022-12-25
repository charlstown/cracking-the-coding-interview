# Libraries
import random as rnd
import time
import string


# Help functions
def rnd_string(length):
    """
    Generates a random string
    :param length:
    :return:
    """
    ascii_letters = string.ascii_letters
    out = ''
    for i in range(length):
        rnd_letter = ascii_letters[rnd.randint(0, len(ascii_letters)-1)]
        out += rnd_letter
    return out


def rnd_matrix(size: int=3, y_columns: int=None, seed: int=0):
    """
    Generates random matrix with the selected size m x m
    :param size: matrix size
    :return: matrix with the selected size
    """
    rnd.seed(seed)
    if y_columns == None:
        y_columns = size
    return [[rnd.randint(0, 9) for column in range(size)] for row in range(y_columns)]


def print_matrix(matrix):
    """
    Prints a matrix in the console
    :param matrix: matrix to be printed
    :return: None
    """
    n_borders = 7*len(matrix)
    print('-'*5)
    for i in matrix:
        line = str(i)[1:-1].replace(',', '\t')
        print(line)
    print('-'*5)


def test_function(*inputs, func, show=False, matrix=False):
    """
    Test the same function with multiple inputs
    :param inputs:
    :param func:
    :param show:
    :return:
    """
    for i, input in enumerate(inputs):
        if show:
            if not matrix:
                print(f"    {input}")
            else:
                print_matrix(input[0])
        else:
            pass
        output = func(*input)
        if not matrix:
            print(f"- Test {i}: {output}")
        else:
            print_matrix(output)


def compare_functions(*func, inpt):
    """
    Compare two functions given the same input and returns metrics based on the performance
    :param func:
    :param inpt:
    :return:
    """
    summary = dict()
    for f in func:
        # Run function
        start = time.time()
        f(*inpt)
        end = time.time()

        # Calculate summary
        total = end -start
        summary[f.__name__] = total

        # Get best function
    best_f = min(summary, key=summary.get)
    difference = round(sorted(summary.values())[1] - summary[best_f], 2)
    print(f"The fastest function is {best_f} it took {difference} seconds less than the second best.\n")
    for k, v in summary.items():
        print(f"{k}: {v}")