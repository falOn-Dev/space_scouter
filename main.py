import json_handler as j
from gui.input_gui import App
import score_handler as sh

#values = j.get_value("Auto", "Cubes", "top")

perfect_auto = [3, 3, 6, 6, 9, True, True, True]
perfect_tele = [3, 3, 6, 6, 9, 15, True, True, True]
perfect_endgame = [True, True, True, True]

score_values = [0.15, 0.1, True, False, 0.01, True, True, False]

if __name__ == '__main__':

    app = App()
    app.mainloop()

    # for i in range(50):
    #sh.create_score_file(2537, perfect_auto, perfect_tele, perfect_endgame)
    # print(sh.interpolate_score_placement(410, "teleop"))
    # rh.ranker("teleop")
    # rh.ranker("auto")
    # rh.ranker("endgame")
