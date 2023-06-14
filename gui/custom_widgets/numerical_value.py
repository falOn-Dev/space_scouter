import customtkinter as ctk


class NumericalValue(ctk.CTkFrame):
    def __init__(self, master, row, title):
        super().__init__(master)
        self.grid_columnconfigure("0", weight=1)
        self.grid_columnconfigure("1", weight=1)
        self.grid_columnconfigure("2", weight=1)
        self.grid_columnconfigure("3", weight=1)
        self.grid_columnconfigure("4", weight=1)

        self.row = row
        self.title = title

        self.label = ctk.CTkLabel(self, text=self.title, anchor="center")
        self.label.grid(row=self.row, column=0, pady=(10, 10))

        self.value = ctk.CTkLabel(self, text="0")
        self.value.grid(row=self.row, column=3, pady=(10, 10))

        self.up = ctk.CTkButton(self, text="+", width=50, command=self.increment)
        self.up.grid(row=self.row, column=4, pady=(10, 10), padx=(5, 0), sticky="w")

        self.down = ctk.CTkButton(self, text="-", width=50, command=self.decrement)
        self.down.grid(row=self.row, column=2, pady=(10, 10), padx=(0, 5), sticky="e")

    def increment(self):
        self.value.configure(text=str(int(self.value.cget("text")) + 1))

    def decrement(self):
        self.value.configure(text=str(int(self.value.cget("text")) - 1))
