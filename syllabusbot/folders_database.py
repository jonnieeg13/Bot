import sqlite3
import platform


def return_filepath():
    conn = None
    platform_name = platform.system()
    try:
        conn = sqlite3.connect('file_path.db')
        conn.execute('CREATE TABLE IF NOT EXISTS FilePath (OS TEXT PRIMARY KEY, FILEPATH TEXT)')
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    filepath = ''
    return filepath



