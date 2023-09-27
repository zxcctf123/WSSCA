import re,json,os


JSON_PATH= os.getcwd()+'/data/file_info.json'


SQLI= [
    r'"{1,3}.*?\'+.*?\'+.*?\'{1,3}"',
    r'(?<!\{)\{[^}]+\}',
    r"\.format\("
]

try:
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    pass
except json.JSONDecodeError as e:
    pass
except UnicodeDecodeError as e:
    pass
else:
    pass


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
    vulnerable=[]
    isVulnerable=False
    for line in range(1, get_nested_dict_length(data[file_path])):
        string = data[file_path][str(line)]
        for sql in SQLI:
            try:
                if re.search(sql,string) and file_path[-2:] == "py":
                    isVulnerable=True
                    temp=[file_path,line,string]
                    vulnerable.append(temp)
                    temp=[]
            except re.error as e:
                pass
    if isVulnerable:
        for v in vulnerable: 
            print(f"The file {vulnerable[0][0]} have been vulnerable to SQL injection attack")
            print(f"Line {v[1]}")
            print(f"Vulnerable code snippet:  {v[2]}\n")
            
            
            
    
