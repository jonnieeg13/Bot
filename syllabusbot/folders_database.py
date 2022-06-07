import os
import sqlite3
import platform
import sys
from inspect import getsourcefile
import click
from syllabusbot.file_dialog import GuiSelectFolder


def get_top_directory():
    print("Select the folder you want to store the folders of classes under")
    gui_folder_selector = GuiSelectFolder()
    gui_folder_selector.mainloop()
    input_folder = gui_folder_selector.get_folder_name()
    if not input_folder:
        print("No folder Chosen")
        sys.exit()
    return input_folder


def create_database(outside_database, systems_list, platform_name):
    file_path_name = get_top_directory()
    conn = sqlite3.connect(outside_database)
    conn_cur = conn.cursor()
    conn_cur.execute(
        '''CREATE TABLE IF NOT EXISTS FilePath (OS TEXT PRIMARY KEY, FOLDERPATH TEXT DEFAULT NULL)''')
    conn.commit()
    for os_name in systems_list:
        conn_cur.execute("""INSERT or IGNORE INTO FilePath (OS) VALUES(?)""", (os_name,))
    conn.commit()
    conn_cur.execute("""UPDATE FilePath SET FOLDERPATH = ? WHERE OS = ?""",
                     (file_path_name, platform_name,))
    conn.commit()
    if conn:
        conn.close()
    return file_path_name


def return_filepath():
    database_directory = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    top_folder_filepath = ''
    conn = None
    platform_name = platform.system()
    database_file_name = 'os_database_path.db'
    database = os.path.join(database_directory, database_file_name)
    systems_list = ['Linux', 'Darwin', 'Windows']
    if os.path.exists(database):
        try:
            conn = sqlite3.connect(database)
            conn_cur = conn.cursor()
            conn_cur.execute('''CREATE TABLE IF NOT EXISTS FilePath (OS TEXT PRIMARY KEY, FOLDERPATH TEXT DEFAULT NULL)''')
            conn.commit()
            conn_cur.execute('''SELECT OS from FilePath''')
            result = [item[0] for item in conn_cur.fetchall()]
            if sorted(result) == sorted(systems_list):
                os_path_result = conn_cur.execute("""SELECT FOLDERPATH from FilePath where OS=? and FOLDERPATH IS NOT NULL""", (platform_name,))
                os_path = os_path_result.fetchone()
                if os_path is None:
                    conn_cur.execute("""UPDATE FilePath SET FOLDERPATH = ? WHERE OS = ?""",
                                     (database_directory, platform_name,))
                    conn.commit()
                else:
                    if not click.confirm(
                        f"The current folder semester courses are saved to is: {os_path[0]}\n" +
                        "Would You Like Keep it?", default=True
                    ):
                        top_folder_filepath = get_top_directory()
                        conn_cur.execute("""UPDATE FilePath SET FOLDERPATH = NULL where FOLDERPATH is not NULL""")
                        conn.commit()
                        conn_cur.execute("""UPDATE FilePath SET FOLDERPATH = ? WHERE OS = ?""",
                                         (top_folder_filepath, platform_name,))
                        conn.commit()
                    else:
                        top_folder_filepath = os_path[0]
            else:
                top_folder_filepath = create_database(database, systems_list, platform_name)

        except sqlite3.Error as e:
            print("SQLITE Error:", e)
        finally:
            if conn:
                conn.close()
    else:
        try:
            top_folder_filepath = create_database(database, systems_list, platform_name)
        except sqlite3.Error as e:
            print("SQLITE Error:", e)

    return top_folder_filepath
