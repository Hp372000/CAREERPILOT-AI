import sqlite3
from pathlib import Path

DB_PATH = Path("data/jobs.db")


def get_connection():
    """Returns a SQLite connection object."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dict-like objects
    return conn
