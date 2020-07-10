from settings import *
from utils import *


class Frame:
    """
    Class for hold the items of a list
    """

    def __init__(self, content=None):
        """
        Constructor that initialize the object
        :param content: if not content is passed, None is assigned and is set as a empty item
        """
        if content:
            self.content = content
            self.is_empty = False
        else:
            self.content = None
            self.is_empty = True

        # Other attributes


    def set_content(self, page):
        """
        Set a page as content
        :param page: target page
        :return: None
        """
        self.content = page
        self.is_empty = False

    def equals(self, other_frame):
        """
        It compare the content of two frames and return a request
        :param other_frame: Another instance of Frame class
        :return: True when the content is equal and False when they are not
        """
        return self.content == other_frame.get_content()

    def get_content(self):
        """
        Get the attribute content
        :return: self.content
        """
        return self.content

    def __str__(self) -> str:
        """
        Return the content in string representation
        :return:
        """
        return str(self.content)


def apply_optimal_algorithm(pages_list, frames_number):
    """
    Optimal algorithm

    This algorithm is base on the Optimal Algorithm for page replacement used
    in Operatem Systems.

    It use as parameters:
        pagesList: a python list that contains the pages names, could be a list o string
        framesNumber: the number of frames to place the pages
    """

    print("Algorithm started")
    print("Pages list: ")
    print_inline_list(pages_list)
    print("\n")
    print("Frames number: " + str(frames_number))
    print("\n")

    # Create a matrix of strings with dimensions large = frames_number length and tall f=pages_list size
    result_matrix = [[Frame() for col in range(frames_number)] for row in range(len(pages_list))]
    print("Empty list: \n")
    print(print_format_matrix(result_matrix))

    print("************** Started *************")

    for state in range(len(result_matrix)-1):
        print(state)
        # Calculate the state
       # page_request()

    print("************** Finished ************")
    # Return the transpose of the result matrix because we considered each time as a row
    return transpose_matrix(result_matrix)


def is_space_in_list(target_list):
    """
    Function that takes a list and return true if the there is a item inside
    marked as empty
    :return: boolean true if there is space
    """
    for frame in target_list:
        if frame.is_empty:
            return True
    return False



def page_request(frames_list, target_page):
    if(is_space_in_list(frames_list)):
        # Put the target frame into the empty frame
        for frame in frames_list:
            print(frame)
