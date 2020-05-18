#! /home/alex/Env/bin/python3

from app import make_app


if __name__ == "__main__":
    app = make_app()
    app.run(host="0.0.0.0", port=65000, debug=True)
