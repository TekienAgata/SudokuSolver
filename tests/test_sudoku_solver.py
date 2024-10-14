"""
Unit tests for Sudoku Solver module
"""
import logging

import pytest

from sudoku_solver import SudokuGrid


@pytest.mark.parametrize(
    "sudoku, expected",
    [
        (
            "solved_correct_sudoku_grid",
            True,
        ),  # full correct example
        (
            "correct_sudoku_grid",
            True,
        ),  # partial correct example
        (
            "full_incorrect_sudoku_grid",
            False,
        ),  # full wrong example
        (
            "incorrect_sudoku_grid",
            False,
        ),  # partial wrong example
    ],
)
def test_is_valid(sudoku, expected, request):
    """
    Test the is_valid method of SudokuGrid
    """
    sudoku_grid = SudokuGrid(request.getfixturevalue(sudoku))
    assert sudoku_grid.is_valid() == expected


@pytest.mark.parametrize(
    "test_input",
    [
        (
            1,
            0,
            2,
            "correct_sudoku_grid",
            True,
        ),
        (
            3,
            0,
            2,
            "correct_sudoku_grid",
            False,
        ),
    ],
)
def test_single_cell_verifier(test_input, request):
    """
    Test the single_cell_verifier method of SudokuGrid
    """
    digit, row, col, sudoku, expected = test_input
    sudoku_solver = SudokuGrid(request.getfixturevalue(sudoku))
    assert sudoku_solver.single_cell_verifier(digit, row, col) == expected


@pytest.mark.parametrize(
    "sudoku, expected",
    [
        (
            "solved_correct_sudoku_grid",
            True,
        ),  # full correct example
        (
            "correct_sudoku_grid",
            True,
        ),  # partial correct example
        (
            "full_incorrect_sudoku_grid",
            False,
        ),  # full wrong example
        (
            "incorrect_sudoku_grid",
            False,
        ),  # partial wrong example
    ],
)
def test_solve_sudoku(sudoku, expected, request):
    """
    Test the solve_sudoku method of SudokuGrid
    """
    sudoku_grid = SudokuGrid(request.getfixturevalue(sudoku))
    assert sudoku_grid.solve_sudoku() == expected


@pytest.mark.parametrize(
    "sudoku, expected",
    [
        (
            "solved_correct_sudoku_grid",
            (-1, -1),
        ),
        (
            "correct_sudoku_grid",
            (0, 2),
        ),
    ],
)
def test_find_empty_cell(sudoku, expected, request):
    """
    Test the find_empty_cell method of SudokuGrid
    """
    sudoku_grid = SudokuGrid(request.getfixturevalue(sudoku))
    assert sudoku_grid.find_empty_cell() == expected


@pytest.mark.parametrize(
    "sudoku, expected_message, expected_grid",
    [
        (
            [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ],
            "This sudoku is correct",
            str(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ]
            ),
        ),  # full correct example
        (
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9],
            ],
            "This sudoku is correct",
            str(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ]
            ),
        ),  # partial correct example
        (
            [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 4, 3, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 3],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 1, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ],
            "This sudoku is incorrect",
            str(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 4, 3, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 3],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 1, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ]
            ),
        ),  # full wrong example
        (
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 0, 1, 9, 0, 0, 5],
                [0, 0, 0, 4, 8, 0, 0, 7, 9],
            ],
            "This sudoku is incorrect",
            str(
                [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 0, 1, 9, 0, 0, 5],
                    [0, 0, 0, 4, 8, 0, 0, 7, 9],
                ],
            ),
        ),  # partial wrong example - program goes through full recursive cycle
        (
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 4, 8, 0, 0, 7, 9],
            ],
            "This sudoku is incorrect",
            str(
                [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 4, 8, 0, 0, 7, 9],
                ],
            ),
        ),  # partial wrong example - the starting grid is incorrect
    ],
)
def test_solve_sudoku_logging(sudoku, expected_message, expected_grid, caplog):
    """
    Test the solve_sudoku_logging method of SudokuGrid with logging
    """
    # given
    caplog.set_level(logging.INFO)
    sudoku_grid = SudokuGrid(sudoku)
    # when
    sudoku_grid.solve_sudoku()
    logs = caplog.records
    # then
    assert logs[0].message == expected_message
    assert logs[1].message == expected_grid
