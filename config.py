"""
Specifications for application
"""
import os
from typing import ClassVar

from pydantic import BaseModel

HOST = "127.0.0.1"
PORT = "8080"


class Config(BaseModel):
    """
    Configuration class for application
    """

    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: ClassVar[bool] = False
    SQLALCHEMY_DATABASE_URI: ClassVar[str] = os.environ.get(
        "DATABASE_URI", "sqlite:///sudoku.db"
    )


class LocalConfig(Config):
    """
    Configuration class for testing application
    """

    DEBUG: bool = True
