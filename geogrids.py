import pandas as pd

import itertools
from progressbar import progressbar

import pandas as pd
import numpy as np

geogrids = pd.read_csv("GEO.csv", delimiter=";")

country_columns = geogrids.columns[[i * 2 for i in range(9)]]
value_columns = geogrids.columns[[i * 2 + 1 for i in range(9)]]

columns = {col: [] for col in country_columns}


for index, row in progressbar(geogrids.iterrows()):
    for country, value in zip(country_columns, value_columns):
        if type(row[country]) == str:
            tall = row[value]
            if type(tall) != float:
                tall = float(tall.replace(",", "."))
            columns[country].append({row[country]: tall})

print("start building combos ( ͡° ͜ʖ ͡°)")
combos = list(itertools.product(*columns.values()))
print("finished building combos ( ͡ʘ ͜ʖ ͡ʘ) \n")
best_combo = ""
best_value = float("inf")

for combination in progressbar(combos):
    combo_name = [list(dictionary.keys())[0] for dictionary in combination]
    if len(combo_name) != len(set(combo_name)):
        continue
    combo_sum = sum([list(dictionary.values())[0] for dictionary in combination])
    if combo_sum < best_value:
        best_value = combo_sum
        best_combo = combo_name


print(best_combo)
print(best_value)
