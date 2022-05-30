import matplotlib.pyplot as plt
from pandas import read_csv as csv


base = "SaoLuiz"

dataframe = csv("C:\\Users\\Licon\\Dropbox\\Utfpr\\Mestrado\\Matérias\\IA\\Boxplot\\time-series-output\\output" + base
                + "\\all_mse.csv", index_col="Unnamed: 0")

dataframe = dataframe[["ELM","AR+ELM","ARMA+ELM","MLP","AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN","RBF","AR+RBF","ARMA+RBF"]]

'''fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True
                               , gridspec_kw={'height_ratios': [1, 3]}
                               )

dataframe.boxplot(ax=ax1, medianprops=dict(color='orange'))
ax1.set_xlabel('')
ax1.set_ylim(ymin=169,ymax=172.5)'''
fig, ax1 = plt.subplots()
dataframe.boxplot(rot=90, medianprops=dict(color='orange'))
'''ax2.set_title('')
ax2.set_ylim(ymin=0,ymax=1.15)
fig.subplots_adjust(top=0.3)

ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.set_visible(False)
ax1.grid(visible=False)
ax2.grid(visible=False)
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)'''

'''plt.set_figheight(8)
plt.set_figwidth(10)'''
plt.tight_layout()
#plt.show()

fig.savefig("C:\\Users\\Licon\\Dropbox\\Utfpr\\Mestrado\\Matérias\\IA\\Boxplot\\time-series-output\\output" + base
                + "/boxplot.png", format="png")