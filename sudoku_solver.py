"""
Module receiving a sudoku grid and solving if possible
"""
from logger import logging


class SudokuGrid:
    """
    Class representing a Sudoku grid and providing methods for solving.
    """

    def __init__(self, sudoku) -> None:
        self.sudoku = sudoku

    def is_valid(self) -> bool:
        """
        checks lengths of rows and columns
        then checks for repetitions within rows, columns and 3x3 grids
        verifies if current 9x9 grid is valid even if incomplete
        """
        visited = set()
        if len(self.sudoku) != 9 or any(len(row) != 9 for row in self.sudoku):
            return False
        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] != 0:
                    row_str = f"{self.sudoku[row][col]} in row {row}"
                    col_str = f"{self.sudoku[row][col]} in col {col}"
                    grid_str = (
                        f"{self.sudoku[row][col]} in grid "
                        f"{row // 3} {col // 3}"
                    )
                    current_values = {row_str, col_str, grid_str}
                    if current_values & visited:
                        return False
                    visited |= current_values
        return True

    def single_cell_verifier(self, digit: int, row: int, col: int) -> bool:
        """
        checks if a digit can, potentially, be inserted at given position
        """
        if digit in self.sudoku[row]:
            return False
        if digit in [self.sudoku[i][col] for i in range(9)]:
            return False
        # below checks the 3x3 grid for repetitions with digit
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for through_rows in range(start_row, start_row + 3):
            for through_cols in range(start_col, start_col + 3):
                if digit == self.sudoku[through_rows][through_cols]:
                    return False
        return True

    def find_empty_cell(self) -> tuple:
        """
        finds first empty cell from tab[0][0]
        """
        for row in range(9):
            for column in range(9):
                if self.sudoku[row][column] == 0:
                    return row, column
        return -1, -1

    def _solve_sudoku(self) -> bool:
        """
        searches for an empty cell and
        if there is none, checks if the sudoku is correct
        if it finds empty cell, attempts to fill it in recursively
        """
        row, col = self.find_empty_cell()
        if col == -1 or row == -1:
            return bool(self.is_valid())

        for digit in range(1, 10):
            if self.single_cell_verifier(digit, row, col):
                self.sudoku[row][col] = digit
                if self._solve_sudoku():
                    return True
                self.sudoku[row][col] = 0
        return False

    def solve_sudoku(self) -> bool:
        """
        Method to enable correct status logs in recursive solution
        """
        if self._solve_sudoku():
            logging.info("This sudoku is correct")
            logging.info(self.sudoku)
            return True
        logging.info("This sudoku is incorrect")
        logging.info(self.sudoku)
        return False
