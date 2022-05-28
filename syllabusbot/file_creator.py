from pathlib import Path
from syllabusbot.syllabus import get_syllabus_links
import requests
import os


class FileCreator:
    def __init__(self, semester_name, course_file_names):
        self.course_file_names = course_file_names
        self.semester_name = semester_name

    def create_course_files(self):
        Path(self.semester_name).mkdir(parents=False, exist_ok=False)
        for files in self.course_file_names:
            path = os.path.join(self.semester_name, files)
            Path(path).mkdir(parents=False, exist_ok=False)
            download_link_string, file_type = get_syllabus_links(files)
            response = requests.get(download_link_string)
            syllabus_string = files + ' ' + "SYLLABUS" + ' ' + file_type
            download_file = os.path.join(path, syllabus_string)
            with open(download_file, "wb") as download:
                download.write(response.content)
            print(f"{files} Directory and Syllabus Written")

# # # TESTER
# test_directory = r"C:\Users\jonni\Test Semester"
# myList = ['CSE 3330', 'CSE 3302', 'MATH 3330', 'MATH 2326']
# file_creator = FileCreator(test_directory, myList)
# file_creator.create_course_files()
