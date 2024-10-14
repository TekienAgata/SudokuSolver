"""
Creating models for the database
"""
from typing import List

from sqlalchemy import JSON, Boolean, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SudokuSolution(Base):
    """
    The class introduced to operate on the database
    """

    __tablename__: str = "sudoku_solutions"

    id: Column = Column(Integer, primary_key=True)
    user_input: Column = Column(JSON)
    outcome_grid: Column = Column(JSON)
    outcome: Column = Column(Boolean, default=False)

    def __init__(
        self,
        user_input: List[List[int]],
        outcome_grid: List[List[int]],
        outcome: bool,
    ) -> None:
        self.user_input = user_input
        self.outcome_grid = outcome_grid
        self.outcome = outcome

    def get_user_input(self) -> List[List[int]]:
        """
        Returns the user input for this Sudoku solution
        """
        return self.user_input

    def get_outcome_grid(self) -> List[List[int]]:
        """
        Returns the outcome grid for this Sudoku solution
        """
        return self.outcome_grid

    def is_successful(self) -> bool:
        """
        Returns True if the solution was successful, False otherwise
        """
        return self.outcome
