import json
import os

import json_handler as j
import pandas as pd


def auto_ranker():
    ranks = set()  # Use a set to disallow duplicate values
    for filename in os.listdir('scores'):
        if filename.endswith('.json'):
            data = pd.read_json('scores/' + filename)
            score = data['scores']['auto']
            ranks.add(score)  # Add score to the set

    ranks = sorted(ranks, reverse=True)  # Sort the set in descending order
    print(ranks)

    json_object = {str(100 - index): int(value) for index, value in enumerate(ranks)}

    # Convert the dictionary to a JSON string
    with open('rankings/auto_rankings.json', 'w') as outfile:
        json.dump(json_object, outfile, indent=4)



def tele_ranker():
    pass
