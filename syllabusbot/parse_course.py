from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import syllabusbot.constants as cons
from selenium.webdriver.remote.webelement import WebElement
from syllabusbot.uta_course_regex import course_regex


class ParseCourse:
    def __init__(self, courses_texts_list: WebElement):
        self.courses_texts_list = courses_texts_list
        self.course_names = self.pull_course_box()

    def pull_course_box(self):
        courses_texts = WebDriverWait(self.courses_texts_list, 20).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, cons.COURSE_TEXTS_CLASS))
        )
        return courses_texts

    def pull_course_names(self):
        course_list = []
        for course_text in self.course_names:
            course_list.append(
                str(course_text.find_element(By.CLASS_NAME, cons.INDIVIDUAL_COURSE_CLASS).get_attribute("text").strip())
            )
        # print(course_list)
        for items in range(len(course_list)):
            course_list[items] = course_regex(course_list[items])
        # print(course_list)
        return course_list
    # ALTERNATE WAY TO GET COURSE NAME
    # course_list = []
    # courses_texts = WebDriverWait(self, 20).until(
    # ec.presence_of_all_elements_located((By.XPATH, cons.COURSE_TEXT))
    # )
    # for course_text in courses_texts:
    #     course_list.append(str(course_text.get_attribute("text")))
    # print(course_list)
