import json

import customtkinter as ctk

class TeleopWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grab_set()

        self.geometry("550x440")
        self.title("Teleop")

    def convert_json_to_arrays(self, category):
        nums_array = []
        checks_array = []

        with open("cfg/gui_config.json") as file:
            json_data = json.load(file)

        if category in json_data:
            category_data = json_data[category]
            if "num" in category_data:
                nums_array = category_data["num"]
            if "checks" in category_data:
                checks_array = category_data["checks"]

        return nums_array, checks_array
