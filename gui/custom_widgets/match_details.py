import json

import customtkinter as ctk


class MatchDetails(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(border_color="#2FA572", border_width=2, corner_radius=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)







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
        self.place_auto()
        self.line_break = ctk.CTkLabel(self, text="------------------------")
        self.line_break.grid(row=4, column=0, sticky="nwes", padx=10, pady=0, columnspan=2)
        self.place_teleop()
        self.line_break2 = ctk.CTkLabel(self, text="------------------------")
        self.line_break2.grid(row=9, column=0, sticky="nwes", padx=10, pady=0, columnspan=2)
        self.place_endgame()



    def place_auto(self):
        self.top_cubes_auto = ctk.CTkLabel(self, text=f"Top Cubes: {self.raw_scores[0][0]}")
        self.top_cubes_auto.grid(row=0, column=0, sticky="nw", padx=10, pady=(3, 1))

        self.mid_cubes_auto = ctk.CTkLabel(self, text=f"Mid Cubes: {self.raw_scores[0][1]}")
        self.mid_cubes_auto.grid(row=1, column=0, sticky="nw", padx=10, pady=1)

        self.top_cones_auto = ctk.CTkLabel(self, text=f"Top Cones: {self.raw_scores[0][2]}")
        self.top_cones_auto.grid(row=0, column=1, sticky="nw", padx=10, pady=1)

        self.mid_cones_auto = ctk.CTkLabel(self, text=f"Mid Cones: {self.raw_scores[0][3]}")
        self.mid_cones_auto.grid(row=1, column=1, sticky="nw", padx=10, pady=1)

        self.hybrid_auto = ctk.CTkLabel(self, text=f"Hybrid: {self.raw_scores[0][4]}")
        self.hybrid_auto.grid(row=2, column=0, sticky="nw", padx=10, pady=1)

        self.docked_auto = ctk.CTkLabel(self, text=f"Docked: {self.raw_scores[0][5]}")
        self.docked_auto.grid(row=2, column=1, sticky="nw", padx=10, pady=1)

        self.engaged_auto = ctk.CTkLabel(self, text=f"Engaged: {self.raw_scores[0][6]}")
        self.engaged_auto.grid(row=3, column=0, sticky="nw", padx=10, pady=1)

        self.exited_auto = ctk.CTkLabel(self, text=f"Exited: {self.raw_scores[0][7]}")
        self.exited_auto.grid(row=3, column=1, sticky="nw", padx=10, pady=1)

    def place_teleop(self):
        self.top_cubes_teleop = ctk.CTkLabel(self, text=f"Top Cubes: {self.raw_scores[1][0]}")
        self.top_cubes_teleop.grid(row=5, column=0, sticky="nw", padx=10, pady=1)

        self.mid_cubes_teleop = ctk.CTkLabel(self, text=f"Mid Cubes: {self.raw_scores[1][1]}")
        self.mid_cubes_teleop.grid(row=5, column=1, sticky="nw", padx=10, pady=1)

        self.top_cones_teleop = ctk.CTkLabel(self, text=f"Top Cones: {self.raw_scores[1][2]}")
        self.top_cones_teleop.grid(row=6, column=0, sticky="nw", padx=10, pady=1)

        self.mid_cones_teleop = ctk.CTkLabel(self, text=f"Mid Cones: {self.raw_scores[1][3]}")
        self.mid_cones_teleop.grid(row=6, column=1, sticky="nw", padx=10, pady=1)

        self.hybrid_teleop = ctk.CTkLabel(self, text=f"Hybrid: {self.raw_scores[1][4]}")
        self.hybrid_teleop.grid(row=7, column=0, sticky="nw", padx=10, pady=1)

        self.docked_teleop = ctk.CTkLabel(self, text=f"Docked: {self.raw_scores[1][5]}")
        self.docked_teleop.grid(row=7, column=1, sticky="nw", padx=10, pady=1)

        self.engaged_teleop = ctk.CTkLabel(self, text=f"Engaged: {self.raw_scores[1][6]}")
        self.engaged_teleop.grid(row=8, column=0, sticky="nw", padx=10, pady=1)

        self.parked_teleop = ctk.CTkLabel(self, text=f"Parked: {self.raw_scores[1][7]}")
        self.parked_teleop.grid(row=8, column=1, sticky="nw", padx=10, pady=1)

    def place_endgame(self):
        self.sustainable_endgame = ctk.CTkLabel(self, text=f"Sustainable Bonus: {self.raw_scores[2][0]}")
        self.sustainable_endgame.grid(row=10, column=0, sticky="nwes", padx=10, pady=0, columnspan=2)

        self.activation_endgame = ctk.CTkLabel(self, text=f"Activation Bonus: {self.raw_scores[2][1]}")
        self.activation_endgame.grid(row=11, column=0, sticky="nwes", padx=10, pady=0, columnspan=2)

        self.cooperation_endgame = ctk.CTkLabel(self, text=f"Cooperation Bonus: {self.raw_scores[2][2]}")
        self.cooperation_endgame.grid(row=12, column=0, sticky="nwes", padx=10, pady=0, columnspan=2)

        self.win_endgame = ctk.CTkLabel(self, text=f"Win Bonus: {self.raw_scores[2][3]}")
        self.win_endgame.grid(row=13, column=0, sticky="nwes", padx=10, pady=0, columnspan=2)