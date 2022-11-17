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


def test_function(*inputs, func, show=False):
    """
    Test the same function with multiple inputs
    :param inputs:
    :param func:
    :param show:
    :return:
    """
    for i in range(len(inputs)):
        input = inputs[i]
        output = func(*input)
        print(f"- Test {i}: {output}")
        if show:
            print(f"    {input}")
        else:
            pass


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