import os
import pandas as pd
import config_utils as cu


class JsonHandler:
    def __init__(self):
        self.raw = None

    def read_json(self, filepath):
        self.raw = pd.read_json("cfg/"+filepath)

    def get_weights(self, section):
        values = []
        cat = self.raw[section]
        for item in cat.values.flatten():
            if isinstance(item, dict):
                values.extend(item.values())
            elif pd.notnull(item):
                values.append(item)
        return values

    def get_value(self, section, category, item):
        data = self.raw[section][category][item]
        return data
