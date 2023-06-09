import json_handler as j
import score_handler as sh

values = j.get_value("Auto", "Cubes", "top")

perfect_auto = [3, 3, 6, 6, 9, True, True, True]
perfect_tele = [3, 3, 6, 6, 9, 15, True, True, True]
perfect_endgame = [5, True, True, True, True]

score_values = [0.15, 0.1, True, False, 0.01, True, True, False]

if __name__ == '__main__':
    sh.create_score_file(2537, 1, perfect_auto, perfect_tele, perfect_endgame)