import customtkinter as ctk

class MatchInfo(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)

        self.data = data

        self.team_label = ctk.CTkLabel(self, text=f"Team Number: {data[0]}")
        self.team_label.grid(row=0, column=0, sticky="nw", padx=10, pady=2)

        self.match_label = ctk.CTkLabel(self, text=f"Match Number: {data[7]}")
        self.match_label.grid(row=0, column=1, sticky="ne", padx=10, pady=2)

        self.rank_scores()
        self.raw_scores()

    def rank_scores(self):
        row = 1
        self.rank_auto = ctk.CTkLabel(self, text=f"Auto Rank: {self.data[1]}")
        self.rank_auto.grid(row=row, column=0, sticky="nw", padx=10, pady=2)
        row += 1
        self.rank_tele = ctk.CTkLabel(self, text=f"Tele Rank: {self.data[2]}")
        self.rank_tele.grid(row=row, column=0, sticky="nw", padx=10, pady=2)
        row += 1
        self.rank_end = ctk.CTkLabel(self, text=f"Endgame Rank: {self.data[3]}")
        self.rank_end.grid(row=row, column=0, sticky="nw", padx=10, pady=2)

    def raw_scores(self):
        row = 1
        self.raw_auto = ctk.CTkLabel(self, text=f"Auto Score: {self.data[4]}")
        self.raw_auto.grid(row=row, column=1, sticky="ne", padx=10, pady=2)
        row += 1
        self.raw_tele = ctk.CTkLabel(self, text=f"Tele Score: {self.data[5]}")
        self.raw_tele.grid(row=row, column=1, sticky="ne", padx=10, pady=2)
        row += 1
        self.raw_end = ctk.CTkLabel(self, text=f"Endgame Score: {self.data[6]}")
        self.raw_end.grid(row=row, column=1, sticky="ne", padx=10, pady=2)

