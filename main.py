import json_handler as j
import score_handler as sh

values = j.get_value("Auto", "Cubes", "top")

perfect_game = [3,3,6,6,9,"true","true","true"]



if __name__ == '__main__':
    sh.calculate_scores(perfect_game)
