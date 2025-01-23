from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()


mysql = mysql.connector.connect(
    host=os.getenv("SINGLESTOREDB_HOST"),
    port=os.getenv("SINGLESTOREDB_PORT"),
    user=os.getenv("SINGLESTOREDB_USER"),
    password=os.getenv("SINGLESTOREDB_PASSWORD"),
    database=os.getenv("SINGLESTOREDB_DATABASE"),
)


def get_cursor(): return mysql.cursor()
