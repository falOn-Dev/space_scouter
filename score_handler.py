import json_handler as j

def calculate_scores(score_values):
    cubes_top = float(score_values[0])
    cubes_mid = float(score_values[1])
    cubes_low = float(score_values[2])

    cones_top = float(score_values[3])
    cones_mid = float(score_values[4])
    gamepiece_low = float(score_values[5])

    mobility_dock = score_values[6]
    mobility_engage = score_values[7]
    mobility_exit = score_values[8]

    mobility_weights = [j.get_value("Auto", "Mobility", "dock"),
                        j.get_value("Auto", "Mobility", "engage"),
                        j.get_value("Auto", "Mobility", "exit")]

    # Calculate the final score using the weighted values from the JSON data and inputs
    weighted_scores = (cubes_top * j.get_value("Auto", "Cubes", "top")) + \
                      (cubes_mid * j.get_value("Auto", "Cubes", "mid")) + \
                      (cubes_low * j.get_value("Auto", "Cubes", "low")) + \
                      (cones_top * j.get_value("Auto", "Cones", "top")) + \
                      (cones_mid * j.get_value("Auto", "Cones", "mid")) + \
                      (gamepiece_low * j.get_value("Auto", "Gamepiece", "low"))

    if mobility_dock.lower() == "true":
        weighted_scores += mobility_weights[0]
    if mobility_engage.lower() == "true":
        weighted_scores += mobility_weights[1]
    if mobility_exit.lower() == "true":
        weighted_scores += mobility_weights[2]

    # Calculate the maximum possible weighted score
    max_weighted_scores = (1 * j.get_value("Auto", "Cubes", "top")) + \
                          (1 * j.get_value("Auto", "Cubes", "mid")) + \
                          (1 * j.get_value("Auto", "Cubes", "low")) + \
                          (1 * j.get_value("Auto", "Cones", "top")) + \
                          (1 * j.get_value("Auto", "Cones", "mid")) + \
                          (1 * j.get_value("Auto", "Gamepiece", "low")) + \
                          sum(mobility_weights)

    # Calculate the final score scaled from 0 to 100
    final_score = (weighted_scores / max_weighted_scores) * 100

    # Print the final score
    print("Final Score:", round(final_score, 2))


def input_scores():
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

