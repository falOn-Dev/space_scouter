import customtkinter as ctk


class NumericalValue(ctk.CTkScrollableFrame):
    def __init__(self, master, row, labels, window):
        super().__init__(master)
        self.grid_columnconfigure("0", weight=1)
        self.grid_columnconfigure("1", weight=1)
        self.grid_columnconfigure("2", weight=1)
        self.grid_columnconfigure("3", weight=1)
        self.grid_columnconfigure("4", weight=1)

        self.row = row
        self.values = []

        self.window = window

        for i in range(len(labels)):
            self.create_widget(labels[i], i)



    def increment(self, label):
        label.configure(text=str(int(label.cget("text")) + 1))
        self.window.update_scores()

    def decrement(self, label):
        label.configure(text=str(int(label.cget("text")) - 1))
        self.window.update_scores()

    def create_widget(self, title, row):
        self.label = ctk.CTkLabel(self, text=title, anchor="center")
        self.label.grid(row=row, column=0, pady=(10, 10))

        self.value = ctk.CTkLabel(self, text="0")
        self.value.grid(row=row, column=3, pady=(10, 10))

        self.up = ctk.CTkButton(self, text="+", width=50, command=lambda label=self.value: self.increment(label))
        self.up.grid(row=row, column=4, pady=(10, 10), padx=(5, 0), sticky="w")

        self.down = ctk.CTkButton(self, text="-", width=50, command=lambda label=self.value: self.decrement(label))
        self.down.grid(row=row, column=2, pady=(10, 10), padx=(0, 5), sticky="e")

        self.values.append(self.value)

    def get_values(self):
        return [int(value.cget("text")) for value in self.values]



