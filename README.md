# PostgreSQL Client REPL Application

A simple interactive command-line client for PostgreSQL databases that provides enhanced formatting and table information viewing capabilities.

## Features

- Interactive REPL (Read-Eval-Print Loop) interface
- Formatted query results with aligned columns
- Table structure inspection command
- Error handling with automatic transaction rollback
- Support for all PostgreSQL queries and commands

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

- PostgreSQL database server ([Tembo](https://tembo.io/) provides no 14 days card free trial)

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Update the database connection settings in `config.py`:

```python
DB_CONFIG = {
    'host': 'your-host',
    'database': 'your-database',
    'user': 'your-username',
    'password': 'your-password',
    'port': '5432'
}
```

## Usage

1. Start the application:

```bash
python postgres-client-app.py
```

2. Available commands:
   - Execute any SQL query at the `postgres>` prompt
   - Use `\t table_name` to view table structure
   - Type `exit` to quit the application

### Examples

View table information:
```sql
postgres> \t users
```

Execute a SELECT query:
```sql
postgres> SELECT * FROM users LIMIT 5;
```

Execute other SQL commands:
```sql
postgres> CREATE TABLE test (id serial PRIMARY KEY, name varchar(100));
```

## Features in Detail

### Table Information Display
- Column names
- Data types
- Constraints and default values
- Nullable status

### Query Result Formatting
- Aligned columns
- Automatic width adjustment
- Row count display (Specially useful for DML statements)
- Clear separation between header and data

## Security Note

Never commit `config.py` with real credentials to version control. Consider using environment variables or a secure secrets management system for production environments.