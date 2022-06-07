import os
import sqlite3
import platform
import sys
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


# INSERT INTO FilePath(OS) VALUES('Linux'), ('Darwin'), ('Windows');
# SELECT OS from FilePath where FOLDERPATH is NULL;
def return_filepath():
    database_directory = get_top_directory()
    select_folder = False
    conn = None
    platform_name = platform.system()
    database_file_name = 'os_database_path.db'
    database = os.path.join(database_directory, database_file_name)
    systems_list = ['Linux', 'Darwin', 'Windows']
    if os.path.exists(database):
        pass
    try:
        conn = sqlite3.connect(database)
        conn_cur = conn.cursor()
        conn_cur.execute('''CREATE TABLE IF NOT EXISTS FilePath (OS TEXT PRIMARY KEY, FOLDERPATH TEXT DEFAULT NULL)''')
        conn.commit()
        conn_cur.execute('''SELECT OS from FilePath''')
        result = conn_cur.fetchone()
        if result:
            os_path_result = conn_cur.execute("""SELECT FOLDERPATH from FilePath where OS=? and FOLDERPATH IS NOT NULL""", (platform_name,))
            os_path = os_path_result.fetchone()
            if os_path is None:
                conn_cur.execute("""UPDATE FilePath SET FOLDERPATH = ? WHERE OS = ?""",
                                 (database_directory, platform_name,))
                conn.commit()
            else:
                if not click.confirm(
                    f"The Path that's on the DB is {os_path[0]}\n" +
                    "Would You Like Keep it?", default=True
                ):
                    database_directory = get_top_directory()
                    conn_cur.execute("""UPDATE FilePath SET FOLDERPATH = NULL where FOLDERPATH is not NULL""")
                    conn.commit()
                    conn_cur.execute("""UPDATE FilePath SET FOLDERPATH = ? WHERE OS = ?""",
                                     (database_directory, platform_name,))
                    conn.commit()
            # print("Something Here")
        else:
            for os_name in systems_list:
                conn_cur.execute("""INSERT or IGNORE INTO FilePath (OS) VALUES(?)""", (os_name,))
            conn.commit()
            # print("Not Here!")

    except sqlite3.Error as e:
        print("SQLITE Error:", e)
    finally:
        if conn:
            conn.close()

    return database_directory


test = return_filepath()
print(test)
