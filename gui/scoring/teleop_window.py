import json

import customtkinter as ctk

from json_handler import JsonHandler
from gui.custom_widgets.numerical_value import NumericalValue
from gui.custom_widgets.checkframe import CheckFrame

import score_handler as sh


class TeleopWindow(ctk.CTkToplevel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.set_default_color_theme("green")

        self.root = root
        self.grab_set()

        self.sub_toplevel = None

        self.json_handler = JsonHandler()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)

        self.nums, self.checks = self.convert_json_to_arrays("teleop")

        self.geometry("550x440")

        self.numerical = NumericalValue(self, 0, self.nums, self)
        self.numerical.grid(row=0, column=4, columnspan=2, rowspan=8, sticky="nsew", padx=10, pady=(10, 0))

        self.checkboxes = CheckFrame(self, 0, self.checks, self)
        self.checkboxes.grid(row=0, column=0, columnspan=2, rowspan=8, sticky="nsew", padx=10, pady=(10, 0))

        self.place_bottom_frame()

    def place_bottom_frame(self):
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.grid(row=8, column=0, columnspan=5, sticky="ew", padx=10, pady=(10, 0))

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)

        self.complete_button = ctk.CTkButton(self.bottom_frame, text="Complete", command=self.send_teleop_scores)
        self.complete_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.score_label = ctk.CTkLabel(self.bottom_frame, text="Score: 0")
        self.score_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

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

    def get_input_values(self):
        nums = self.numerical.get_values()
        checks = self.checkboxes.get_values()
        return nums + checks

    def update_scores(self):
        raw_score = self.get_input_values()
        scores = sh.calculate_scores(raw_score, self.json_handler.get_weights("Tele"))
        self.score_label.configure(text="Score: " + str(scores))

    def send_teleop_scores(self):
        teleop_data = self.get_input_values()
        self.root.teleop_data = teleop_data
        self.destroy()
