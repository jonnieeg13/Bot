import re


def course_regex(text_in):
    pattern = re.compile(r"^[a-zA-Z]+\s?[0-9]{4}")
    return pattern.search(text_in).group()


def regex_match(text_in):
    pattern = re.match(r"^[a-zA-Z]+\s?[0-9]{4}", text_in)
    # pattern = re.match(r"\w{0,6}\s[0-9]{4}", text_in)
    return bool(pattern)
