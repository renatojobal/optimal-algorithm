def print_inline_list(target_list):
    """
    Print in the same line the elements of a list
    :param target_list: the list with the elements
    :return: None
    """
    for item in target_list:
        print(item, end=' ')


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

    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            result_matrix[j][i] = matrix[i][j]

    print_format_matrix(result_matrix)
    return result_matrix
