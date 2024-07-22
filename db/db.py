from pathlib import Path
import sqlite3

_DB_PATH_FILE = Path(__file__).resolve()
_DB_PATH_DIR = _DB_PATH_FILE.parent
_DB_PATH_DATA = _DB_PATH_DIR.joinpath("data")


def check_path():
    return _DB_PATH_DIR.exists()


def create_collection(db_name: str):
    db_name += ".sqlite"
    try:
        db_path = _DB_PATH_DATA.joinpath(db_name)
        db = sqlite3.connect(db_path)
        print("Connected to database ", db_name)
    except sqlite3.OperationalError as e:
        print("Could not connect to database ", e)
    finally:
        db.close()


