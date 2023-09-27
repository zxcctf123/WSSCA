from modules.utils import *
from modules.detect import *
from tqdm import trange
import argparse,sys,time



print(magenta +"""
_ _ _ _____ _____ _____ _____ 
| | | |   __|   __|     |  _  |"""+blend_color+"""
| | | |__   |__   |   --|     |"""+red+"""
|_____|_____|_____|_____|__|__|
"""+green+"""
By Khanhhnahk1 and H Roy Todd
""" + reset_text)


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='\U0001F4D6 Example argument parsing')


parser.add_argument('-f', '--file', help='\U0001F4C2 Specify project folter, '+yellow+'example: /mnt/d/project/vulnerableflask'+reset_text)


# Automatically display help if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()


if args.file:
    print(cyan+f"""[+] Have found files in folder: {args.file}"""+reset_text)
    file_paths=get_all_files(args.file)
    for path in file_paths:
        print("   [-] "+path)
        
    if(os.path.exists(JSON_PATH) == False):
        file_info_to_json(file_paths)
    print("\n[+] Searching for vulnerabilities....")
    # Wait for the user to press Enter
    input("\nYour project has been extracted to "+cyan+"data/file_info.json."+reset_text+"\nPress Enter to continue...")
    
    #loading bar
    for i in trange(100, ncols=80):
        time.sleep(0.01)

    for path in get_all_files(args.file):
        sqli(path)
    

        
