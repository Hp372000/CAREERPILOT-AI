from .db import get_connection


def create_jobs_table():
    """Creates the jobs table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            link TEXT UNIQUE,
            description TEXT,
            skills TEXT,
            date_scraped TEXT
        );
        """
    )

    conn.commit()
    conn.close()
