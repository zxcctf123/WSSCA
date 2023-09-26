from modules.utils import *
from modules.detect import *
import argparse,sys



print("""
_ _ _ _____ _____ _____ _____ 
| | | |   __|   __|     |  _  |
| | | |__   |__   |   --|     |
|_____|_____|_____|_____|__|__|
      
By Khanhhnahk1 and H Roy Todd
""")


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example argument parsing')


parser.add_argument('-f', '--file', help='Specify project folter, example: /mnt/d/project/vulnerableflask')


# Automatically display help if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()


if args.file:
    print(f"""[+] Have found files in folder: {args.file}""")
    file_paths=get_all_files(args.file)
    for path in get_all_files(args.file):
        print("[-] "+path)
        # sqli(path)
    if(os.path.exists(JSON_PATH) == False):
        file_info_to_json(file_paths)

#    sqli('/mnt/d/DTU/Capstone1/lab/database.py')
    

        
