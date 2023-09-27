import re,json,os


JSON_PATH= os.getcwd()+'/data/file_info.json'

#text color formats
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
blend_color = "\033[38;2;255;0;127m"
green_text = '\033[92m'
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"
reset_text = "\033[0m"

SQLI= [
    r'"{1,3}.*?\'+.*?\'+.*?\'{1,3}"',
    r'(?<!\{)\{[^}]+\}',
    r"\.format\("
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
    isVulnerable = False
    for line in range (1, get_nested_dict_length(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        for sql in SQLI:
            try:
                if re.search(sql,string) and file_path[-2:] == "py":
                    isVulnerable=True
                    temp=[file_path,line,string]
                    vulnerable.append(temp)
                    
            except re.error as e:
                pass
    if isVulnerable:
        for v in vulnerable: 
            print("🆘🆘" + red + f" The file {vulnerable[0][0]} have been vulnerable to SQL injection attack" + reset_text)
            print(cyan + f"  [*] Line {v[1]}")
            print(f"   [*] Vulnerable code snippet: \n {v[2]}\n" + reset_text)
    else:
        print(green + f'✅ Your {file_path} is not Vulnerable to SQL Injection! 👌😁👌' + reset_text)
            
            
            
    
