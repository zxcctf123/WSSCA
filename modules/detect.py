import re,json,os


JSON_PATH= os.getcwd()+'/data/file_info.json'


SQLI= [
    r'"{1,3}.*?\'+.*?\'+.*?\'{1,3}"',
       r'(?<!\{)\{[^}]+\}'
]

"""
param:
dictionary: dictionary
"""
def get_nested_dict_length(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, dict):
            count += get_nested_dict_length(value)
        else:
            count += 1

    return count+1

def sqli(file_path):

    try:
        with open(JSON_PATH, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File 'file_info.json' not found.")
    except json.JSONDecodeError as e:
        pass
    except UnicodeDecodeError as e:
        pass
    else:
        for line in range(1, get_nested_dict_length(data[file_path])):
            string = data[file_path][str(line)]
            for sql in SQLI:
                try:
                    if re.match(string, sql) and len(string)>5 :
                        print(f"""Vulnerable to SQL Injection in file: {file_path} \n line : {line} \n
                                """)
                except re.error as e:
                    pass
                
            
    
