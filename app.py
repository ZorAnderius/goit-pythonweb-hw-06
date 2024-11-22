from config.db import get_db
def execute_query():
    db = next(get_db())
    try:
        pass
    finally:
        db.close()


if __name__ == '__main__':
        execute_query()