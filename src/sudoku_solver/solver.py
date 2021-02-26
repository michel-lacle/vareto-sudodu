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


def is_valid_solution_with_set_validator(sudoku):

    # the key observation from our meeting that rows and cols have the same processing logic:
    # check if a number is repeated. (we are ignoring other validations like cell value < 0 || > 9)

    # therefore we can do one pass and check both rows and cols at the same time.
    # so our n would be the size of the sudoku row so 9

    # we could use two data structures to keep track of rows and cols and test if we saw a number twice

    for i in range(len(sudoku)):

        # we use a set here for ease of use, but you can also use an array and use an index lookup to see if a bit
        # is set if we really want to be super efficient

        row_value_tracker = set()
        col_value_tracker = set()

        for j in range(len(sudoku[i])):

            # row check
            row = sudoku[i][j]

            if row in row_value_tracker:
                return False
            else:
                row_value_tracker.add(row)

            # col check
            col = sudoku[j][i]

            if col in col_value_tracker:
                False
            else:
                col_value_tracker.add(col)

    print("hooray, you have a valid solution to your sudoku")

    return True
