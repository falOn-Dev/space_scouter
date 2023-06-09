import os

import pandas as pd
import config_utils as cu

# Read JSON data into a DataFrame

raw = pd.read_json('cfg/charged_up.json')


# Returns the weights for a given section
def get_weights(section):
    values = []
    cat = raw[section]
    for item in cat.values.flatten():
        if isinstance(item, dict):
            values.extend(item.values())
        elif pd.notnull(item):
            values.append(item)
    return values

# Returns the weight of a specific item
def get_value(section, category, item):

    data = raw[section][category][item]

    return data

