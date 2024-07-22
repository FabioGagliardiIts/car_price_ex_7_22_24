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


##Modifiche Dammacco

from pathlib import Path
import sqlite3
import pandas as pd
import requests
from io import StringIO

# Definizione del Path
# in queste tre righe ho risolto l'accesso al database
_DB_PATH_FILE = Path(__file__).resolve()
_DB_PATH_DIR = _DB_PATH_FILE.parent
_DB_PATH_DATA = _DB_PATH_DIR.joinpath('data')

def check_path():
    print(_DB_PATH_DIR)

#inserimento tramite streaming IO
def insert_db(db_name:str, table_name: str, db_from: str):
    try:
        db_name += ".sqlite"
        db_temp_name = db_name + ".csv"
        db_path = _DB_PATH_DATA.joinpath(db_name)
        response = requests.get(db_from)
        if response.status_code != 200:
            raise RuntimeError(f"Errore durante il download del file: Codice di stato {response.status_code}")

        # Leggi il contenuto del file CSV direttamente in un DataFrame di pandas
        csv_content = response.content.decode('utf-8')
        df = pd.read_csv(StringIO(csv_content))

        #db
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()

    except Exception as e:
        raise RuntimeError(f"Errore durante l'inserimento nel database: {str(e)}")


def insert_from_pd(db_name:str, table_name: str, db_csv_from: str):
    try:
        db_name += ".sqlite"
        db_temp_name = db_name + ".csv"
        db_path = _DB_PATH_DATA.joinpath(db_name)
        df = pd.read_csv(db_csv_from)

        #nel caso in cui non fosse csv
        #df = pd.read_excel('https://example.com/path/to/dataset.xlsx')
        #df = pd.read_json('https://example.com/path/to/dataset.json')

        #vado a fare le modifiche necessarie sul dataframe
        columns_drop = ["CarName", "symboling", "fueltype", "aspiration", "doornumber", "carbody", "drivewheel",
                        "car_ID", "fuelsystem", "enginelocation", "enginetype", "cylindernumber"]
        subset = df.drop(columns=columns_drop)

        #db
        conn = sqlite3.connect(db_path)
        #Altri valori possibili sono 'fail' (genera un errore se la tabella esiste) e 'append' (aggiunge i dati alla tabella esistente)
        subset.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()

    except Exception as e:
        raise RuntimeError(f"Errore durante l'inserimento nel database: {str(e)}")