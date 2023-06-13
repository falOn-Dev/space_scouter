import os
import pandas as pd


class JsonHandler:
    def __init__(self):
        self.prefix = ""

        # if os.getenv('PYCHARM_HOSTED'):
        #     self.prefix = ""
        # else:
        #     self.prefix = "../"
        self.raw = None
        self.read_json("charged_up.json")

    def read_json(self, filepath):
        self.raw = pd.read_json(self.prefix+"cfg/"+filepath)
        print("Config changed to: " + filepath)

    def get_weights(self, section):
        values = []
        cat = self.raw[section]
        for item in cat.values.flatten():
            if isinstance(item, dict):
                values.extend(item.values())
            elif pd.notnull(item):
                values.append(item)
        return values

    def list_configs(self):
        files = []
        with os.scandir(self.prefix+"cfg") as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry.name)

        return files

    def get_value(self, section, category, item):
        data = self.raw[section][category][item]
        return data
