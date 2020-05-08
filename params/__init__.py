import os
import json


LOGS = json.load(open("params/public/logs.json"))
# PUBLIC_MAIN = json.load(open("params/public/main.json"))
# PRIVATE_MAIN = json.load(open("params/private/main.json"))


# class _main:

#     url = os.getenv("MAIN_URL", PRIVATE_MAIN["url"])
#     email = os.getenv("MAIN_EMAIL", PRIVATE_MAIN["email"])
#     password = os.getenv("MAIN_PASSWORD", PRIVATE_MAIN["password"])
#     exec_path = os.getenv("MAIN_EXEC_PATH", PUBLIC_MAIN["exec_path"])
#     headless = bool(os.getenv("MAIN_HEADLESS", PUBLIC_MAIN["headless"]))
#     exec_hour = int(os.getenv("MAIN_EXEC_HOUR", PUBLIC_MAIN["exec_hour"]))
#     infinite_loop = bool(os.getenv("MAIN_INFINITE_LOOP", PUBLIC_MAIN["infinite_loop"]))
#     os_time_shift = int(os.getenv("MAIN_OS_TIME_SHIFT", PUBLIC_MAIN["os_time_shift"]))


class _logs:

    path = os.getenv("LOG_PATH", LOGS["path"])
    filename = os.getenv("LOG_FILENAME", LOGS["filename"])
    in_file = int(
        os.getenv("LOG_IN_FILE", LOGS["in_file"])
    )  # if True log in file else in stdout
    filemode = os.getenv(
        "LOG_FILEMODE", LOGS["filemode"]
    )  # ['a', 'w'] if "w" delete old file else append
    level = os.getenv("LOG_LEVEL", LOGS["level"])
    datefmt = "%Y-%m-%d %H:%M:%S"
    srtfmt = "%(asctime)s | %(levelname)-8s | %(message)s | %(funcName)s | %(lineno)d | %(module)s | %(filename)s"
    ext = os.getenv("LOG_EXT", LOGS["ext"])


class Params:
    # main = _main
    logs = _logs
