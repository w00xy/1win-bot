import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_LITE = f"sqlite+aiosqlite:///{os.path.join(BASE_DIR, '..', 'users.db')}"
# PROD
DB_LITE = f"sqlite+aiosqlite:///data/users.db"
BOT_TOKEN = os.getenv("BOT_TOKEN")
REF_URL = "https://1wimdx.life/casino/list/4?p=306v"
IMAGE_FOLDER = os.path.join(BASE_DIR, "utils", "images", "1win")