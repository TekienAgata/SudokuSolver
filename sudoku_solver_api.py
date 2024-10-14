"""
Module handling api calls for sudoku-solver
"""
import copy
import json

from flask import Blueprint, current_app, jsonify
from flask_restx import Api, Resource, fields, reqparse

from models import SudokuSolution
from sudoku_solver import SudokuGrid

sudoku = Blueprint("api", __name__)
sudoku_api = Api(sudoku)

# model for input validation
sudoku_input_model = sudoku_api.model(
    "SudokuInput",
    {
        "sudoku_grid": fields.List(
            fields.List(fields.Integer, required=True), required=True
        )
    },
)


def is_valid_9x9_int_matrix(data: list) -> bool:
    """
    Checks if json is a list of 9 lists, each containing exactly 9 integers
    """
    if not isinstance(data, list) or len(data) != 9:
        return False

    for row in data:
        if not isinstance(row, list) or len(row) != 9:
            return False

        for item in row:
            if not isinstance(item, int):
                return False

    return True


@sudoku_api.route("/solve-sudoku", methods=["POST"])
class SudokuSolver(Resource):
    """
    Sudoku solver api
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Parser for input validation
        """
        super().__init__(*args, **kwargs)

        self.sudoku_parser = reqparse.RequestParser()
        self.sudoku_parser.add_argument(
            "sudoku_grid",
            type=list,
            location="json",
            required=True,
            help="Sudoku grid is required "
            "Correct sudoku grid must be 9x9 integers",
        )

    @sudoku_api.expect(sudoku_input_model)
    def post(self) -> None:
        """
        Handles communication, receiving and returning data
        """
        requested_data = self.sudoku_parser.parse_args()
        sudoku_grid_lists = requested_data.get("sudoku_grid", [])
        if not is_valid_9x9_int_matrix(sudoku_grid_lists):
            # prepare and return response
            response_data = {
                "errors": "Sudoku grid is required "
                "Correct sudoku grid must be 9x9 integers",
                "message": "Input payload validation failed",
            }
            response = jsonify(response_data)
            response.status_code = 400
            return response

        # ensure there is an unchanged user inout available
        user_input = copy.deepcopy(sudoku_grid_lists)

        # make an instance of sudoku
        sudoku_grid = SudokuGrid(sudoku_grid_lists)

        # solve sudoku
        solve_outcome = sudoku_grid.solve_sudoku()
        outcome_sudoku = sudoku_grid.sudoku

        # save attempt in database
        db_session = current_app.db_session()
        sudoku_solution = SudokuSolution(
            user_input=json.dumps(user_input),
            outcome_grid=json.dumps(outcome_sudoku),
            outcome=solve_outcome,
        )
        db_session.add(sudoku_solution)
        db_session.commit()

        # prepare and return response
        if solve_outcome:
            response_data = {
                "solving_outcome": "success",
                "sudoku_grid_filled_in": outcome_sudoku,
            }
        else:
            response_data = {
                "solving_outcome": "failure",
                "reason": "This sudoku is incorrect and could not be solved",
            }
        return jsonify(response_data)
