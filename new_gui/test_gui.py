import json

import customtkinter as ctk

from new_gui.custom_widgets.checkframe import CheckFrame
from new_gui.custom_widgets.numerical_value import NumericalValue
from json_handler import JsonHandler
import score_handler as sh

from new_gui.auto_window import AutoWindow
from new_gui.teleop_window import TeleopWindow


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.set_default_color_theme("green")

        self.j_hand = JsonHandler()
        self.configs = None

        self.extras = self.get_checks()




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


        self.geometry("550x440")

        self.auto_data = []
        self.teleop_data = []

        self.windows_frame = ctk.CTkFrame(self)
        self.windows_frame.grid(row=0, column=4, columnspan=2, rowspan=8, sticky="nsew", padx=10, pady=(10, 0))

        self.check_frame = CheckFrame(self, 0, self.extras, self)
        self.check_frame.grid(row=0, column=0, columnspan=2, rowspan=8, sticky="nsew", padx=10, pady=(10, 0))

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.grid(row=8, column=0, columnspan=5, sticky="ew", padx=10, pady=(10, 10))

        self.update_configs()
        self.place_bottom_frame()
        self.place_windows_frame()

        self.windows_frame.grid_columnconfigure(0, weight=1)


        self.toplevel_window = None



    def place_windows_frame(self):


        self.auto_button = ctk.CTkButton(self.windows_frame, text="Autonomous", command=lambda: self.open_toplevel(AutoWindow))
        self.auto_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.teleop_button = ctk.CTkButton(self.windows_frame, text="Teleop", command=lambda: self.open_toplevel(TeleopWindow))
        self.teleop_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def open_toplevel(self, window):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = window(self, self)


    def place_bottom_frame(self):

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)

        self.team_number = ctk.CTkEntry(self.bottom_frame, placeholder_text="Team Number")
        self.team_number.grid(row=0, column=0, padx=10, pady=5, sticky="sw")

        self.calculate_final = ctk.CTkButton(self.bottom_frame, text="Calculate Final Score", command=lambda: sh.create_score_file(self.team_number.get(), self.auto_data, self.teleop_data, self.get_check_value()))
        self.calculate_final.grid(row=1, column=0, padx=10, pady=10, sticky="sw")

        self.config_selector = ctk.CTkOptionMenu(self.bottom_frame, values=self.configs, command=lambda event: self.j_hand.read_json(self.config_selector.get()))
        self.config_selector.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        self.config_check = ctk.CTkButton(self.bottom_frame, text="Check Configs", command=lambda : print(self.j_hand.raw))
        self.config_check.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        self.test_scores = ctk.CTkButton(self.bottom_frame, text="Test Scores", command=self.print_auto_scores)
        self.test_scores.grid(row=2, column=0, padx=10, pady=10, sticky="sw")

    def update_configs(self):
        self.configs = self.j_hand.list_configs()

    def get_check_value(self):
        return self.check_frame.get_values()

    def get_checks(self):
        with open("cfg/gui_config.json", "r") as file:
            data = json.load(file)

        data_array = data["extra"]
        return data_array

    def update_scores(self):
        print("ill fix this later")


    def print_auto_scores(self):
        print(self.teleop_data)