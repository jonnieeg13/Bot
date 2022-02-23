from pathlib import Path


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


