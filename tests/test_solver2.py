from sudoku_solver.solver2 import is_valid_solution

def invalid_solved_sudoku():
    return [
        [1,4,1,1,0,6,2,3,4],
        [4,6,1,5,3,4,5,3,7],
        [1,7,6,2,5,0,8,5,6],

        [5,3,1,3,9,8,1,3,8],
        [2,1,1,3,3,5,5,3,3],
        [8,1,1,6,3,7,5,4,3],

        [5,7,4,3,2,3,7,6,1],
        [6,2,4,7,8,9,5,5,1],
        [1,2,3,6,2,5,1,9,5],
    ]


def valid_solved_sudoku():
    return [
        [3,4,5,1,7,6,2,8,9],
        [9,6,2,3,4,8,5,1,7],
        [1,7,8,2,5,9,4,3,6],

        [4,3,6,5,9,2,1,7,8],
        [2,5,7,8,6,1,9,4,3],
        [8,9,1,7,3,4,6,2,5],

        [5,8,9,4,2,3,7,6,1],
        [6,1,4,9,8,7,3,5,2],
        [7,2,3,6,1,5,8,9,4],
    ]


# for boundary checking the last row/col
def almost_valid_sudoku_last_row_col_invalid():
    return [
        [3,4,5,1,7,6,2,8,9],
        [9,6,2,3,4,8,5,1,7],
        [1,7,8,2,5,9,4,3,6],

        [4,3,6,5,9,2,1,7,8],
        [2,5,7,8,6,1,9,4,3],
        [8,9,1,7,3,4,6,2,5],

        [5,8,9,4,2,3,7,6,1],
        [6,1,4,9,8,7,3,5,2],
        [7,2,3,6,1,5,8,9,1],
    ]


# for boundary checking the first row/col
def almost_valid_sudoku_first_row_col_invalid():
    return [
        [9,4,5,1,7,6,2,8,9],
        [9,6,2,3,4,8,5,1,7],
        [1,7,8,2,5,9,4,3,6],

        [4,3,6,5,9,2,1,7,8],
        [2,5,7,8,6,1,9,4,3],
        [8,9,1,7,3,4,6,2,5],

        [5,8,9,4,2,3,7,6,1],
        [6,1,4,9,8,7,3,5,2],
        [7,2,3,6,1,5,8,9,1],
    ]

def test_that_invalid_sudoku_is_not_a_valid_solution():
    is_valid = is_valid_solution(invalid_solved_sudoku())

    assert is_valid is False


def test_that_valid_sudoku_is_a_valid_solution():
    is_valid = is_valid_solution(valid_solved_sudoku())

    assert is_valid is True


def test_that_last_row_col_boundary_sudoku_is_not_a_valid_solution():
    is_valid = is_valid_solution(almost_valid_sudoku_last_row_col_invalid())

    assert is_valid is False


def test_that_first_row_col_boundary_sudoku_is_not_a_valid_solution():
    is_valid = is_valid_solution(almost_valid_sudoku_first_row_col_invalid())

    assert is_valid is False
