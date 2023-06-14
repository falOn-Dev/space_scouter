import customtkinter as ctk
from new_gui.custom_widgets.numerical_value import NumericalValue
from json_handler import JsonHandler


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.j_hand = JsonHandler()
        self.configs = None

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
        self.bottom_frame.grid(row=8, column=0, columnspan=5, sticky="ew", padx=10, pady=(10, 10))

        self.update_configs()
        self.place_bottom_frame()



    def place_bottom_frame(self):

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)

        self.team_number = ctk.CTkEntry(self.bottom_frame, placeholder_text="Team Number")
        self.team_number.grid(row=0, column=0, padx=10, pady=5, sticky="sw")

        self.calculate_final = ctk.CTkButton(self.bottom_frame, text="Calculate Final Score")
        self.calculate_final.grid(row=1, column=0, padx=10, pady=10, sticky="sw")

        self.config_selector = ctk.CTkOptionMenu(self.bottom_frame, values=self.configs, command=lambda event: self.j_hand.read_json(self.config_selector.get()))
        self.config_selector.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        self.config_check = ctk.CTkButton(self.bottom_frame, text="Check Configs", command=lambda : print(self.j_hand.raw))
        self.config_check.grid(row=1, column=1, padx=10, pady=10, sticky="e")

    def update_configs(self):
        self.configs = self.j_hand.list_configs()

