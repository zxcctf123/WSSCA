import json

#model dictionary
temp = {
    'file_path' : {
        'line' : 'content',
    }
}

temp2 = {
    'file_p':{
        'l' : 'c'
    }
}

#data is the dictionary contains the found vulnerables
def add_data_to_json(data, filename):
    try:
        with open(filename, "r+") as file:
            # Load existing JSON data
            json_data = json.load(file)

            # Append the new data to the existing JSON
            if isinstance(json_data, dict):
                json_data.update(data)
            else:
                raise TypeError("The existing JSON data should be a list.")

            # Move the file cursor to the beginning
            file.seek(0)

            # Write the updated JSON data
            json.dump(json_data, file, indent=4)

        print(f"The data has been added to {filename}.")

    #if file does not exist, create new one then add the data directly    
    except FileNotFoundError:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"The data has been exported to {filename}.")

add_data_to_json(temp2, 'data/vul.json')