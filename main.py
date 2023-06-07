import json_handler as j
import score_handler as sh

values = j.get_value("Auto", "Cubes", "top")

perfect_game = [3,0,0,0,0,False,False,False]

score_values = [0.15, 0.1, True, False, 0.01, True, True, False]

if __name__ == '__main__':
    weights = j.get_weights("Auto")
    final_score = sh.calculate_scores(perfect_game,weights)
    print(final_score)


