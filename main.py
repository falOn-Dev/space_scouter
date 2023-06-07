import json_handler as ci
import csv_handler as cv

values = ci.get_value("Auto", "Cubes", "top")
print(values)

cv.output_score()