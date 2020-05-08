import logging
import os


def setBasicConfig(Params):
    """Update logging.basicConfig from params.py

    args :
        filename (str): the filename of the root script
        ext (str) : the extension - optional - defaut is .log"""

    p_log = Params.logs

    # clean filename
    p_log.filename = p_log.filename.replace(".py", "")

    # base for basiConfig
    logging_dict = {
        "level": getattr(logging, p_log.level),
        "format": p_log.srtfmt,
        "datefmt": p_log.datefmt,
    }

    # logfile
    assert os.path.isdir(p_log.path)
    logfile = f"{p_log.path}{p_log.filename}{p_log.ext}"

    # if "w" as logging filemode rewrite logfile with header
    if (p_log.filemode == "w") and p_log.in_file:
        open(p_log.in_file, "w").write("")

    # if log_in_file update basiConfig
    if p_log.in_file:
        logging_dict.update({"filename": logfile, "filemode": "a"})

    # basic config and logger
    logging.basicConfig(**logging_dict)
