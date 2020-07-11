def print_inline_list(target_list):
    """
    Print in the same line the elements of a list
    :param target_list: the list with the elements
    :return: None
    """
    for item in target_list:
        chunk = "'" + str(item) + "',"
        print(chunk, end=' ')


def print_format_matrix(matrix):
    """
    Print a matrix in a organized way using the function print_inline_list
    :param matrix: the target matrix
    :return: None
    """
    for row in matrix:
        print_inline_list(row)
        print("\n")


def transpose_matrix(matrix):
    """
    Transpose a matrix
    :param matrix: target matrix
    :return: result matrix
    """
    result_matrix = [[None for col in range(len(matrix))] for row in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_matrix[j][i] = matrix[i][j]

    print_format_matrix(result_matrix)
    return result_matrix


def get_matrix_for_response(matrix, default_null=None):
    """
    It return a matrix that is a list of list, instead a list o Frames()
    :param default_null:    The default value for null spaces. For example could be " " or -1
    :param matrix:          list o of list of Frames()
    :return:                list of lists of integers
    """
    list_of_lists = [[" " for col in range(len(matrix[0]))] for row in range(len(matrix))]

    for row_index, row in enumerate(matrix):
        for item_index, item in enumerate(row):
            primitive = item.get_content(default=default_null)
            list_of_lists[row_index][item_index] = primitive

    return list_of_lists
