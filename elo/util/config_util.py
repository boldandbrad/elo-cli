import json
import os

from elo.util.env_util import get_config_path

defaults = {
    "active-series": "default",
}

CONFIG_FILE = "config.json"


def config_init() -> None:
    """Initialize and check elo-cli user configuration file."""
    config_path = get_config_path()

    # create config file
    if not os.path.isfile(config_path + CONFIG_FILE):
        with open(config_path + CONFIG_FILE, "w") as file:
            json.dump(defaults, file, indent=4)
    else:
        # TODO: check that existing config is valid
        pass


def read_config_file():
    config_path = get_config_path()

    with open(config_path + CONFIG_FILE, "r") as fp:
        data = fp.read()

    conf = json.loads(data)
    return conf


def update_config_file(conf: dict) -> None:
    config_path = get_config_path()

    with open(config_path + CONFIG_FILE, "w") as fp:
        json.dump(conf, fp, indent=4)


def set_default_configs() -> dict:
    return update_config_file(defaults)


def get_config_value(key: str) -> str:
    conf = read_config_file()
    return conf[key]


def set_config_value(key: str, val: str) -> str:
    conf = read_config_file()
    conf[key] = val
    update_config_file(conf)
    return val
