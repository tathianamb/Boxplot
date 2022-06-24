from pandas import read_csv as csv, DataFrame
from collections import Counter
from matplotlib import pyplot as plt

'''import os
ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
print(ROOT_DIR)'''

dataframe = csv(".\\time-series-output\\neurons.csv", sep=';')
values = dataframe.iloc[:, 1:].values.reshape(1,-1)[0]
map = dict(Counter(values))
map_sorted = {k: v for k, v in sorted(map.items(), key=lambda item: item[1])}

color = ["#76ff89",
         "#00f5a1",
         "#00e8c3",
         "#00daea",
         "#00c9ff",
         "#00b7ff",
         "#00a1ff",
         "#0086ff",
         "#0060ff"]
explode = (0.4, 0.3, 0.2, 0.1, 0.05, 0.025, 0, 0, 0)
labels = []
sizes = []

for x, y in map_sorted.items():
    labels.append(x)
    sizes.append(y)

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=color, explode=explode, autopct='%.1f%%')
ax.legend(wedges, labels,
          title="Quantidade de neurônios",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
plt.axis('equal')
plt.tight_layout()
plt.show()