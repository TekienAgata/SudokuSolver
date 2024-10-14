"""
Module to create the app with predefined specs
"""
from config import HOST, PORT, Config
from factory import create_app

app = create_app(Config)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
else:
    application = app
