import string
from random import randint, choice

import ResultsWriter
from sort_tree_with_iterator import treesort_with_iterations

def get_token(length=15, only_digits=False):
    rand_str = lambda n: ''.join([choice(string.ascii_lowercase) for i in range(n)])
    if only_digits:
        rand_str = lambda n: ''.join([choice(string.digits) for i in range(n)])
    set_id = rand_str(length)
    return set_id

def generate_array(size=1):
    arr = []
    for i in range(0, size):
        arr.append(get_token())
    return arr


def main():
    limit = 150
    repeat = 1
    for i in range(0, limit + 1):
        for j in range(0, repeat):
            array = generate_array(i)
            arr, iterations = treesort_with_iterations(array)
            ResultsWriter.print(i, iterations)


main()
