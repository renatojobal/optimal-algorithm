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
            return "E"
        return str(self.content)

    def get_frame_details(self):
        """
        Return a string with all the details of this frame-
        Util for debug
        :return: string
        """
        string = """\n
            Content:{}
            Update time: {}
            Is empty: {}
            \n
        """.format(self.content, self.updated_time, self.is_empty)
        return string


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

    print("************** Started *************")
    print("Len of the matrix: " + str(len(result_matrix)))
    # Variable that let us know the current time
    current_time = 0
    frames_list = result_matrix[current_time]
    for row in result_matrix:
        print("Iteration = " + str(current_time))

        new_row = calculate_next_state(frames_list=frames_list,
                                       target_page=pages_list[current_time],
                                       current_time=current_time,
                                       pages_list=pages_list)

        result_matrix[current_time] = new_row

        # Put a copy of this sate to the next row
        if current_time < len(result_matrix) - 1:
            frames_list = snapshot(new_row)

        # Update the time
        current_time = current_time + 1

    print("************** Finished ************")
    # Return the transpose of the result matrix because we considered each time as a row
    return transpose_matrix(result_matrix)
    # return result_matrix


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
    :param target_page: requested page
    :return: True when the page is loaded otherwise return False
    """
    for frame in frames_list:
        if frame.content == target_page:
            return True
    return False


def all_pages_used_in_the_future(frames_list, pages_list, current_time):
    """
    Function that review the pages loaded in the frames list and verify if they are use in the future from the
    current time.
    :param current_time:    The current time of the state
    :param frames_list:     The frames list with the pages loaded
    :param pages_list:      The reference list with the pages
    :return:                True if all the pages from the frame list are used in the future. Otherwise return False
    """
    future_list = pages_list[current_time:]

    result_list = []  # A list o booleans
    for index, page in enumerate(pages_list):
        if page in future_list:
            result_list.append(True)
        else:
            result_list.append(False)

    if False in result_list:
        # "Not all pages are used in the future")
        return False
    # "All pages are used in teh future")
    return True


def replace_older_frame(frames_list, target_page, current_time):
    """
    This function compare the times when the frames were updated, we catch the older frame and insert it the target page
    :param current_time:The time of the state
    :param target_page: The target to be inserted in the older frame
    :param frames_list: Reference list with Frame items
    :return:            The updated frame list
    """

    target_index = 0  # Variable to know ere is the older frame

    minor = 999
    for index, frame in enumerate(frames_list):
        print(frame.get_frame_details())
        if frame.updated_time < minor:
            minor = frame.updated_time
            target_index = index

    older_frame = frames_list[target_index].copy_itself()

    # Insert the target page in the older frame
    older_frame.set_content(target_page, current_time)

    # Insert the update "older_frame" int the frames list
    frames_list[target_index] = older_frame

    # Return the updated target list
    return frames_list


def replace_useless_frame(frames_list, target_page, pages_list, current_time):
    """
    Main function of the optimal optimal algorithm.
    We replace the frame which content will not be used in the longest time
    :param pages_list:      The reference list with all the pages
    :param frames_list:     The frame list to be updated
    :param target_page:     The target page that we will insert in some frame
    :param current_time:    The time of the state
    :return:                Update frame list with the target page inside a frame
    """

    future_pages_list = pages_list[current_time:]

    list_of_indexes = get_indexes_of_next_used(page_list=future_pages_list, frames_list=frames_list)

    major = -999
    useless_frame_index = 0
    for dictionary in list_of_indexes:
        # Iterating over a list of dictionaries
        if dictionary["next_time_used"] > major:
            useless_frame_index = dictionary["frame_index"]
            major = dictionary["next_time_used"]

    # Insert the page in the useless frame

    frames_list[useless_frame_index].set_content(target_page, current_time)

    return frames_list


def get_next_time_used(target_page, page_list):
    """
    Return the first time when the target page appear on the list
    :param target_page:  Target page
    :param page_list:    List that contain the pages
    :return:             A integer value
    """
    for index, page in enumerate(page_list):
        if page == target_page:
            return index


def get_indexes_of_next_used(page_list, frames_list):
    """
    Return a list with the indexes of the the next when the page into the fragment will appear in the page list
    :param page_list:   Reference page list
    :param frames_list: A list of Frames items
    :return:            A list of integers
    """
    next_time_used = []
    for frame_index, frame in enumerate(frames_list):
        index_next_time_use = get_next_time_used(frame.content, page_list)
        dict_element = {"frame_index": frame_index, "next_time_used": index_next_time_use}

        next_time_used.append(dict_element)

    return next_time_used


def calculate_next_state(frames_list, target_page, current_time, pages_list):
    print("Current frame list: ")
    print_inline_list(frames_list)
    pages_in_future = pages_list[current_time:]
    print("\nPages in the future: " + str(pages_in_future))
    print("Target page: {}\n".format(target_page))

    if not is_page_loaded(frames_list, target_page):  # If the page is not loaded
        # A fail happen
        # Increment the counter of fails
        print("\n*Fail request\n")

        if is_space_in_list(frames_list):  # If there is space
            # Put the target frame into the empty frame
            for frame in frames_list:
                if frame.is_empty:
                    frame.set_content(page=target_page, time=current_time)
                    return frames_list
        else:
            if all_pages_used_in_the_future(frames_list, pages_list, current_time):
                print("All pages are used in teh future\n")
                # If true: apply optimal algorithm
                updated_frame_list = replace_useless_frame(frames_list=frames_list,
                                                           target_page=target_page,
                                                           pages_list=pages_list,
                                                           current_time=current_time)
                return updated_frame_list
            else:
                print("Not all pages are used in the future\n")
                # Apply FIFO with the pages that are not used in the future
                updated_frame_list = replace_older_frame(frames_list, target_page, current_time)
                print("Update frame list: ")
                print_inline_list(updated_frame_list)
                print("\n")
                return updated_frame_list

    else:
        # The page is already loaded so alright
        print("The page is already loaded\n")
        pass

    return frames_list.copy()


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
