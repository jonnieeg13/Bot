import re
import dotenv
import os
import canvasapi
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self, class_list=None):
        if class_list is None:
            class_list = ''
        self.class_string = class_list
        super().__init__()
        self.url_data_string = ''

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined return matching href.
                if name == "href" and re.search(self.class_string, value):
                    self.url_data_string = value


def get_syllabus_links(class_list):
    url_string = ''
    dotenv.load_dotenv(dotenv.find_dotenv())
    token = os.environ.get('CANVAS_API_TOKEN')
    baseurl = 'https://uta.instructure.com'
    canvas = canvasapi.Canvas(baseurl, token)
    user = canvas.get_user('self')
    paginated_courses = user.get_courses(enrollment_state='active', include=['syllabus_body'])
    regex_modified_string = class_list.replace(' ', '.')
    syl = []
    for course in paginated_courses:
        if course.syllabus_body:
            syl.append(course.syllabus_body)
    parser = MyHTMLParser(regex_modified_string)
    for s in syl:
        parser.feed(s)
        url_string = parser.url_data_string
    return url_string
