import customtkinter as ctk

class WeightApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("550x440")
        self.title("Weighting")

        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("dark")


