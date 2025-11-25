# import re

# # NOTE: There are only a few tests included, so multiple solutions will work.
# # Feel free to encourage students to find oversights and add tests to this lab!

# name = r""
# name_regex = re.compile(name)

import re

name_regex = re.compile(r"^[A-Z][a-z]*(?:[ '-][A-Z][a-z]*)*$")

phone_regex = re.compile(r"^(?:\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$")

email_regex = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$")
