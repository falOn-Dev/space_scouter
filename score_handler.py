import json_handler as j
import random


def calculate_auto(score_values):
    cubes_top = float(score_values[0])
    cubes_mid = float(score_values[1])

    cones_top = float(score_values[2])
    cones_mid = float(score_values[3])
    gamepiece_low = float(score_values[4])

    mobility_dock = score_values[5]
    mobility_engage = score_values[6]
    mobility_exit = score_values[7]

    mobility_weights = [
        j.get_value("Auto", "Mobility", "dock"),
        j.get_value("Auto", "Mobility", "engage"),
        j.get_value("Auto", "Mobility", "exit")
    ]

    # Calculate the final score using the weighted values from the JSON data and inputs
    weighted_scores = (
            cubes_top * j.get_value("Auto", "Cubes", "top")
            + cubes_mid * j.get_value("Auto", "Cubes", "mid")
            + cones_top * j.get_value("Auto", "Cones", "top")
            + cones_mid * j.get_value("Auto", "Cones", "mid")
            + gamepiece_low * j.get_value("Auto", "Gamepiece", "low")
    )

    if mobility_dock.lower() == "true":
        weighted_scores += mobility_weights[0]
    if mobility_engage.lower() == "true":
        weighted_scores += mobility_weights[1]
    if mobility_exit.lower() == "true":
        weighted_scores += mobility_weights[2]

    # Calculate the maximum possible weighted score
    max_weighted_scores = (
            cubes_top * j.get_value("Auto", "Cubes", "top")
            + cubes_mid * j.get_value("Auto", "Cubes", "mid")
            + cones_top * j.get_value("Auto", "Cones", "top")
            + cones_mid * j.get_value("Auto", "Cones", "mid")
            + gamepiece_low * j.get_value("Auto", "Gamepiece", "low")
            + sum(mobility_weights)
    )

    # Calculate the final score scaled from 0 to 100
    final_score = (weighted_scores / max_weighted_scores) * 100

    # Print the final score
    print("Final Score:", round(final_score, 2))
def input_auto():
    score_values = []

    score_values.append(float(input("Enter the numerical score for top-level Cubes: ")))
    score_values.append(float(input("Enter the numerical score for mid-level Cubes: ")))

    score_values.append(float(input("Enter the numerical score for top-level Cones: ")))
    score_values.append(float(input("Enter the numerical score for mid-level Cones: ")))
    score_values.append(float(input("Enter the numerical score for the low gamepiece: ")))

    mobility_dock = input("Enter 'True' if Mobility dock is true, otherwise enter 'False': ")
    mobility_engage = input("Enter 'True' if Mobility engage is true, otherwise enter 'False': ")
    mobility_exit = input("Enter 'True' if Mobility exit is true, otherwise enter 'False': ")

    score_values.append(mobility_dock)
    score_values.append(mobility_engage)
    score_values.append(mobility_exit)

    return score_values
def random_auto():
    # Generate random scores for each component
    cubes_top = random.randint(0, 3)
    cubes_mid = random.randint(0, 3)

    cones_top = random.randint(0, 6)
    cones_mid = random.randint(0, 6)

    gamepiece_low = random.randint(0, 9)

    # Randomize docking and engagement
    mobility_dock = "true"
    mobility_engage = random.choice(["true", "false"])
    if mobility_engage == "false":
        mobility_dock = "false"

    mobility_exit = random.choice(["true", "false"])

    # Return the randomized scores and mobility status as an array
    return [cubes_top, cubes_mid, cones_top, cones_mid, gamepiece_low, mobility_dock, mobility_engage, mobility_exit]

def calculate_tele(score_values):
    cubes_top = float(score_values[0])
    cubes_mid = float(score_values[1])

    cones_top = float(score_values[2])
    cones_mid = float(score_values[3])
    gamepiece_low = float(score_values[4])

    cycle = float(score_values[5])

    mobility_dock = score_values[6]
    mobility_engage = score_values[7]
    mobility_exit = score_values[8]

    mobility_weights = [
        j.get_value("Tele", "Mobility", "dock"),
        j.get_value("Tele", "Mobility", "engage"),
        j.get_value("Tele", "Mobility", "exit"),
    ]

    # Calculate the final score using the weighted values from the JSON data and inputs
    weighted_scores = (
        cubes_top * j.get_value("Tele", "Cubes", "top")
        + cubes_mid * j.get_value("Tele", "Cubes", "mid")
        + cones_top * j.get_value("Tele", "Cones", "top")
        + cones_mid * j.get_value("Tele", "Cones", "mid")
        + gamepiece_low * j.get_value("Tele", "Gamepiece", "low")
        + cycle * j.get_value("Tele", "Mobility", "cycle")
    )

    if mobility_dock.lower() == "true":
        weighted_scores += mobility_weights[0]
    if mobility_engage.lower() == "true":
        weighted_scores += mobility_weights[1]
    if mobility_exit.lower() == "true":
        weighted_scores += mobility_weights[2]

    # Calculate the maximum possible weighted score
    max_weighted_scores = (
        cubes_top * j.get_value("Tele", "Cubes", "top")
        + cubes_mid * j.get_value("Tele", "Cubes", "mid")
        + cones_top * j.get_value("Tele", "Cones", "top")
        + cones_mid * j.get_value("Tele", "Cones", "mid")
        + gamepiece_low * j.get_value("Tele", "Gamepiece", "low")
        + sum(mobility_weights)
    )

    # Calculate the final score scaled from 0 to 100
    final_score = (weighted_scores / max_weighted_scores) * 100

    # Print the final score
    print("Final Score:", round(final_score, 2))
def input_tele():
    score_values = []

    score_values.append(float(input("Enter the numerical score for top-level Cubes: ")))
    score_values.append(float(input("Enter the numerical score for mid-level Cubes: ")))

    score_values.append(float(input("Enter the numerical score for top-level Cones: ")))
    score_values.append(float(input("Enter the numerical score for mid-level Cones: ")))
    score_values.append(float(input("Enter the numerical score for the low gamepiece: ")))

    cycle = float(input("Enter the numerical score for the cycle: "))

    mobility_dock = input("Enter 'True' if Mobility dock is true, otherwise enter 'False': ")
    mobility_engage = input("Enter 'True' if Mobility engage is true, otherwise enter 'False': ")
    mobility_exit = input("Enter 'True' if Mobility exit is true, otherwise enter 'False': ")

    score_values.append(cycle)
    score_values.append(mobility_dock)
    score_values.append(mobility_engage)
    score_values.append(mobility_exit)

    return score_values
def random_tele():
    # Generate random scores for each component
    cubes_top = random.randint(0, 3)
    cubes_mid = random.randint(0, 3)

    cones_top = random.randint(0, 6)
    cones_mid = random.randint(0, 6)

    gamepiece_low = random.randint(0, 9)

    cycle = random.randint(0, 5)

    # Randomize docking and engagement
    mobility_dock = "true"
    mobility_engage = random.choice(["true", "false"])
    if mobility_engage == "false":
        mobility_dock = "false"

    mobility_exit = random.choice(["true", "false"])

    # Return the randomized scores and mobility status as an array
    return [cubes_top, cubes_mid, cones_top, cones_mid, gamepiece_low, cycle, mobility_dock, mobility_engage, mobility_exit]


def calculate_endgame(score_values):
    link = float(score_values[0])
    sustain = score_values[1].lower() == "true"
    coop = score_values[2].lower() == "true"
    activation = score_values[3].lower() == "true"
    win = score_values[4].lower() == "true"

    endgame_weights = [
        j.get_value("Endgame", "Bonus", "link"),
        j.get_value("Endgame", "Bonus", "sustain"),
        j.get_value("Endgame", "Bonus", "coop"),
        j.get_value("Endgame", "Bonus", "activation"),
        j.get_value("Endgame", "Bonus", "win")
    ]

    # Calculate the final score using the weighted values from the JSON data and inputs
    weighted_scores = (
        link * endgame_weights[0]
        + endgame_weights[1] if sustain else 0
        + endgame_weights[2] if coop else 0
        + endgame_weights[3] if activation else 0
        + endgame_weights[4] if win else 0
    )

    # Calculate the maximum possible weighted score
    max_weighted_scores = sum(endgame_weights)

    # Calculate the final score scaled from 0 to 100
    final_score = (weighted_scores / max_weighted_scores) * 100

    # Print the final score
    print("Final Score:", round(final_score, 2))
def input_endgame():
    score_values = []

    link = float(input("Enter the numerical score for link: "))
    sustain = input("Enter 'True' if Sustain is true, otherwise enter 'False': ")
    coop = input("Enter 'True' if Coop is true, otherwise enter 'False': ")
    activation = input("Enter 'True' if Activation is true, otherwise enter 'False': ")
    win = input("Enter 'True' if Win is true, otherwise enter 'False': ")

    score_values.append(link)
    score_values.append(sustain)
    score_values.append(coop)
    score_values.append(activation)
    score_values.append(win)

    return score_values
def random_endgame():
    link = random.randint(0, 10)

    coop = random.choice(["True", "False"])
    if coop == "True" and link >= 4:
        sustain = "True"
    elif coop == "False" and link >= 5:
        sustain = "True"
    else:
        sustain = "False"

    activation = random.choice(["True", "False"])
    win = random.choice(["True", "False"])

    return [link, sustain, coop, activation, win]







