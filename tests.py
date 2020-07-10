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
        print_format_matrix(self.result_matrix)
        print("\n")


def test():
    """
    Create tests and run them
    :return: None
    """

    test1 = Test(pages_list="a b c d e f g h i j ", frames_number=4)
    test1.run()


test()
