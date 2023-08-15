import json
import os

import customtkinter as ctk

from gui.custom_widgets.match_info import MatchInfo
from gui.custom_widgets.match_details import MatchDetails


class ViewerApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("550x440")
        self.title("Viewer")

        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("dark")

        self.grid_columnconfigure(0, weight=12)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.scores = self.extract_keys_from_directory()

        self.matches_frame = ctk.CTkScrollableFrame(self)
        self.matches_frame.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.detail_frame = MatchDetails(self)
        self.detail_frame.grid(row=0, column=1, padx=5, pady=10, sticky="nsw")

        self.add_scores()

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

                        # Append team_number:match_number to the values list
                        values.append(f"{filename[:-5]}")

                        results.append(values)
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON file: {file_path}")

        # Sort results based on team number and match number
        results.sort(key=lambda x: (int(x[-1].split("_")[0]), int(x[-1].split("_")[1])))
        return results

    def add_scores(self):
        for score in self.scores:
            match = MatchInfo(self.matches_frame, score, self.detail_frame)
            match.grid(sticky="ew", padx=(10, 30), pady=10)
