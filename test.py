import re
import json 

format_string_pattern = r'(?<!\{)\{[^}]+\}'

concat_string_pattern = r'"{1,3}.*?\'+.*?\'+.*?\'{1,3}"'

string=open('/mnt/d/DTU/Capstone1/lab/database.py', 'r').read()

with open('/mnt/d/DTU/Capstone1/lab/database.py', 'r') as file:
    lines = file.readlines()
    # print(lines)

file_dict = {}

for line_number, line_content in enumerate(lines, start=1):
    file_dict[line_number] = line_content.strip()



# matches = re.findall(concat_string_pattern, string)
# for match in matches:
#     print(match)
# if matches:
#     print("Potential format string usage detected!")
#     print("Matched format string(s):", matches)
# else:
#     print("No potential format string usage detected.")

# print(code_snippet)
# code_snippet = '"""Select username,password,name,id from users where username=\'\"\"\"+user+\"\"\"\' and password=\'\"\"\"+passwd+"""\''



