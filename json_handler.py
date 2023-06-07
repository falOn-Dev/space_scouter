import pandas as pd

# Read JSON data into a DataFrame
raw = pd.read_json('charged_up.json')

def get_value(section, category, item):

    data = raw[section][category][item]


    result = {
        "Result": data,
    }
    return data

# Call the function
