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
        self.updated_time = None  # This represent the time when a page was put inside this frame

    def set_content(self, page, time):
        """
        Set a page as content
        :param time: The current time of the state
        :param page: target page
        :return: None
        """
        self.content = page
        self.updated_time = time
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

    def copy_itself(self):
        """
        :return: A different object with the same self attributes
        """
        new_copy = Frame()
        new_copy.content = self.content
        new_copy.is_empty = self.is_empty
        new_copy.updated_time = self.updated_time
        return new_copy

    def __str__(self) -> str:
        """
        Return the content in string representation
        :return:
        """
        if self.is_empty:
            return "Empty"
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
    print("Len of the matrix: " + str(len(result_matrix)))
    # Variable that let us know the current time
    current_time = 0
    frames_list = result_matrix[current_time]
    for row in result_matrix:
        # print("Matrix at the time: " + str(current_time - 1))
        # print_format_matrix(result_matrix)
        # print("Next step\n")

        # print("Frames list")
        # print_inline_list(frames_list)
        # print("\n")
        # Calculate the state and set it to the current row
        new_row = calculate_next_state(frames_list=frames_list,
                                       target_page=pages_list[current_time],
                                       current_time=current_time)
        print("New row")
        print_inline_list(new_row)
        print("\n")
        result_matrix[current_time] = new_row
        print("Matrix at the time: " + str(current_time))
        # Put a copy of this sate to the next row
        if current_time < len(result_matrix) - 1:
            frames_list = snapshot(new_row)

        # Update the time
        current_time = current_time + 1

    print("************** Finished ************")
    # TODO: Return the transpose of the result matrix because we considered each time as a row
    return result_matrix


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


def is_page_loaded(frames_list, target_page):
    """
    Verify if the page is inside some frame in the list
    :param frames_list: frame list
    :param target_page: reuqested page
    :return: True when the page is loaded otherwise return False
    """
    for frame in frames_list:
        if frame.content == target_page:
            return True
    return False


def calculate_next_state(frames_list, target_page, current_time):
    if not is_page_loaded(frames_list, target_page):  # If the page is not loaded

        if is_space_in_list(frames_list):  # If there is space
            # Put the target frame into the empty frame
            for frame in frames_list:
                if frame.is_empty:
                    frame.set_content(page=target_page, time=current_time)
                    return frames_list

        else:  # If there is not space
            pass  # TODO
    else:
        # A fail happen
        # Increment the counter of fails
        pass

    return frames_list


def snapshot(frames_list):
    """
    This method return a new list with new instance of each element
    :param frames_list: target list
    :return: a new copy with identical instances os each element
    """
    snapshot_list = []

    for item in frames_list:
        snapshot_list.append(item.copy_itself())
    return snapshot_list
