import shutil
from pathlib import Path


def delete_directory(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


class FileCreator:
    def __init__(self, semester_name, course_file_names):
        self.course_file_names = course_file_names
        self.semester_name = semester_name

    def create_semester_file(self):
        Path(self.semester_name).mkdir(parents=False, exist_ok=False)

    def create_course_files(self):
        for files in self.course_file_names:
            path = f'{self.semester_name}\\{files}'
            Path(path).mkdir(parents=False, exist_ok=False)


# myList = ['CSE 3302', 'CSE 3330', 'MATH 2326', 'MATH 3330']
# test = 'G:\\Test'
# # delete_directory(test)
# filetest = FileCreator(test, myList)
# filetest.create_semester_file()
# filetest.create_course_files()
# # delete_directory(test)
