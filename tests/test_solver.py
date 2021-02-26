from sudoku_solver.solver import is_valid_solution_with_set_validator
from sudoku_solver.solver import invalid_solved_sudoku
from sudoku_solver.solver import valid_solved_sudoku


def test_that_invalid_sudoku_is_not_a_valid_solution():
    is_valid = is_valid_solution_with_set_validator(invalid_solved_sudoku())

    assert is_valid == False

def test_that_valid_sudoku_is_a_valid_solution():
    is_valid = is_valid_solution_with_set_validator(valid_solved_sudoku())

    assert is_valid == True