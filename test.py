import chardet
    # with open(file_path, 'r') as file:
    #     lines = file.readlines()

    # file_dict = {}

    # for line_number, line_content in enumerate(lines, start=1):
    #     file_dict[line_number] = line_content.strip()

    # print(file_dict)

# new = {
#     'line2':'c2'
# }
# my_dict = {
#     'file_path': new
# }



# print (my_dict)



with open('/etc/passwd', 'rb') as file:
        raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)['encoding']
print(detected_encoding)

with open('/etc/passwd','r',encoding=detected_encoding) as file:
        print(file.read())