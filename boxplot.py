import matplotlib.pyplot as plt
from pandas import read_csv as csv


base = "SaoLuiz"

dataframe = csv(".\\time-series-output\\output" + base
                + "\\all_mse.csv", index_col="Unnamed: 0")

fig, ax1 = plt.subplots()

dataframe.boxplot(ax=ax1, rot=90, medianprops=dict(color='orange'))

'''
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True
                               , gridspec_kw={'height_ratios': [1, 3]}
                               )

dataframe.boxplot(ax=ax1, medianprops=dict(color='orange'))
ax1.set_xlabel('')
ax1.set_ylim(ymin=10,ymax=35)
#fig, ax1 = plt.subplots()
dataframe.boxplot(ax=ax2, rot=90, medianprops=dict(color='orange'))
ax2.set_title('')
ax2.set_ylim(ymin=0,ymax=6.5)
fig.subplots_adjust(top=0.3)

ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.set_visible(True)
ax1.grid(visible=True)
ax2.grid(visible=True)
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

fig.savefig(".\\time-series-output\\output" + base
               + "/boxplot.png", format="png")