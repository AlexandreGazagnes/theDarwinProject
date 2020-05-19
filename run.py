#! /home/alex/Env/bin/python3


from src import logger
from app import make_app
from utils.compile_scss import compile_scss

if __name__ == "__main__":

    logger.info("called")

    compile_scss()
    app = make_app()
    app.run(host="0.0.0.0", port=65000, debug=True)
