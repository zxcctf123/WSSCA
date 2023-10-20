import os,chardet,json


def get_all_files(folder_path):
    file_paths = []
    
    # Walk through all the directories and files within the given folder
    for root, directories, files in os.walk(folder_path):
        for file in files:
            # Get the absolute path of each file
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    
    return file_paths

"""
return the encoding type of the specific file
Param:
+ file_path : str (path of a file)
"""
def detected_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)['encoding']
    return detected_encoding


""" 
    Try to read the contents of files in array, also try 3 kind of encoding in case that files have differences in encoding types
"""
def read_file_content(file_path):
    file_dict = {}

    
    try:
        with open(file_path, 'r', encoding=detected_encoding(file_path)) as file:
            lines = file.readlines()

            for line_number, line_content in enumerate(lines, start=1):
                file_dict[line_number] = line_content.strip()

    except UnicodeDecodeError:
        pass

    return file_dict

def file_info_to_json(file_paths):
    file_info={}
    for path in file_paths:
        temp={
            path:read_file_content(path)
        }
        file_info.update(temp)
    with open('data/file_info.json','w') as file:
        json.dump(file_info,file,indent=4)
