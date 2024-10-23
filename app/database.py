import os
import sqlite3

from app.config import BASE_DIR


def database():
    db_path = os.path.join(BASE_DIR, "..", "users.db")

    con = sqlite3.connect(db_path)

    cur = con.cursor()

    return cur, con

