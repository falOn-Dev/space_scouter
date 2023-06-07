import json_handler as j
import score_handler as sh

values = j.get_value("Auto", "Cubes", "top")

perfect_game = [3,3,6,6,9,"true","true","true"]



if __name__ == '__main__':
    #input_scores = sh.input_scores()
    random_game = sh.random_auto()
    print(random_game)
    sh.calculate_auto(perfect_game)
