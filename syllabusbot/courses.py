from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import syllabusbot.constants as cons
from syllabusbot.parse_course import ParseCourse
from syllabusbot.file_creator import FileCreator
from syllabusbot.uta_course_regex import regex_match
from syllabusbot.folders_database import return_filepath
from selenium.common.exceptions import TimeoutException
import click


class Courses(webdriver.Chrome):

    def __init__(self, teardown=False):
        self.semester = self.get_semester()
        self.semester_path = self.semester_path(self.semester)
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Courses, self).__init__(executable_path=ChromeDriverManager().install(), options=options)
        self.implicitly_wait(15)

    @staticmethod
    def semester_path(season_year):
        formatted_season_year = ' '.join(elem.capitalize() for elem in season_year.split())
        top_folder_name = return_filepath()
        path = os.path.join(top_folder_name, formatted_season_year)
        return path

    def get_semester(self):
        while True:
            self.semester = input("Enter Year and Semester: ")
            if not regex_match(self.semester):
                print('Incorrect Semester Entered')
                continue
            else:
                break
        return self.semester

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

    def check_exists_by_xpath(self, xpath):
        try:
            semester_button = WebDriverWait(self, 20).until(ec.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            return None, False
        return semester_button, True

    def manage_classes_select(self):
        manage_classes_btn = self.find_element(By.ID, cons.MANAGE_CLASSES)
        manage_classes_btn.click()
        semester_xpath = f"//a[contains(text(),'{self.semester}')]"
        semester_button, semester_list_found = self.check_exists_by_xpath(semester_xpath)
        if semester_list_found:
            semester_button.click()

    def extract_classes(self):
        courses_texts_list = WebDriverWait(self, 20).until(
            ec.presence_of_element_located((By.ID, cons.COURSE_TEXTS_PANEL))
        )
        parse = ParseCourse(courses_texts_list)
        course_names = parse.pull_course_names()
        if click.confirm(
                f"Semester courses will be saved to: {self.semester_path}\n" +
                f"Making sub-folders from list: {course_names}\n" +
                "Do you want to Continue?", default=True
        ):
            try:
                file_creator = FileCreator(self.semester_path, course_names)
                file_creator.create_course_files()
            except FileExistsError as e:
                print(e)
        else:
            self.teardown = True

    def bot_wait(self):
        self.implicitly_wait(60)
