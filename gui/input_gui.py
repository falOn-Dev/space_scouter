from functools import partial
import customtkinter as ctk
from gui.auto_input_gui import AutoInputWindow
from gui.teleop_input_gui import TeleopInputWindow
import score_handler as score
from json_handler import JsonHandler


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configs = None
        self.geometry("500x400")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.title("Space Scouter")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(999, weight=1)
        self.grid_rowconfigure(998, weight=1)

        self.endgame_data = []
        self.j_hand = JsonHandler()

        self.endgame_box()
        self.pages()
        self.output()

        self.toplevel_window = None

        self.auto_data = []
        self.teleop_data = []


        self.is_calculating_score = False

        self.update_configs()

    def update_configs(self):
        self.configs = self.j_hand.list_configs()
        self.config_selector.configure(values=self.configs)

    def pages(self):
        self.open_auto = ctk.CTkButton(self, text="Input Auto Score",
                                       command=lambda: self.open_toplevel(AutoInputWindow))
        self.open_auto.grid(row=0, column=0, padx=5, pady=(10,0), sticky="ew")

        self.auto_score = ctk.CTkLabel(self, text="Auto Score: 0", anchor="n")
        self.auto_score.grid(row=1, column=0, sticky="ew", padx=10, pady=0)

        self.open_teleop = ctk.CTkButton(self, text="Input Tele Score",
                                         command=lambda: self.open_toplevel(TeleopInputWindow))
        self.open_teleop.grid(row=0, column=1, padx=5, pady=(10,0), sticky="ew")

        self.teleop_score = ctk.CTkLabel(self, text="Teleop Score: 0", anchor="n")
        self.teleop_score.grid(row=1, column=1, sticky="ew", padx=10, pady=0)

    def open_toplevel(self, window):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = window(self, self)

    def endgame_box(self):
        self.endgame_frame = ctk.CTkFrame(master=self)
        self.endgame_frame.grid(row=0, column=3, rowspan=2, padx=10, pady=10, sticky="nsew")
        # Add checkboxes and labels to the endgame_frame
        self.checkbox1 = ctk.CTkCheckBox(self.endgame_frame, text="Sustain")
        self.checkbox1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.checkbox2 = ctk.CTkCheckBox(self.endgame_frame, text="Coop")
        self.checkbox2.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.checkbox3 = ctk.CTkCheckBox(self.endgame_frame, text="Active")
        self.checkbox3.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.checkbox4 = ctk.CTkCheckBox(self.endgame_frame, text="Win")
        self.checkbox4.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    def settings_box(self):
        self.settings_frame = ctk.CTkFrame(master=self)
        self.settings_frame.grid(row=4, column=3, rowspan=2, padx=10, pady=10, sticky="nsew")

    def update_scores(self):
        self.auto_score.configure(text=f"Auto Score: {self.auto_score_val}")
        self.teleop_score.configure(text=f"Teleop Score: {self.teleop_score_val}")

    def output(self):
        self.team_number = ctk.CTkEntry(self, placeholder_text="Team Number")
        self.team_number.grid(row=999, column=0, padx=10, pady=5, sticky="sw")

        def calculate_score():

            #self.j_hand.read_json(self.config_selector.get())

            # Check if the function is already running
            if self.is_calculating_score:
                return

            # Set the flag variable to indicate that the calculation is in progress
            self.is_calculating_score = True

            self.endgame_data.append(self.checkbox1.get())
            self.endgame_data.append(self.checkbox2.get())
            self.endgame_data.append(self.checkbox3.get())
            self.endgame_data.append(self.checkbox4.get())

            score.create_score_file(
                int(self.team_number.get()),
                self.auto_data,
                self.teleop_data,
                self.endgame_data
            )

            # Reset the flag variable after the calculation is done
            self.is_calculating_score = False

        self.calculate_final = ctk.CTkButton(self, text="Calculate Score", command=calculate_score)
        self.calculate_final.grid(row=1000, column=0, padx=20, pady=(5, 20), sticky="sw")

        self.config_selector = ctk.CTkOptionMenu(self, values=self.configs, command=lambda event: self.j_hand.read_json(self.config_selector.get()))
        self.config_selector.grid(row=1000, column=3, padx=10, pady=5, sticky="se")

        self.check_config = ctk.CTkButton(self, text="Check Config", command=lambda: print(self.j_hand.raw))
        self.check_config.grid(row=999, column=3, padx=10, pady=5, sticky="se")

        self.config_selector.set("charged_up.json")
