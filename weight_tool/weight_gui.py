import json

import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.title("Space Scouter Weighting Tool")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)

        with open("scores.json", "r") as f:
            self.scores = json.load(f)

        self.auto_score = self.scores["auto"]
        self.teleop_score = self.scores["teleop"]
        self.endgame_score = self.scores["endgame"]

        self.create_weight_slider()

    def label_config(self, label: ctk.CTkLabel, value):
        value = round(float(value), 3)
        label.configure(text=value)

    def create_weight_slider(self):
        self.top_cube_slider = ctk.CTkSlider(self, from_=0, to=1, orientation="horizontal", command=lambda x: self.label_config(self.top_cube_label, x))
        self.top_cube_slider.grid(row=0, column=4, sticky="w")
        self.top_cube_label = ctk.CTkLabel(self, text="0.5")
        self.top_cube_label.grid(row=0, column=3, sticky="w")





app = App()
app.mainloop()
