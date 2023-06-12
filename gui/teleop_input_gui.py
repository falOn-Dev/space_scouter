from functools import partial

import customtkinter as ctk
import score_handler as score
from json_handler import JsonHandler


class TeleopInputWindow(ctk.CTkToplevel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engaged_checkbox = None
        self.docked_checkbox = None
        self.low_pieces_value = None
        self.top_cones_value = None
        self.mid_cones_value = None
        self.mid_cubes_value = None
        self.top_cubes_value = None
        self.parked_checkbox = None
        self.cycle_value = None

        self.json_handler = JsonHandler()

        self.geometry("550x440")
        self.title("Teleop Input")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.grid_rowconfigure(999, weight=1)

        self.app = app

        self.create_input_fields()
        self.create_checkboxes()

        self.focus()


    def send_teleop_data(self):
        self.app.teleop_data = self.get_input_values()
        self.app.teleop_score.configure(text=self.score_label.cget("text"))
        self.destroy()

    def update_score(self):
        raw_score = self.get_input_values()
        scores = score.calculate_scores(raw_score, self.json_handler.get_weights("Tele"))
        self.score_label.configure(text="Score: " + str(scores))


    def create_input_fields(self):
        row = 0

        # Top Cubes
        top_cubes_label = ctk.CTkLabel(self, text="Top Cubes:", anchor="center")
        top_cubes_label.grid(row=row, column=0, pady=(10, 0))

        top_cubes_value = ctk.CTkLabel(self, text="0")
        top_cubes_value.grid(row=row, column=3, pady=(10, 0))

        top_cubes_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=top_cubes_value: self.top_cubes_up_command(label), width=50)
        top_cubes_up.grid(row=row, column=4, pady=(10, 0), padx=(5, 0), sticky="w")

        top_cubes_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=top_cubes_value: self.top_cubes_down_command(label),
                                       width=50)
        top_cubes_down.grid(row=row, column=2, pady=(10, 0), padx=(0, 5), sticky="e")

        row += 1

        # Mid Cubes
        mid_cubes_label = ctk.CTkLabel(self, text="Mid Cubes:", anchor="center")
        mid_cubes_label.grid(row=row, column=0, pady=(10, 0))

        mid_cubes_value = ctk.CTkLabel(self, text="0")
        mid_cubes_value.grid(row=row, column=3, pady=(10, 0))

        mid_cubes_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=mid_cubes_value: self.top_cubes_up_command(label), width=50)
        mid_cubes_up.grid(row=row, column=4, pady=(10, 0), padx=(5, 0), sticky="w")

        mid_cubes_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=mid_cubes_value: self.top_cubes_down_command(label),
                                       width=50)
        mid_cubes_down.grid(row=row, column=2, pady=(10, 0), padx=(0, 5), sticky="e")

        row += 1

        # Top Cones
        top_cones_label = ctk.CTkLabel(self, text="Top Cones:", anchor="center")
        top_cones_label.grid(row=row, column=0, pady=(10, 0))

        top_cones_value = ctk.CTkLabel(self, text="0")
        top_cones_value.grid(row=row, column=3, pady=(10, 0))

        top_cones_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=top_cones_value: self.top_cubes_up_command(label), width=50)
        top_cones_up.grid(row=row, column=4, pady=(10, 0), padx=(5, 0), sticky="w")

        top_cones_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=top_cones_value: self.top_cubes_down_command(label),
                                       width=50)
        top_cones_down.grid(row=row, column=2, pady=(10, 0), padx=(0, 5), sticky="e")

        row += 1

        # Mid Cones
        mid_cones_label = ctk.CTkLabel(self, text="Mid Cones:", anchor="center")
        mid_cones_label.grid(row=row, column=0, pady=(10, 0))

        mid_cones_value = ctk.CTkLabel(self, text="0")
        mid_cones_value.grid(row=row, column=3, pady=(10, 0))

        mid_cones_up = ctk.CTkButton(self, text="+",
                                     command=lambda label=mid_cones_value: self.top_cubes_up_command(label), width=50)
        mid_cones_up.grid(row=row, column=4, pady=(10, 0), padx=(5, 0), sticky="w")

        mid_cones_down = ctk.CTkButton(self, text="-",
                                       command=lambda label=mid_cones_value: self.top_cubes_down_command(label),
                                       width=50)
        mid_cones_down.grid(row=row, column=2, pady=(10, 0), padx=(0, 5), sticky="e")

        row += 1

        # Low Pieces
        low_pieces_label = ctk.CTkLabel(self, text="Low Pieces:", anchor="center")
        low_pieces_label.grid(row=row, column=0, pady=(10, 0))

        low_pieces_value = ctk.CTkLabel(self, text="0")
        low_pieces_value.grid(row=row, column=3, pady=(10, 0))

        low_pieces_up = ctk.CTkButton(self, text="+",
                                      command=lambda label=low_pieces_value: self.top_cubes_up_command(label), width=50)
        low_pieces_up.grid(row=row, column=4, pady=(10, 0), padx=(5, 0), sticky="w")

        low_pieces_down = ctk.CTkButton(self, text="-",
                                        command=lambda label=low_pieces_value: self.top_cubes_down_command(label),
                                        width=50)
        low_pieces_down.grid(row=row, column=2, pady=(10, 0), padx=(0, 5), sticky="e")

        row += 1

        cycle_time_label = ctk.CTkLabel(self, text="Cycle Time:", anchor="center")
        cycle_time_label.grid(row=row, column=0, pady=(10, 0))
        cycle_time_value = ctk.CTkLabel(self, text="0")
        cycle_time_value.grid(row=row, column=3, pady=(10, 0))
        cycle_time_up = ctk.CTkButton(self, text="+",
                                      command=lambda label=cycle_time_value: self.top_cubes_up_command(label), width=50)
        cycle_time_up.grid(row=row, column=4, pady=(10, 0), padx=(5, 0), sticky="w")
        cycle_time_down = ctk.CTkButton(self, text="-",
                                        command=lambda label=cycle_time_value: self.top_cubes_down_command(label),
                                        width=50)
        cycle_time_down.grid(row=row, column=2, pady=(10, 0), padx=(0, 5), sticky="e")


        self.cycle_value = cycle_time_value

        self.score_label = ctk.CTkLabel(self, text="Score: ", anchor="center")
        self.score_label.grid(row=999, column=0, sticky="sw", padx=20, pady=20)

        send_button = ctk.CTkButton(self, text="Complete", command=self.send_teleop_data)
        send_button.grid(row=999, column=4, sticky="se", padx=20, pady=20)
        self.top_cubes_value = top_cubes_value
        self.mid_cubes_value = mid_cubes_value
        self.top_cones_value = top_cones_value
        self.mid_cones_value = mid_cones_value
        self.low_pieces_value = low_pieces_value

    def create_checkboxes(self):
        row = 6

        docked_checkbox = ctk.CTkCheckBox(self, text="Docked", command=self.update_score)
        docked_checkbox.grid(row=row, column=0, pady=10)

        engaged_checkbox = ctk.CTkCheckBox(self, text="Engaged", command=self.update_score)
        engaged_checkbox.grid(row=row + 1, column=0, pady=10)

        parked_checkbox = ctk.CTkCheckBox(self, text="Parked", command=self.update_score)
        parked_checkbox.grid(row=row + 2, column=0, pady=10)

        self.docked_checkbox = docked_checkbox
        self.engaged_checkbox = engaged_checkbox
        self.parked_checkbox = parked_checkbox

    def top_cubes_up_command(self, label):
        label.configure(text=str(int(label.cget("text")) + 1))
        self.update_score()

    def top_cubes_down_command(self, label):
        label.configure(text=str(int(label.cget("text")) - 1))
        self.update_score()


    def get_input_values(self):
        input_values = []

        # Get the values of the input fields
        top_cubes_value = int(self.top_cubes_value.cget("text"))
        mid_cubes_value = int(self.mid_cubes_value.cget("text"))
        top_cones_value = int(self.top_cones_value.cget("text"))
        mid_cones_value = int(self.mid_cones_value.cget("text"))
        low_pieces_value = int(self.low_pieces_value.cget("text"))
        cycle_value = int(self.cycle_value.cget("text"))

        # Get the values of the checkboxes
        docked_value = bool(self.docked_checkbox.get())
        engaged_value = bool(self.engaged_checkbox.get())
        parked_value = bool(self.parked_checkbox.get())

        # Append the values to the array
        input_values.append(top_cubes_value)
        input_values.append(mid_cubes_value)
        input_values.append(top_cones_value)
        input_values.append(mid_cones_value)
        input_values.append(low_pieces_value)
        input_values.append(cycle_value)
        input_values.append(docked_value)
        input_values.append(engaged_value)
        input_values.append(parked_value)

        return input_values

    def print_input_values(self):
        input_values = self.get_input_values()
        print(input_values)
