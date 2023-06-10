import json
import json_handler as j
import random
import os


def calculate_scores(score_values, weights):
    # Normalize the weights to ensure they sum up to 1
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]

    weighted_scores = sum(get_weighted_score(score, weight) for score, weight in zip(score_values, normalized_weights))
    max_weighted_scores = sum(weight for weight in normalized_weights)

    # Calculate the final score scaled from 0 to 100
    final_score = (weighted_scores / max_weighted_scores) * 100

    # Ensure the final score is within the range of 0 to 100

    # Print the final score
    return round(final_score, 0)


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
    mobility_dock = True
    mobility_engage = random.choice([True, False])

    if not mobility_engage:
        mobility_dock = False

    mobility_exit = random.choice([True, False])

    # Return the randomized scores and mobility status as an array
    return [cubes_top, cubes_mid, cones_top, cones_mid, gamepiece_low, mobility_dock, mobility_engage, mobility_exit]

def random_tele():
    # Generate random scores for each component
    cubes_top = random.randint(0, 3)
    cubes_mid = random.randint(0, 3)

    cones_top = random.randint(0, 6)
    cones_mid = random.randint(0, 6)

    gamepiece_low = random.randint(0, 9)

    mobility_cycle = random.randint(10,25)

    # Randomize docking and engagement
    mobility_dock = True
    mobility_engage = random.choice([True, False])

    if not mobility_engage:
        mobility_dock = False

    mobility_exit = random.choice([True, False])

    # Return the randomized scores and mobility status as an array
    return [cubes_top, cubes_mid, cones_top, cones_mid, gamepiece_low, mobility_cycle, mobility_engage, mobility_exit]


def random_endgame():
    # Randomize the endgame status
    endgame_dock = random.choice([True, False])
    endgame_engage = random.choice([True, False])
    endgame_exit = random.choice([True, False])
    endgame_park = random.choice([True, False])

    if not endgame_dock:
        endgame_exit = False

    # Return the randomized endgame status as an array
    return [endgame_dock, endgame_engage, endgame_exit, endgame_park]


def create_score_file(team_number, score_auto, score_tele, score_endgame):
    auto_weights = j.get_weights("Auto")
    teleop_weights = j.get_weights("Tele")
    endgame_weights = j.get_weights("Endgame")

    auto_score = calculate_scores(score_auto, auto_weights)
    teleop_score = calculate_scores(score_tele, teleop_weights)
    endgame_score = calculate_scores(score_endgame, endgame_weights)

    output = {
        "team_number": team_number,
        "scores": {
            "auto": auto_score,
            "teleop": teleop_score,
            "endgame": endgame_score
        },
        "raw_scores": {
            "auto": score_auto,
            "teleop": score_tele,
            "endgame": score_endgame
        }
    }

    scores_directory = "scores/"
    existing_matches = []
    for filename in os.listdir(scores_directory):
        if filename.endswith(".json"):
            existing_matches.append(int(filename.split("_")[1].split(".")[0]))

    match_number = 1
    while match_number in existing_matches:
        match_number += 1

    output["match_number"] = match_number
    file_contents = json.dumps(output, indent=4)
    path = scores_directory + str(team_number) + "_" + str(match_number) + ".json"

    with open(path, "w+") as file:
        file.write(file_contents)


def interpolate_score_placement(score: int, category: str):
    with open('rankings/'+category.lower()+'_rankings.json', 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)

    placement = 0

    # Find the ranks above and below the given score
    ranks_above = [int(rank) for rank in data.keys() if data[rank] > score]
    ranks_below = [int(rank) for rank in data.keys() if data[rank] < score]

    if ranks_above and ranks_below:
        # Interpolate the placement
        rank_above = max(ranks_above)
        rank_below = min(ranks_below)
        placement = rank_below + (rank_above - rank_below) * (score - data[str(rank_below)]) / (data[str(rank_above)] - data[str(rank_below)])

    return round(placement)