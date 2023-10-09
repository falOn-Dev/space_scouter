import customtkinter as ctk


class CheckFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, row, labels, window):
        super().__init__(master)
        self.grid_columnconfigure("0", weight=1)
        self.grid_columnconfigure("1", weight=1)
        self.grid_columnconfigure("2", weight=1)
        self.grid_columnconfigure("3", weight=1)
        self.grid_columnconfigure("4", weight=1)

        self.window = window

        self.row = row
        self.values = []


        for i in range(len(labels)):
            self.create_widget(labels[i], i)

    def create_widget(self, title, row):
        self.value = ctk.CTkCheckBox(self, text=title, command=self.window.update_scores)
        self.value.grid(row=row, column=3, pady=(10, 10))

        self.values.append(self.value)

    def get_values(self):
        return [bool(value.get()) for value in self.values]