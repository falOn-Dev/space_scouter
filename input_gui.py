from functools import partial

import customtkinter as ctk


class AutoInputWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engaged_checkbox = None
        self.docked_checkbox = None
        self.low_pieces_value = None
        self.top_cones_value = None
        self.mid_cones_value = None
        self.mid_cubes_value = None
        self.top_cubes_value = None
        self.exited_checkbox = None
        self.geometry("600x400")
        self.title("Auto Input")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.grid_rowconfigure(999, weight=1)

        self.create_input_fields()
        self.create_checkboxes()

    def create_input_fields(self):
        row = 0

        # Top Cubes
        top_cubes_label = ctk.CTkLabel(self, text="Top Cubes:", anchor="center")
        top_cubes_label.grid(row=row, column=0, pady=(10, 0))

        top_cubes_value = ctk.CTkLabel(self, text="0")
        top_cubes_value.grid(row=row, column=3, pady=(10, 0))

        top_cubes_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=top_cubes_value: self.top_cubes_up_command(label), width=50)
        top_cubes_up.grid(row=row, column=2, pady=(10, 0))

        top_cubes_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=top_cubes_value: self.top_cubes_down_command(label),
                                       width=50)
        top_cubes_down.grid(row=row, column=4, pady=(10, 0))

        row += 1

        # Mid Cubes
        mid_cubes_label = ctk.CTkLabel(self, text="Mid Cubes:", anchor="center")
        mid_cubes_label.grid(row=row, column=0, pady=(10, 0))

        mid_cubes_value = ctk.CTkLabel(self, text="0")
        mid_cubes_value.grid(row=row, column=3, pady=(10, 0))

        mid_cubes_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=mid_cubes_value: self.top_cubes_up_command(label), width=50)
        mid_cubes_up.grid(row=row, column=2, pady=(10, 0))

        mid_cubes_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=mid_cubes_value: self.top_cubes_down_command(label),
                                       width=50)
        mid_cubes_down.grid(row=row, column=4, pady=(10, 0))

        row += 1

        # Top Cones
        top_cones_label = ctk.CTkLabel(self, text="Top Cones:", anchor="center")
        top_cones_label.grid(row=row, column=0, pady=(10, 0))

        top_cones_value = ctk.CTkLabel(self, text="0")
        top_cones_value.grid(row=row, column=3, pady=(10, 0))

        top_cones_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=top_cones_value: self.top_cubes_up_command(label), width=50)
        top_cones_up.grid(row=row, column=2, pady=(10, 0))

        top_cones_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=top_cones_value: self.top_cubes_down_command(label),
                                       width=50)
        top_cones_down.grid(row=row, column=4, pady=(10, 0))

        row += 1

        # Mid Cones
        mid_cones_label = ctk.CTkLabel(self, text="Mid Cones:", anchor="center")
        mid_cones_label.grid(row=row, column=0, pady=(10, 0))

        mid_cones_value = ctk.CTkLabel(self, text="0")
        mid_cones_value.grid(row=row, column=3, pady=(10, 0))

        mid_cones_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=mid_cones_value: self.top_cubes_up_command(label), width=50)
        mid_cones_up.grid(row=row, column=2, pady=(10, 0))

        mid_cones_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=mid_cones_value: self.top_cubes_down_command(label),
                                       width=50)
        mid_cones_down.grid(row=row, column=4, pady=(10, 0))

        row += 1

        # Low Pieces
        low_pieces_label = ctk.CTkLabel(self, text="Low Pieces:", anchor="center")
        low_pieces_label.grid(row=row, column=0, pady=(10, 0))

        low_pieces_value = ctk.CTkLabel(self, text="0")
        low_pieces_value.grid(row=row, column=3, pady=(10, 0))

        low_pieces_up = ctk.CTkButton(self, text="+",
                                      command=lambda label=low_pieces_value: self.top_cubes_up_command(label), width=50)
        low_pieces_up.grid(row=row, column=2, pady=(10, 0))

        low_pieces_down = ctk.CTkButton(self, text="-",
                                        command=lambda label=low_pieces_value: self.top_cubes_down_command(label),
                                        width=50)
        low_pieces_down.grid(row=row, column=4, pady=(10, 0))

        calculate_button = ctk.CTkButton(self, text="Calculate", command=partial(self.print_input_values))
        calculate_button.grid(row=999, column=0, sticky="sw", padx=20, pady=20)

        self.top_cubes_value = top_cubes_value
        self.mid_cubes_value = mid_cubes_value
        self.top_cones_value = top_cones_value
        self.mid_cones_value = mid_cones_value
        self.low_pieces_value = low_pieces_value

    def create_checkboxes(self):
        row = 5

        docked_checkbox = ctk.CTkCheckBox(self, text="Docked")
        docked_checkbox.grid(row=row, column=0,pady=10)

        engaged_checkbox = ctk.CTkCheckBox(self, text="Engaged")
        engaged_checkbox.grid(row=row + 1, column=0,pady=10)

        exited_checkbox = ctk.CTkCheckBox(self, text="Exited")
        exited_checkbox.grid(row=row + 2, column=0,pady=10)

        self.docked_checkbox = docked_checkbox
        self.engaged_checkbox = engaged_checkbox
        self.exited_checkbox = exited_checkbox

    def top_cubes_up_command(self, label):
        label.configure(text=str(int(label.cget("text")) + 1))

    def top_cubes_down_command(self, label):
        label.configure(text=str(int(label.cget("text")) - 1))

    def get_input_values(self):
        input_values = []

        # Get the values of the input fields
        top_cubes_value = int(self.top_cubes_value.cget("text"))
        mid_cubes_value = int(self.mid_cubes_value.cget("text"))
        top_cones_value = int(self.top_cones_value.cget("text"))
        mid_cones_value = int(self.mid_cones_value.cget("text"))
        low_pieces_value = int(self.low_pieces_value.cget("text"))

        # Get the values of the checkboxes
        docked_value = bool(self.docked_checkbox.get())
        engaged_value = bool(self.engaged_checkbox.get())
        exited_value = bool(self.exited_checkbox.get())

        # Append the values to the array
        input_values.append(top_cubes_value)
        input_values.append(mid_cubes_value)
        input_values.append(top_cones_value)
        input_values.append(mid_cones_value)
        input_values.append(low_pieces_value)
        input_values.append(docked_value)
        input_values.append(engaged_value)
        input_values.append(exited_value)

        return input_values

    def print_input_values(self):
        print(self.get_input_values())


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.title("Space Scouter")

        self.button_1 = ctk.CTkButton(self, text="Input Auto Score", command=lambda: self.open_toplevel(AutoInputWindow))
        self.button_1.pack(side="top", padx=10, pady=10)

        self.toplevel_window = None

    def open_toplevel(self, window):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = window(self)  # create window if it's None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists, focus it
