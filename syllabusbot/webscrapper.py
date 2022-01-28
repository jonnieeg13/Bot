from selenium import webdriver
import os
import syllabusbot.constants as cons


class Courses(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\chromedriver_win32", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] = driver_path
        super(Courses, self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(cons.BASE_URL)

