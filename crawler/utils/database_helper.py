from crawler.utils.database import connection

migration_file = "schema/book_crawler_database.sql"
drop_database_file = "schema/drop_book_crawler_database.sql"


def reset_database():
    print("reset database")
    return run_sql_file(drop_database_file)


def run_migration():
    print("run migration")
    return run_sql_file(migration_file)


def run_sql_file(file_name):
    """
    Execute an SQL file
    :param file_name: file path
    """
    statements = __parse_sql(file_name)
    conn = connection()
    try:
        with conn.cursor() as cursor:
            for statement in statements:
                cursor.execute(statement)
            conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()


def __parse_sql(file_name, delimiter=';'):
    data = open(file_name, 'r').readlines()
    stmts = []
    stmt = ''

    for _, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            delimiter = line.split()[1]
            continue

        if delimiter not in line:
            stmt += line.replace(delimiter, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip())
            stmt = ''
        else:
            stmts.append(line.strip())

    return stmts
