shebang = "#! /home/alex/Env/bin/python3"

from flask.cli import FlaskGroup

from src import logger
from app import create_app
from utils.compile_scss import compile_scss


app = create_app()


# def main():
#     logger.info("called")
#     compile_scss()
#     app = create_app()
#     # cli = FlaskGroup(app)
#     app.run(host="0.0.0.0", port=5000)
#     # cli()


# if __name__ == "__main__":
#     main()
