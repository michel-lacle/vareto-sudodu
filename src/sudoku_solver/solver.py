


def is_valid_solution_with_set_validator(sudoku):

    # the key observation from our meeting is that rows and cols have the same processing logic:
    # check if a number is repeated. (we are ignoring other validations like cell value < 0 || > 9)

    # therefore we can do one pass and check both rows and cols at the same time.
    # so our runtime complexity would be the size of the sudoku row/col so 9 * 9 --> O(n*n)

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
