# Postgres Client REPL Application

A command-line client application that enables users to connect to a Postgres instance in the cloud and interact with it through a REPL (Read-Evaluate-Print Loop) interface.

## Features

- Interactive REPL for executing SQL queries
- Formatted output for SELECT query results
- Table information command (`\t <table_name>`) to display column details
- Error handling for SQL operations
- Clean and formatted output presentation

### More about REPL

REPL stands for Read-Eval-Print Loop. It is an interactive programming environment that allows users to enter code, have it immediately executed, and see the results, all within a continuous loop.

The key components of a REPL are:

1. **Read**: The REPL reads the user's input, typically a single expression or statement.

2. **Evaluate**: The REPL evaluates the input, executing the code and generating a result.

3. **Print**: The REPL prints the result of the evaluation back to the user.

4. **Loop**: After printing the result, the REPL loops back to the beginning, waiting for the next user input.

REPLs are commonly used in programming languages and software development environments to provide an interactive way for users to experiment with code, test ideas, and debug issues. They are particularly useful for learning, prototyping, and quickly testing small pieces of code.

In the context of the Postgres client application you provided, the REPL allows the user to interact with the Postgres database by entering SQL queries or special commands, and immediately seeing the results or status of the operation. This makes it easier for users to explore the database and test different SQL statements without having to write and run full-fledged scripts.

## Prerequisites

- Python 3.7 or higher
- Access to a PostgreSQL database instance ([Tembo](https://tembo.io/) offers free trial, no card needed)
- Database connection details (host, database name, username, password)

## Installation

1. Clone this repository

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, create a file called config.py file with the database connection details:

```python
host = "your-postgres-host.provider.com"
database = "your_database"
user = "your_username"
password = "your_password"
```

## Usage

1. Start the application:
```bash
python postgres-client-app.py
```

2. Once the application is running, you can:
   - Execute SQL queries directly
   - Use `\t <table_name>` to view table information
   - Type `exit` to quit the application

### Example Commands

```sql
postgres> SELECT * FROM users;
postgres> \t users
postgres> INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
postgres> exit
```

### Special Commands

- `\t <table_name>`: Shows column names, data types, and constraints for the specified table
- `exit`: Closes the connection and exits the application

## Output Formatting

- SELECT query results are displayed in a formatted table
- Table information is displayed with column details and constraints
- Non-SELECT queries return success/failure status
- Error messages are clearly displayed when operations fail

## Error Handling

The application handles various types of errors:
- Connection errors
- SQL syntax errors
- Permission errors
- Invalid table names
- Invalid commands

## Security Notes

- Never commit your database credentials to version control
- Consider using environment variables for sensitive connection details
- Ensure proper database user permissions are set

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
