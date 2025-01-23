from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = "mysql+pymysql://" + os.getenv("SINGLESTOREDB_URL")

PASSCODE = os.getenv("PASSCODE")
