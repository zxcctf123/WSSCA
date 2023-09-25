from modules.utils import *
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
    print("""[+] Have found files in folder""")
    for path in get_all_files(args.file):
        print("[-] "+path)
    print("""[+] Start searching for sink in project""")
    