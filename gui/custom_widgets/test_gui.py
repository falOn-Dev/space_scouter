import customtkinter as ctk
from gui.custom_widgets.numerical_value import NumericalValue


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.geometry("550x440")
        self.test = NumericalValue(self, 0, "Top Cubes: ")
        self.test.grid(column=4, row=0, padx=10, pady=10, sticky="nsew")  # Adjusted column and added padding


app = App()
app.mainloop()
