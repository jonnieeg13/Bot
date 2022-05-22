import re

import dotenv
import os
import canvasapi
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, print it.
                # if name == "href":
                if name == "href" and re.search(r"CSE.3302", value):
                    print(name, "=", value)


dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://uta.instructure.com'

canvas = canvasapi.Canvas(BASEURL, TOKEN)

user = canvas.get_user('self')

paginated_courses = user.get_courses(enrollment_state='active', include=['syllabus_body', 'term', 'total_students'])
# courses = [course.attributes for course in paginated_courses]
syl = []
for course in paginated_courses:
    # print(course.total_students)
    if course.syllabus_body:
        # print(course.syllabus_body)
        syl.append(course.syllabus_body)

# print(courses[0])
# print(syl[0])
# # for string in syl:
#     print(string)
parser = MyHTMLParser()
parser.feed(syl[0])
