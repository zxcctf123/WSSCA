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
    r'<script\b[^>]*>.*?</script>',
    r'<[^>]+on[^=]+=[\'"].*?[\'"]\s*[^>]*>',
    r'javascript:',
    r'eval\('
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

def isSqli(file_paths):
    for file_path in file_paths:
        for line in range (1, get_ndict_len(json_data()[file_path])):
            string = json_data()[file_path][str(line)]
            for sql in SQLI:
                try:
                    if re.search(sql,string) and file_path[-2:] == "py":
                        return True
                except re.error as e:
                    pass
    return False

"""
whichVuln is used to optimize the code for scanning
0 for sqli
1 for xss
2 for ssrf
...
"""

def sqli(file_path, whichVuln):
    vulnerable=[]
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        for sql in SQLI:
            try:
                ###########################
                if re.search(sql,string) and file_path[-2:] == "py":
                    temp=[file_path,line,string]
                    vulnerable.append(temp)
            except re.error as e:
                pass
    if (len(vulnerable) != 0):
        match whichVuln:
            case 0 : attack = "SQL Injection"
            case 1 : attack = "XSS"
            case 2 : attack = "SSRF"
        print("🆘🆘" + red + f" The file {vulnerable[0][0]} have been vulnerable to "+ attack +" attack" + reset_text)
    for v in vulnerable: 
        print(cyan + f"  [*] Line {v[1]}")
        print(f"   [*] Vulnerable code snippet: \n {v[2]}\n" + reset_text)
            

def isXSS(file_paths):
    for file_path in file_paths:
        for line in range (1, get_ndict_len(json_data()[file_path])):
            string = json_data()[file_path][str(line)]
            for xss in XSS:
                try:
                    if re.search(xss,string) and file_path[-4:] == "html":
                        return True
                except re.error as e:
                    pass
    return False
            
