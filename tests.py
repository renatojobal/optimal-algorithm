import main
from utils import *


class Test:
    """
    Test class
    """

    def __init__(self, pages_list, frames_number, expected_matrix=None):
        """
        Constructor
        :param pages_list:
        :param frames_number:
        """
        self.pages_list = pages_list.split()
        self.frames_number = frames_number
        self.expected_matrix = expected_matrix
        self.result_matrix = [[]]

    def run(self):
        self.result_matrix = main.apply_optimal_algorithm(self.pages_list, self.frames_number)

        print("Test finished")
        print("Result: ")
        print(self.pages_list)
        print_format_matrix(self.result_matrix)
        print("\n")
        if self.expected_matrix:
            print("Expected Matrix")
            print_format_matrix(self.expected_matrix)


def test():
    """
    Create tests and run them
    :return: None
    """

    test1 = Test(pages_list="7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7", frames_number=3)


    expected_matrix2 = [
        [["7"], ["7"], ["7"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["2"], ["7"], ["7"], ["7"]],
        [["E"], ["0"], ["0"], ["0"], ["0"], ["0"], ["0"], ["4"], ["4"], ["0"], ["0"], ["0"], ["0"], ["0"], ["0"], ["0"], ["0"], ["0"], ["0"], ["0"]],
        [["E"], ["E"], ["1"], ["1"], ["1"], ["3"], ["3"], ["3"], ["3"], ["3"], ["3"], ["3"], ["1"], ["1"], ["1"], ["1"], ["1"], ["1"], ["1"], ["1"]]
    ]

    test2 = Test(pages_list="7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1", frames_number=3, expected_matrix=expected_matrix2)
    test2.run()

test()
