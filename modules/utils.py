import os



def get_all_files(folder_path):
    file_paths = []
    
    # Walk through all the directories and files within the given folder
    for root, directories, files in os.walk(folder_path):
        for file in files:
            # Get the absolute path of each file
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    
    return file_paths

def read_file_content(file_paths):
    file_contents = []
    
    """ Try to read the contents of files in array, also try 3 kind of encoding in case that files have differences in encoding types
    """
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                file_contents.append(content)
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='utf-16') as file:
                    content = file.read()
                    file_contents.append(content)
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as file:
                    content = file.read()
                    file_contents.append(content)
    
    return file_contents

