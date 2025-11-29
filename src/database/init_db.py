from .models import create_jobs_table


def initialize_database():
    print("[DB] Initializing database...")
    create_jobs_table()
    print("[DB] jobs table created or already exists.")


if __name__ == "__main__":
    initialize_database()
