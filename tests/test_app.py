import unittest
from app import \
        index, \
        delete, \
        update, \
        divit


def test_index():
    pass


def test_delete():
    pass


def test_update():
    pass


def test_divit():

    numerators = [-5, -2, 0]
    denominators = [-5, -1, 0]
    ground_truth = [1, 5, None, 0.4, 2, None, 0, 0, None]

    ind = 0
    for num in numerators:
        for denom in denominators:
            print(num, denom)
            assert divit(num, denom) == ground_truth[ind]
            ind += 1
