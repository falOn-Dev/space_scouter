import customtkinter as ctk

class EndgameInputWindow(ctk.CTkToplevel):

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("600x500")
        self.title("Endgame Input")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")


        self.app = app

