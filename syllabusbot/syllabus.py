import re
import dotenv
import os
import canvasapi
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self, class_list=None):
        # # List implementation
        # if class_list is None:
        #     class_list = []
        # self.class_list = class_list
        # # string implementation
        if class_list is None:
            class_list = ''
        self.class_string = class_list
        super().__init__()
        # # List implementation
        # self.url_data_list = []
        # # string implementation
        self.url_data_string = ''

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined return matching href.
                # # List implementation
                # for classes in self.class_list:
                #     if name == "href" and re.search(classes, value):
                #         self.url_data_list.append(value)
                if name == "href" and re.search(self.class_string, value):
                    self.url_data_string = value


def get_syllabus_links(class_list):
    # # List implementation
    # url_list = []
    # # string implementation
    url_string = ''
    dotenv.load_dotenv(dotenv.find_dotenv())
    token = os.environ.get('CANVAS_API_TOKEN')
    baseurl = 'https://uta.instructure.com'
    canvas = canvasapi.Canvas(baseurl, token)
    user = canvas.get_user('self')
    paginated_courses = user.get_courses(enrollment_state='active', include=['syllabus_body'])

    # list implementation
    # regex_modified_list = []
    # for course in class_list:
    #     regex_modified_list.append(course.replace(' ', '.'))
    # # string implementation
    regex_modified_string = class_list.replace(' ', '.')
    syl = []
    for course in paginated_courses:
        if course.syllabus_body:
            syl.append(course.syllabus_body)
    # # list implementation
    # parser = MyHTMLParser(regex_modified_list)
    # # string implementation
    parser = MyHTMLParser(regex_modified_string)
    for s in syl:
        parser.feed(s)
        # # list implementation
        # url_list = parser.url_data_list
        # # string implementation
        url_string = parser.url_data_string
    split_name = url_string.split("/")
    file_name = split_name[-1]
    split_file_type = file_name.split(".")
    file_type = "." + split_file_type[-1]
    return url_string, file_type

# # # TESTER
# myList = ['CSE 3330', 'CSE 3302', 'MATH 3330', 'MATH 2326']
# # list implementation
# download_link_List = get_syllabus_links(myList)
# for link in download_link_List:
#     print(link)
# download_link_string, file_ext = get_syllabus_links(myList[0])
# print(download_link_string, file_ext)
