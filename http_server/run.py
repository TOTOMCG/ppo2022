#! /usr/bin/env python3
import os
import json
import ctypes
import platform
import argparse
from pathlib import Path

APP_WORK_DIR = Path(os.path.dirname(__file__))

HOME = Path(os.environ.get("HOMEPATH", "HOME"))

APP_HOME = APP_WORK_DIR / Path("ppo")
# APP_HOME = HOME / Path(".ppo")

VENV_DIR = "venv_ppo"

CFG = {
    "flask": {
        "port": "",
        "host": "0.0.0.0",
        "debug": True
    },
    "database": {
        "path": str(APP_HOME / "ppo.db")
    },
    "device": {
        "path": str(APP_HOME / "data")
    }
}


def init():
    parser = argparse.ArgumentParser(description='PPO CASE 8')
    parser.add_argument("--port", action="store",
                        dest="port", default=9999)
    parser.add_argument("--debug", action="store_true",
                        dest="debug", default=False)
    args = parser.parse_args()
    try:
        PORT = int(args.port)
    except Exception:
        PORT = 9999
    IS_DEBUG_MODE = args.debug
    CFG["flask"]["port"] = PORT
    CFG["flask"]["debug"] = IS_DEBUG_MODE


def install_virtualenv():
    try:
        os.system("virtualenv --version")
    except Exception:
        os.system("pip3 install virtualenv")


def create_virtualenv():
    if not os.path.isdir(APP_WORK_DIR / VENV_DIR):
        os.system(f"cd {APP_WORK_DIR}; virtualenv -p python3 {VENV_DIR}")


def make_dirs():
    if not os.path.isdir(APP_HOME):
        os.mkdir(APP_HOME)
        if platform.system() == "Windows":
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(
                APP_HOME, FILE_ATTRIBUTE_HIDDEN)
    if not os.path.isdir(APP_HOME / CFG["device"]["path"]):
        os.mkdir(APP_HOME / CFG["device"]["path"])


def get_port():
    return CFG['flask']['port']


def is_debug():
    return CFG['flask']['debug']


def run():
    cmd1 = os.path.join(APP_WORK_DIR, VENV_DIR, "bin", "activate")
    if platform.system() != "Windows":
        cmd1 = ". " + cmd1

    cmd2 = f"{VENV_DIR}/bin/pip3 install -r {APP_WORK_DIR}/requirements.txt"
    os.system(f"{cmd1} && {cmd2}")
    args = f"--port {get_port()} {is_debug() and '--debug' or ''}"
    os.system(f"{APP_WORK_DIR}/src/server.py {args}")


def write_config():
    with open(APP_WORK_DIR / Path("src") / "config.json", "w") as fp:
        json.dump(CFG, fp, indent=2, ensure_ascii=False)


def main():
    init()
    install_virtualenv()
    create_virtualenv()
    make_dirs()
    write_config()
    run()


if __name__ == "__main__":
    main()
