import json_handler as j
import random


def calculate_scores(score_values, weights):
    # Normalize the weights to ensure they sum up to 1
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]

    weighted_scores = sum(get_weighted_score(score, weight) for score, weight in zip(score_values, normalized_weights))
    max_weighted_scores = sum(weight for weight in normalized_weights)

    # Calculate the final score scaled from 0 to 100
    final_score = (weighted_scores / max_weighted_scores) * 100

    # Ensure the final score is within the range of 0 to 100
    final_score = min(final_score, 100)

    # Print the final score
    return round(final_score,2)
def get_weighted_score(score, weight):
    if isinstance(score, (int, float)):
        return score * weight
    elif isinstance(score, bool):
        return 100 if score else 0
    elif isinstance(score, str):
        return 100 if score.lower() == "true" else 0
    else:
        return 0
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







