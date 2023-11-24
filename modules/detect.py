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
    r"{!(.*?)!}",
    r"{{(.*?)\s*\|\s*safe\s*}}"
]

SSRF = [
    r'urlopen\s*\(\s*[\'"](http|https|ftp)://'
]

Deserialize = [
    r'pickle.load\('
]

# WeakSecret = [
#     r''
# ]

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

def unique(str):
    for i in range(1, len(str)-1):
        if (str[i]==str[i+1]):
            str[i]=''
    return str

# Vulnerabilities detecting function
# It returns the code of the vulnerability
# 1 for sqli
# 2 for xss
# 3 for ssrf
# 4 for desirialize
# 5 for JWT
def isVulnerable(file_path):
    vulvs = ''
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        # for sql in SQLI:
        #     try:
        #         if re.search(sql,string) and file_path[-2:] == "py":
        #             return 1
        #     except re.error as e:
        #         pass
        # for xss in XSS:
        #     try:
        #         if re.search(xss,string) and file_path[-4:] == "html":
        #             return 2
        #     except re.error as e:
        #         pass
        if (file_path[-2:] == 'py'):
            for sql in SQLI:
                if (re.search(sql, string)):
                    vulvs+='1'
                    break
            for ssrf in SSRF:
                if (re.search(ssrf, string)):
                    vulvs+='3'
                    break
            for dese in Deserialize:
                if (re.search(dese, string)):
                    vulvs+='4'
                    break
            # for jwt in WeakSecret:
            #     if (re.search(jwt, string)):
            #         vulvs.append('5')
            #         break
        for xss in XSS:
            if file_path[-4:] == 'html' and re.search(xss,string):
                vulvs+='2'
                break
    vulvs=unique(vulvs)
    return vulvs

vulnType = {
    '1': 'SQL Injection',
    '2': 'XSS',
    '3': 'SSRF',
    '4': 'Deserialize',
    '5': 'Weak secret key'
}

def sqli (vulnerable, file_path):
    vulnerable.append("🆘🆘" + red + f" The file {file_path} have been vulnerable to SQL Injection attack" + reset_text)
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        for sql in SQLI:
            if re.search(sql,string):
                temp=[file_path,line,string]
                vulnerable.append(temp)
    return vulnerable

def xss (vulnerable, file_path):
    vulnerable.append("🆘🆘" + red + f" The file {file_path} have been vulnerable to XSS attack" + reset_text)
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        for xss in XSS:
            if re.search(xss,string) and file_path[-2:] == "html":
                temp=[file_path,line,string]
                vulnerable.append(temp)
    return vulnerable

def ssrf (vulnerable, file_path):
    vulnerable.append("🆘🆘" + red + f" The file {file_path} have been vulnerable to SSRF attack" + reset_text)
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        for ssrf in SSRF:
            if re.search(ssrf,string):
                temp=[file_path,line,string]
                vulnerable.append(temp)
    return vulnerable

def deserialize (vulnerable, file_path):
    vulnerable.append("🆘🆘" + red + f" The file {file_path} have been vulnerable to Deserialize attack" + reset_text)
    for line in range (1, get_ndict_len(json_data()[file_path])):
        string = json_data()[file_path][str(line)]
        for dese in Deserialize:
            if re.search(dese,string):
                temp=[file_path,line,string]
                vulnerable.append(temp)
    return vulnerable

# def weakSecr (vulnerable, file_path):
#     vulnerable.append("🆘🆘" + red + f" The file {file_path} is contained Weak Secret Variables" + reset_text)
#     for line in range (1, get_ndict_len(json_data()[file_path])):
#         string = json_data()[file_path][str(line)]
#         for jwt in WeakSecret:
#             if re.search(jwt,string):
#                 temp=[file_path,line,string]
#                 vulnerable.append(temp)
#     return vulnerable

# def vuln(file_path, whichVuln):
def vuln(file_path, vulvs):
    vulnerable=[]
    # # attack = vulnType[whichVuln]
    # match whichVuln:
    #     case 1 : attack = "SQL Injection"
    #     case 2 : attack = "XSS"
    #     case 3 : attack = "CSRF"
    # vulnerable.append("🆘🆘" + red + f" The file {file_path} have been vulnerable to "+ attack +" attack" + reset_text)
    # for line in range (1, get_ndict_len(json_data()[file_path])):
    #     string = json_data()[file_path][str(line)]
    #     if whichVuln == 1:
    #         for sql in SQLI:
    #             try:
    #                 if re.search(sql,string) and file_path[-2:] == "py":
    #                     temp=[file_path,line,string]
    #                     vulnerable.append(temp)
    #             except re.error as e:
    #                 pass
    #     if whichVuln == 2:
    #         for xss in XSS:
    #             try:
    #                 if re.search(xss,string) and file_path[-4:] == "html":
    #                     temp=[file_path,line,string]
    #                     vulnerable.append(temp)
    #             except re.error as e:
    #                 pass
    # return vulnerable
    
    for type in vulvs:
        match type:
            case '1' : vulnerable = sqli(vulnerable, file_path)
            case '2' : vulnerable = xss(vulnerable, file_path)
            case '3' : vulnerable = ssrf(vulnerable, file_path)
            case '4' : vulnerable = deserialize(vulnerable, file_path)
            # case 5 : vulnerable = weakSecr(vulnerable, file_path)
    return vulnerable
