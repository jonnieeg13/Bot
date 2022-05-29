import os
import sqlite3
import platform
import sys
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


def return_filepath(database_directory):
    select_folder = False
    conn = None
    platform_name = platform.system()
    database_file_name = 'os_database_path.db'
    database = os.path.join(database_directory, database_file_name)
    systems = ['Linux', 'Darwin', 'Windows']
    try:
        conn = sqlite3.connect(database)
        conn.execute('CREATE TABLE IF NOT EXISTS FilePath (OS TEXT PRIMARY KEY, FILEPATH TEXT)')
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    filepath = ''
    return filepath


# test = get_top_directory()
# print(test)