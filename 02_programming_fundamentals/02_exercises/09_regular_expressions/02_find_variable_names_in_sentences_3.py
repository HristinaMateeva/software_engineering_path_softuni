import re

pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"

data = input()

result = [el.group() for el in re.finditer(pattern, data)]

print(','.join(result))
