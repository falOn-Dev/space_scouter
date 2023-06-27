import customtkinter as ctk
from gui.scoring.test_gui import App as ScoringApp

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

    def open_scoring(self):
        scoring_app = ScoringApp()
        scoring_app.mainloop()



