from pandas import read_csv as csv, DataFrame, Series
from collections import Counter
from matplotlib import pyplot as plt

'''import os
ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
print(ROOT_DIR)
'''
lags_rna = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            1, 2, 3, 4, 5, 6, 7, 13, 14, 15,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            1, 2, 3, 4, 5, 6, 7, 8, 10, 12]

lags_ar = [5, 6, 7, 8, 11, 16, 17, 22, 24, 30,
            5, 6, 7, 8, 9, 10, 11, 24,
            8, 9, 14, 15, 16, 21, 22, 23, 24, 30,
            3, 4, 5, 12, 15, 17, 21, 23, 27, 29,
            5, 6, 7, 10, 12, 15, 16, 18, 20, 30]

lags_arma = [2, 3, 5, 7, 10, 16, 17, 22, 27, 30,
            3, 9, 10, 11, 14, 19, 21, 22, 24, 27,
            7, 8, 14, 15, 16, 21, 22, 23, 24, 30,
            9, 17,
            3, 9, 11, 12, 15, 16, 18, 20, 28]

series = Series(data=lags_rna)

map_counter = dict(Counter(series))
map_counter = {k: v for k, v in sorted(map_counter.items(), key=lambda item: item[0])}

var = 100/5

map_percentage = {i:j*var for i,j in map_counter.items()}
map_percentage = {k: v for k, v in sorted(map_percentage.items(), key=lambda item: item[0])}

fig, ax1 = plt.subplots()
fig.set_figheight(5)
fig.set_figwidth(10)
color = 'tab:blue'
ax1.set_xlabel('lag')
ax1.set_ylabel('Número de seleções', color=color)
ax1.bar(map_counter.keys(), map_counter.values(), color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'black'

ax2.set_ylabel('Porcentagem de seleções', color=color)  # we already handled the x-label with ax1
ax2.plot(map_counter.keys(), map_percentage.values(), 'o-', color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()