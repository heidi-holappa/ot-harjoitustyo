from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS USERS;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS CONTACTS;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE USERS (
            username TEXT PRIMARY KEY,
            password TEXT,
            role TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE CONTACTS (
            username TEXT,
            datetime TEXT,
            channel TEXT,
            type TEXT,
            gender TEXT,
            age TEXT,
            content TEXT,
            marked INTEGER
        )
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
