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
    for the given table, with padded formatting for alignment.
    """
    cursor.execute(f"SELECT * FROM information_schema.columns WHERE table_name = '{table_name}'")
    columns = cursor.fetchall()
    
    if columns:
        # Define column headers
        headers = ["Column Name", "Data Type", "Constraints"]
        column_widths = [len(header) for header in headers]

        # Calculate maximum length for each column based on data
        for column in columns:
            column_widths[0] = max(column_widths[0], len(str(column['column_name'])))
            column_widths[1] = max(column_widths[1], len(str(column['data_type'])))
            constraint = f"{column['column_default']}, {column['is_nullable']}"
            column_widths[2] = max(column_widths[2], len(constraint))

        # Print table header
        header = " | ".join(headers[i].ljust(column_widths[i]) for i in range(len(headers)))
        print(f"Table: {table_name}")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        # Print each row with padded values
        for column in columns:
            row = [
                str(column['column_name']).ljust(column_widths[0]),
                str(column['data_type']).ljust(column_widths[1]),
                f"{column['column_default']}, {column['is_nullable']}".ljust(column_widths[2])
            ]
            print(" | ".join(row))
        print("-" * len(header) + "\n")
    else:
        print(f"No columns found for table '{table_name}'\n")


def format_result_set(cursor):
    """
    Formats the output of a SELECT query (result set) with padded columns.
    """
    rows = cursor.fetchall()
    if rows:
        column_names = [desc[0] for desc in cursor.description]
        column_widths = [len(col) for col in column_names]
        
        # Calculate maximum length of each column
        for row in rows:
            for i, value in enumerate(row.values()):
                column_widths[i] = max(column_widths[i], len(str(value)))
        
        # Print header
        header = " | ".join(name.ljust(column_widths[i]) for i, name in enumerate(column_names))
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        
        # Print each row with padded values
        for row in rows:
            row_data = " | ".join(str(value).ljust(column_widths[i]) for i, value in enumerate(row.values()))
            print(row_data)
        print("-" * len(header))
        print(f"{len(rows)} rows returned\n")
    else:
        print("No rows returned\n")

def repl():
    """
    Read-Evaluate-Print Loop for the Postgres client application with enhanced features.
    """
    conn, cursor = connect_to_postgres()
    print("Connected to PostgreSQL database!")
    print("Type 'exit' to quit or '\\t <table_name>' to see table information")
    
    while True:
        try:
            user_input = input("postgres> ")
            if user_input.lower().strip() == "exit":
                conn.close()
                print("Goodbye!")
                break
            elif user_input.startswith("\\t "):
                table_name = user_input.split(" ")[1]
                print_table_info(cursor, table_name)
            else:
                cursor.execute(user_input)
                if user_input.lower().strip().startswith("select"):
                    format_result_set(cursor)
                else:
                    affected_rows = cursor.rowcount
                    print(f"Operation successful, {affected_rows} rows affected")
                conn.commit()
        except (Exception, psycopg2.Error) as error:
            print(f"Error: {error}")
            conn.rollback()  # Rollback in case of error

if __name__ == "__main__":
    repl()