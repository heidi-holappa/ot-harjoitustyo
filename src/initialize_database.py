from database_connection import get_database_connection

def drop_tables(connection):
    """Destroys the tables from the database.

    Args:
        connection (connect object): an object that enables the database connection.
    """
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS USERS;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS CONTACTS;
    ''')

    connection.commit()


def create_tables(connection):
    """Creates database tables for the application

    Args:
        connection (connect object): an object that enables the database connection.
    """
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
            marked TEXT
        )
    ''')

    connection.commit()


def initialize_database():
    """Calls a method to activate the object that enables database connection.

    Calls methods to delete and create tables to database.

    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
