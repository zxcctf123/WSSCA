from modules.utils import *
from modules.detect import *
from tqdm import trange
import argparse,sys,time,atexit



print(magenta +"""
_ _ _ _____ _____ _____ _____ 
| | | |   __|   __|     |  _  |"""+blend_color+"""
| | | |__   |__   |   --|     |"""+blue+"""
|_____|_____|_____|_____|__|__|
"""+green+"""
By Khanhhnahk1 and H Roy Todd
""" + reset_text)


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='\U0001F4D6'+cyan+' Example argument parsing'+reset_text)


parser.add_argument('-f', '--file', help='\U0001F4C2 Specify project folter, '+yellow+'example: /mnt/d/project/vulnerableflask'+reset_text)


# Automatically display help if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    

args = parser.parse_args()


if args.file:
    print(cyan+f"""[+] Have found files in folder: {args.file}"""+reset_text)
    file_paths=get_all_files(args.file)
    for path in file_paths:
        print("   [-] "+path)
        
    if(os.path.exists(JSON_PATH) == False):
        file_info_to_json(file_paths)
    
    # Wait for the user to press Enter
    input("\nYour project has been extracted to "+cyan+"data/file_info.json."+reset_text+"\nPress Enter to continue...")

    #Detect and print out vulnerabilities
    isVuln = False
    vulnerable_files = []
    
    vulvs = ''
    for i in trange(len(file_paths), desc="Detecting"):
        file_path = file_paths[i]
        # whichvulv = isVulnerable(file_path)
        vulvs = isVulnerable(file_path)
        # if whichvulv != 0:
    if vulvs != '':
        isVuln = True
        vulnerable_files.append(vuln(file_path, vulvs))
        # vulnerable_files.append(vuln(file_path, whichvulv))
    if not isVuln:
        print(green + '\n✅ Your project is not vulnerable! 👌😁👌' + reset_text)
    else:
        for vulnerable_file in vulnerable_files:
            print(vulnerable_file[0])
            for v in vulnerable_file:
                print(cyan + f"  [*] Line {v[1]}")
                print(f"   [*] Vulnerable code snippet: \n {v[2]}\n" + reset_text)

def delete_json_file():
    os.remove(JSON_PATH)
    print('Deleted ' + cyan + 'application temporary data. CYA!' + reset_text)

atexit.register(delete_json_file)