import matplotlib.pyplot as plt
from pandas import read_csv as csv


dataframe = csv(".\\time-series-output\\rankings.csv", sep=';')
'''dataframe = dataframe.transpose()
dataframe.columns = dataframe.iloc[0]
dataframe = dataframe.drop(dataframe.index[0])
dataframe = dataframe.astype(int)'''

'''cols = ["AR",
        "ARMA",
        "MLP",
        "RBF",
        "ELM",
        "ESN",
        "Mediana (ML)",
        "Mediana (RNAs)",
        "Mediana (RNAs sem RBF)",
        "Mediana (MU)",
        "Mediana (MU sem RBF)",
        "Mediana (todos)",
        "Média (ML)",
        "Média (RNAs)",
        "Média (RNAs sem RBF)",
        "Média (MU)",
        "Média (MU sem RBF)",
        "Média (todos)"]

dataframe = dataframe[cols]'''


fig, ax1 = plt.subplots()
ax1.grid(visible=True)

dataframe.boxplot(ax=ax1, rot=90, medianprops=dict(color='orange'))

plt.tight_layout()

plt.show()

fig.savefig(".\\time-series-output\\boxplot_rankings.png", format="png")