import json
import os

import customtkinter as ctk

from gui.custom_widgets.match_info import MatchInfo


class ViewerApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("550x440")
        self.title("Viewer")

        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("dark")

        scores = self.extract_keys_from_directory()

        self.print_scores = ctk.CTkButton(self, text="Print Scores", command=lambda : print(scores[0]))
        self.print_scores.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.info_test = MatchInfo(self, scores[0])
        self.info_test.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def extract_keys_from_directory(self):
        results = []

        directory = "scores/"
        keys = ["team_number", "auto", "teleop", "endgame", "match_number"]

        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)

                with open(file_path, 'r') as file:
                    try:
                        data = json.load(file)
                        values = []

                        def find_values(obj):
                            if isinstance(obj, dict):
                                for key, value in obj.items():
                                    if key == "raw_scores":
                                        continue  # Skip the entire "raw_scores" object
                                    elif key in keys:
                                        values.append(value)
                                    elif isinstance(value, (dict, list)):
                                        find_values(value)
                            elif isinstance(obj, list):
                                for item in obj:
                                    find_values(item)

                        find_values(data)
                        results.append(values)
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON file: {file_path}")

        return results

