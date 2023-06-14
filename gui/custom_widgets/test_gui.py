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

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)

        self.geometry("550x440")
        self.test = NumericalValue(self, 0, ["Top Cubes: ", "Mid Cubes: ", "Bottom Cubes: ", "Top Cones: ", "Mid Cones: ", "Bottom Cones: "])
        self.test.grid(row=0, column=4, columnspan=2, rowspan=8, sticky="nsew", padx=10, pady=(10, 0))

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.grid(row=8, column=0, columnspan=5, sticky="ew", padx=10, pady=(10, 0))



app = App()
app.mainloop()
