import re,json,os


JSON_PATH= os.getcwd()+'/data/file_info.json'

#text color formats
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
blend_color = "\033[38;2;128;0;255m"
green_text = '\033[92m'
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
reset_text = "\033[0m"

SQLI = [
    r'"{1,3}.*?\'+.*?\'+.*?\'{1,3}"',
    r'(?<!\{)\{[^}]+\}',
    r"\.format\("
]

XSS = [
    r"\{\!(.*?)\!\}",  
    r"{{(.*?)\s*\|\s*safe\s*}}"
]



PICKLE = [
    r'\bpickle\.loads\([^)]*\)'
]

def json_data():
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
    return data


"""
param:
dictionary: dictionary
"""
def get_ndict_len(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, dict):
            count += get_ndict_len(value)
        else:
            count += 1

    return count+1

# Vulnerabilities detecting function
# It returns the code of the vulnerability
# 1 for sqli
# 2 for xss
# 3 for unsecure deserialize
def isVulnerable(file_path):
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        for sql in SQLI:
            try:
                if re.search(sql,string) and file_path[-2:] == "py":
                    return 1
            except re.error as e:
                pass
        for xss in XSS:
            try:
                if re.search(xss,string) and file_path[-4:] == "html":
                    return 2
            except re.error as e:
                pass
        for pickle in PICKLE:
            try:
                if re.search(pickle,string) and file_path[-2:] == "py":
                    return 3
            except re.error as e:
                pass  
    return 0

def vuln(file_path, whichVuln):
    vulnerable=[]
    match whichVuln:
        case 1 : attack = "SQL Injection. Use Parameterized query and Prepared Statement instead."
        case 2 : attack = "XSS. Remember to escape dangerous output character."
        case 3 : attack = "Unsecure Deserialize. Please use a safer serialize format such as json"
    vulnerable.append("🆘🆘" + red + f" The file {file_path} have been vulnerable to "+ attack + reset_text)
    # print("🆘🆘" + red + f" The file {vulnerable[0][0]} have been vulnerable to "+ attack +" attack" + reset_text)
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        if whichVuln == 1:
            for sql in SQLI:
                try:
                    if re.search(sql,string) and file_path[-2:] == "py":
                        temp=[file_path,line,string]
                        vulnerable.append(temp)
                except re.error as e:
                    pass
        if whichVuln == 2:
            for xss in XSS:
                try:
                    if re.search(xss,string) and file_path[-4:] == "html":
                        temp=[file_path,line,string]
                        vulnerable.append(temp)
                except re.error as e:
                    pass
        if whichVuln == 3:
            for pickle in PICKLE:
                try:
                    if re.search(pickle,string) and file_path[-2:] == "py":
                        temp=[file_path,line,string]
                        vulnerable.append(temp)
                except re.error as e:
                    pass

    return vulnerable
