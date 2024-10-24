import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_LITE = f"sqlite+aiosqlite:///{os.path.join(BASE_DIR, '..', 'users.db')}"
