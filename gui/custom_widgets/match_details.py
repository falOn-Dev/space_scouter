import json

import customtkinter as ctk


class MatchDetails(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(border_color="#2FA572", border_width=2, corner_radius=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)


        self.data = None
        self.raw_scores = None

    def set_data(self, data):
        self.data = data

        self.raw_scores = []

        with open(f"scores/{data[8]}.json", 'r') as file:
            self.raw_data = json.load(file)

            self.raw_scores.append(self.raw_data["raw_scores"]["auto"])
            self.raw_scores.append(self.raw_data["raw_scores"]["teleop"])
            self.raw_scores.append(self.raw_data["raw_scores"]["endgame"])

        self.update_data()

    def update_data(self):
        if self.raw_scores is None:
            return

        self.auto_score = ctk.CTkLabel(self, text=f"Auto Score: {self.raw_scores[0]}")
        self.auto_score.grid(row=0, column=0, sticky="nw", padx=10, pady=2)

        self.tele_score = ctk.CTkLabel(self, text=f"Tele Score: {self.raw_scores[1]}")
        self.tele_score.grid(row=1, column=0, sticky="nw", padx=10, pady=2)

        self.end_score = ctk.CTkLabel(self, text=f"Endgame Score: {self.raw_scores[2]}")
        self.end_score.grid(row=2, column=0, sticky="nw", padx=10, pady=2)