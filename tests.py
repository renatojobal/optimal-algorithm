import main


def print_inline_list(target_list):
    for item in target_list:
        print(item, end=' ')


def print_format_matrix(matrix):
    for row in matrix:
        print_inline_list(row)
    print("\n")


class Test:

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


def test():
    """
    Create tests and run them
    :return: None
    """

    test1 = Test(pages_list="a b c d e f g h i j ", frames_number=4)
    test1.run()


test()