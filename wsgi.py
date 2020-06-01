#! /home/alex/Env/bin/python3

shebang = "#! /home/alex/Env/bin/python3"

from src import logger
from app import create_app
from utils.compile_scss import compile_scss


def main():
    logger.info("called")
    compile_scss()
    app = create_app()
    app.run(host="0.0.0.0", port=65000)


if __name__ == "__main__":
    main()
