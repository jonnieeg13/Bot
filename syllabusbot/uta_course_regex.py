import re


def course_regex(text_in):
    pattern = re.compile(r"^[a-zA-Z]+\s?[0-9]{4}")
    return pattern.search(text_in).group()
