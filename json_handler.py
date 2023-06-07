import pandas as pd

# Read JSON data into a DataFrame
raw = pd.read_json('charged_up.json')



def get_weights(section):
    values = []
    cat = raw[section]
    for item in cat.values.flatten():
        if isinstance(item, dict):
            values.extend(item.values())
        elif pd.notnull(item):
            values.append(item)
    return values

def get_value(section, category, item):

    data = raw[section][category][item]

    return data

