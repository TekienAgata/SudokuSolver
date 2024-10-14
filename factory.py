"""
Flask application blueprint
"""
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from sudoku_solver_api import sudoku


def create_engine_instance(uri):
    """
    Create SQLAlchemy engine
    """
    engine = create_engine(uri)
    return engine


def create_session(engine):
    """
    Create SQLAlchemy session
    """
    session = sessionmaker(bind=engine)
    return session


def create_app(configs) -> Flask:
    """
    Create a Flask app instance from blueprint
    """
    app = Flask(__name__)
    app.config.from_object(configs)

    engine = create_engine_instance(configs.SQLALCHEMY_DATABASE_URI)
    session = create_session(engine)
    app.db_session = session

    Base.metadata.create_all(engine)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> None:
    """
    Register blueprints to application
    """
    app.register_blueprint(sudoku, url_prefix="/api/v1")
