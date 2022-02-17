#!  /usr/bin/env python3
import sqlite3


def read_sql_file():
    with open("./main.sql") as fp:
        content = fp.read()
    return content


def create_tables(connection, sql: str):
    connection.executescript(sql)


def main():
    connection = sqlite3.connect("/tmp/test.db")
    sql = read_sql_file()
    create_tables(connection, [sql])
    connection.close()


if __name__ == "__main__":
    main()
