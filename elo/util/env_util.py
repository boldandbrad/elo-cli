import getpass
import os
import platform

from typing import Tuple

APP_NAME = "elo-cli"


def _os_file_paths() -> Tuple[str, str, str]:
    is_travis = "TRAVIS" in os.environ  # running in travis ci
    usrname = getpass.getuser()

    if platform.system() == "Linux" and not is_travis:
        home_path = f"/home/{usrname}/.{APP_NAME}/"
        log_path = f"/var/log/{APP_NAME}/"
    elif platform.system() == "Darwin" and not is_travis:
        home_path = f"/Users/{usrname}/.{APP_NAME}/"
        log_path = f"/Users/{usrname}/Library/Logs/{APP_NAME}/"
    elif platform.system() == "Windows" and not is_travis:
        home_path = f"C:\\Users\\{usrname}\\.{APP_NAME}\\"
        log_path = f"C:\\Users\\{usrname}\\AppData\\local\\{APP_NAME}\\"
    else:
        home_path = f".{APP_NAME}/"
        log_path = f".logs/{APP_NAME}/"

    config_path = home_path
    db_path = home_path + "series"

    return config_path, db_path, log_path


def get_config_path() -> str:
    config_path, _, _ = _os_file_paths()
    if not os.path.exists(config_path):
        os.makedirs(config_path)
    return config_path


def get_db_path() -> str:
    _, db_path, _ = _os_file_paths()
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    return db_path


def get_log_path() -> str:
    _, _, log_path = _os_file_paths()
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    return log_path
