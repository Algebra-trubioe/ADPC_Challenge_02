import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG

def connect_to_postgres():
    """
    Connects to the Postgres instance in the cloud using credentials from config file.
    Returns a connection object and a cursor object.
    """
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            database=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            port=DB_CONFIG['port']
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        return conn, cursor
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        exit(1)

def print_table_info(cursor, table_name):
    """
    Prints the name of the columns, their data types, and constraints (if applicable)
    for the given table.
    """
    cursor.execute(f"SELECT * FROM information_schema.columns WHERE table_name = '{table_name}'")
    columns = cursor.fetchall()
    print(f"Table: {table_name}")
    print("Column Name | Data Type | Constraints")
    print("-" * 50)
    for column in columns:
        print(f"{column['column_name']} | {column['data_type']} | {column['column_default'], column['is_nullable']}")
    print()

def format_result_set(cursor):
    """
    Formats the output of a SELECT query (result set).
    """
    rows = cursor.fetchall()
    if rows:
        column_names = [desc[0] for desc in cursor.description]
        print("-" * (sum(len(name) for name in column_names) + 3 * (len(column_names) - 1)))
        print(" | ".join(column_names))
        print("-" * (sum(len(name) for name in column_names) + 3 * (len(column_names) - 1)))
        for row in rows:
            print(" | ".join(str(value) for value in row.values()))
        print("-" * (sum(len(name) for name in column_names) + 3 * (len(column_names) - 1)))
        print(f"{len(rows)} rows returned")
    else:
        print("No rows returned")
    print()

def repl():
    """
    Read-Evaluate-Print Loop for the Postgres client application.
    """
    conn, cursor = connect_to_postgres()
    print("Connected to PostgreSQL database!")
    print("Type 'exit' to quit or '\t <table_name>' to see table information")
    
    while True:
        try:
            user_input = input("postgres> ")
            if user_input.lower().strip() == "exit":
                conn.close()
                print("Goodbye!")
                break
            elif user_input.startswith("\t "):
                table_name = user_input.split(" ")[1]
                print_table_info(cursor, table_name)
            else:
                cursor.execute(user_input)
                if user_input.lower().strip().startswith("select"):
                    format_result_set(cursor)
                else:
                    print("Operation successful")
                conn.commit()
        except (Exception, psycopg2.Error) as error:
            print(f"Error: {error}")
            conn.rollback()  # Rollback in case of error

if __name__ == "__main__":
    repl()