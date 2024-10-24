import os
import sqlite3

from config import BASE_DIR


def db():
    db_path = os.path.join(BASE_DIR, "..", "users.db")

    con = sqlite3.connect(db_path)

    cur = con.cursor()

    return cur, con

