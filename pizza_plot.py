from pandas import read_csv as csv, DataFrame


'''import os
ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
print(ROOT_DIR)'''

dataframe = csv(".\\time-series-output\\neurons.csv", index_col="Unnamed: 0")


print(dataframe)

dataframe.groupby(['Brasília', 'Florianópolis', 'Natal', 'Petrolina', 'São Luís']).sum().plot(kind='pie', y='points')