"""
Introducing fixtures for simple and consistent testing
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import LocalConfig
from factory import create_app
from models import Base


@pytest.fixture
def flask_test_app():
    """
    Fixture to create an instance of the application
    """
    app_instance = create_app(LocalConfig)
    yield app_instance


@pytest.fixture
def test_client(flask_test_app):
    """
    Fixture to create a test client for the application
    """
    with flask_test_app.test_client() as client:
        yield client


@pytest.fixture
def db_session(flask_test_app):
    """
    Fixture to create and drop the database for each test
    """
    with flask_test_app.app_context():
        engine = create_engine(LocalConfig.SQLALCHEMY_DATABASE_URI)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        session_instance = session()
        yield session_instance
        session_instance.close()
        Base.metadata.drop_all(engine)


@pytest.fixture
def correct_sudoku_grid():
    """
    Correct, unresolved sudoku grid to be used in tests
    """
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


@pytest.fixture
def solved_correct_sudoku_grid():
    """
    Correct resolved sudoku grid to be used in tests
    """
    return [
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


@pytest.fixture
def incorrect_sudoku_grid():
    """
    Incorrect, unresolved sudoku grid to be used in tests
    """
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 7],
    ]


@pytest.fixture
def full_incorrect_sudoku_grid():
    """
    Incorrect, full sudoku grid to be used in tests
    """
    return [
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
