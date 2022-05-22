import re
import dotenv
import os
import canvasapi
from html.parser import HTMLParser

myList = ['CSE 3330', 'CSE 3302', 'MATH 3330', 'MATH 2326']


class MyHTMLParser(HTMLParser):
    def __init__(self, class_list=None):
        if class_list is None:
            class_list = []
        self.class_list = class_list
        super().__init__()

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, print it.
                # if name == "href":
                for classes in self.class_list:
                    if name == "href" and re.search(classes, value):
                        print(name, "=", value)


def get_syllabus_links(class_list):

    dotenv.load_dotenv(dotenv.find_dotenv())
    token = os.environ.get('CANVAS_API_TOKEN')
    baseurl = 'https://uta.instructure.com'
    canvas = canvasapi.Canvas(baseurl, token)
    user = canvas.get_user('self')
    paginated_courses = user.get_courses(enrollment_state='active', include=['syllabus_body'])

    regex_modified_list = []
    for course in class_list:
        regex_modified_list.append(course.replace(' ', '.'))

    syl = []
    for course in paginated_courses:
        if course.syllabus_body:
            syl.append(course.syllabus_body)

    parser = MyHTMLParser(regex_modified_list)
    for s in syl:
        parser.feed(s)


get_syllabus_links(myList)
