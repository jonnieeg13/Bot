from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import syllabusbot.constants as cons
from syllabusbot.parse_course import ParseCourse
from syllabusbot.file_creator import FileCreator
from syllabusbot.uta_course_regex import regex_match


class Courses(webdriver.Chrome):
    def __init__(self, driver_path=cons.DRIVER_PATH, teardown=False, semester=""):
        self.semester_path = self.get_semester()
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] = driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.semester = semester
        super(Courses, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def get_semester(self):
        while True:
            self.semester = input("Enter Semester and Year: ")
            if not regex_match(self.semester):
                print('Incorrect Semester Entered')
                continue
            else:
                break
        result = ' '.join(elem.capitalize() for elem in self.semester.split())
        # print("Semester", result)
        test = 'G:'
        path = f'{test}\\{result}'
        return path

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(cons.BASE_URL)

    def click_student_btn(self):
        front_stu_btn = self.find_element(By.ID, cons.FRONT_STUDENT_BTN)
        front_stu_btn.click()

    def login(self):
        login_button = self.find_element(By.XPATH, cons.LOGIN_BTN)
        login_button.click()

    def select_username(self, username):
        username_field = self.find_element(By.ID, cons.USER_NAME_SELECT_ID)
        username_field.clear()
        username_field.send_keys(username)

    def select_username_next(self):
        username_next = self.find_element(By.ID, cons.USER_NAME_SELECT_NEXT)
        username_next.click()

    def select_password(self, password):
        password_field = self.find_element(By.ID, cons.PASSWORD_SELECT_ID)
        password_field.clear()
        password_field.send_keys(password)

    def select_password_sign_in(self):
        password_sign_in = self.find_element(By.XPATH, cons.PASSWORD_SIGNIN_ID)
        password_sign_in.click()

    def manage_classes_select(self):
        manage_classes_btn = self.find_element(By.ID, cons.MANAGE_CLASSES)
        manage_classes_btn.click()

    def extract_classes(self):
        courses_texts_list = WebDriverWait(self, 20).until(
            ec.presence_of_element_located((By.ID, cons.COURSE_TEXTS_PANEL))
        )
        parse = ParseCourse(courses_texts_list)
        filecreator = FileCreator(self.semester_path, parse.pull_course_names())
        filecreator.create_semester_file()
        filecreator.create_course_files()
