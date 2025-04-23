import logging

import coloredlogs
from dotenv import find_dotenv, load_dotenv
from waitress import serve

load_dotenv(find_dotenv())


if __name__ == "__main__":
    from app import create_app

    # Make sure to define the logger object
    logging.getLogger(__name__)
    logging.root.setLevel(logging.INFO)
    fmt_str = r"[%(asctime)s] - %(name)s - P%(process)s - %(levelname)s: %(message)s"
    formatter = logging.Formatter(fmt=fmt_str, datefmt=r"%Y-%m-%d %H:%M:%S")

    ## Just for console streaming with colored logs
    coloredlogs.install(level="INFO", fmt=fmt_str, isatty=True)

    app = create_app()
    serve(app, host="0.0.0.0", port=5000)
