import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


class GuiSelectFolder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.filename = None
        self.title('Open File Dialog')
        self.resizable(False, False)
        self.geometry('300x150')
        self.open_button = ttk.Button(
            self,
            text='Select Folder',
            command=self.select_file
        )
        self.label1 = tk.Label(self,
                               text="Select the folder you want to\n"
                                    "store the folders of classes under",
                               font=("Arial", 12))
        self.label1.pack(expand=True)
        self.open_button.pack(expand=True)

    def select_file(self):
        self.filename = fd.askdirectory(title='Select The Folder')
        self.destroy()

    def get_folder_name(self):
        return self.filename
