def read_input(filename):
    """Reads the input from a file and returns it as a list of strings."""
    with open(filename) as f:
        return f.read().splitlines()


def write_output(filename, data):
    """Writes the output to a file."""
    with open(filename, 'w') as f:
        f.write(data)


def split_input(input_str, delimiter=' '):
    """Splits the input string by the given delimiter and returns a list of parts."""
    return input_str.split(delimiter)


def sum_list(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)
