"""
Unit testing for sudoku solver api module
"""


def test_solve_sudoku_success(test_client, correct_sudoku_grid):
    """
    Testing api with correct json and correct solution
    """
    # given
    # when
    response = test_client.post(
        "/api/v1/solve-sudoku", json={"sudoku_grid": correct_sudoku_grid}
    )

    # then
    assert response.status_code == 200
    assert response.json["solving_outcome"] == "success"
    assert response.json["sudoku_grid_filled_in"] is not None


def test_solve_sudoku_failure(test_client, incorrect_sudoku_grid):
    """
    Testing api with correct json and incorrect sudoku grid
    """
    # given
    # when
    response = test_client.post(
        "/api/v1/solve-sudoku", json={"sudoku_grid": incorrect_sudoku_grid}
    )

    # then
    assert response.status_code == 200
    assert response.json["solving_outcome"] == "failure"
    assert (
        response.json["reason"]
        == "This sudoku is incorrect and could not be solved"
    )


def test_solve_sudoku_json_missing(test_client):
    """
    Testing api with no json provided
    """
    # given
    # when
    response = test_client.post("/api/v1/solve-sudoku")

    # then
    assert response.status_code == 400
    assert (
        response.json["errors"]["sudoku_grid"]
        == "Sudoku grid is required Correct sudoku grid must be 9x9 integers "
        "Missing required parameter in the JSON body"
    )
    assert response.json["message"] == "Input payload validation failed"


def test_solve_sudoku_empty_json(test_client):
    """
    Testing api with empty json
    """
    json_data = {}

    response = test_client.post("/api/v1/solve-sudoku", json=json_data)

    assert response.status_code == 400
    assert (
        response.json["errors"]["sudoku_grid"]
        == "Sudoku grid is required Correct sudoku grid must be 9x9 integers "
        "Missing required parameter in the JSON body"
    )
    assert response.json["message"] == "Input payload validation failed"


def test_solve_sudoku_wrong_data_type(test_client):
    """
    Testing api with incorrect data type
    """
    # given
    invalid_data = {"sudoku_grid": "invalid"}

    # when
    response = test_client.post("/api/v1/solve-sudoku", json=invalid_data)

    # then
    assert response.status_code == 400
    assert (
        response.json["errors"]
        == "Sudoku grid is required Correct sudoku grid must be 9x9 integers"
    )
    assert response.json["message"] == "Input payload validation failed"
