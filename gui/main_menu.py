import customtkinter as ctk
from gui.scoring.scoring_home import App as ScoringApp
from gui.viewer.view_gui import ViewerApp
from gui.weighting.weight_gui import WeightApp

class MainMenu(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("dark")

        self.geometry("300x300")
        self.title("Main Menu")

        self.place_buttons()


    def place_buttons(self):
        score_open = ctk.CTkButton(self, text="Scoring", command=self.open_scoring)
        score_open.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        weight_open = ctk.CTkButton(self, text="Weighting", command=self.open_weighting)
        weight_open.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        viewer_open = ctk.CTkButton(self, text="Viewer", command=self.open_viewer)
        viewer_open.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    def open_scoring(self):
        scoring_app = ScoringApp()
        scoring_app.mainloop()

    def open_weighting(self):
        weight_app = WeightApp()
        weight_app.mainloop()

    def open_viewer(self):
        viewer_app = ViewerApp()
        viewer_app.mainloop()




