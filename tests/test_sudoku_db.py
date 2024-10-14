"""
Unit testing for the sudoku solver database operations
"""

import json

from models import SudokuSolution


def test_save_correct_sudoku_solution(
    test_client, db_session, correct_sudoku_grid, solved_correct_sudoku_grid
):
    """
    Test saving a correct Sudoku solution to the database
    """
    # given the app

    # when correct sudoku grid is posted
    response = test_client.post(
        "/api/v1/solve-sudoku", json={"sudoku_grid": correct_sudoku_grid}
    )

    # then
    assert response.status_code == 200

    saved_solution = db_session.query(SudokuSolution).first()
    assert saved_solution is not None
    assert saved_solution.user_input == json.dumps(correct_sudoku_grid)
    assert saved_solution.outcome is True
    assert saved_solution.outcome_grid == json.dumps(
        solved_correct_sudoku_grid
    )


def test_save_incorrect_sudoku_solution(
    test_client, db_session, incorrect_sudoku_grid
):
    """
    Test saving an incorrect Sudoku solution to the database
    """
    # given the app

    # when incorrect sudoku grid is posted
    response = test_client.post(
        "/api/v1/solve-sudoku", json={"sudoku_grid": incorrect_sudoku_grid}
    )

    # then
    assert response.status_code == 200

    # Check if the Sudoku solution is saved in the database
    saved_solution = db_session.query(SudokuSolution).first()
    assert saved_solution is not None
    assert saved_solution.user_input == json.dumps(incorrect_sudoku_grid)
    assert saved_solution.outcome is False
    assert saved_solution.outcome_grid == json.dumps(incorrect_sudoku_grid)
