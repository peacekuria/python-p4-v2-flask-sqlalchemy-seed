# server/app.py

from config import create_app
from config import db

# create a Flask application instance
app = create_app()


if __name__ == '__main__':
    app.run(port=5555, debug=True)

