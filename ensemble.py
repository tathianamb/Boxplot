from pandas import read_csv as csv
from sklearn.metrics import mean_squared_error as MSE, mean_absolute_error as MAE


base = "SaoLuiz"

df_y = csv(".\\time-series-output\\output" + base
                + "\\saida_teste_mse.csv", index_col="Unnamed: 0", sep=';')

df_y["Ensemble-média-todos"] = df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False)
df_y["Ensemble-média-NN"] = df_y[['ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False)

df_mse = csv(".\\time-series-output\\output" + base
                + "\\all_mse.csv"
             #, index_col="Unnamed: 0", sep=';'
             )

df_mse = df_mse[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP","AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN","RBF","AR+RBF","ARMA+RBF"]]

df_mse.loc[:, "Mediana (ML)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA']].median(axis=1, skipna=False))
df_mse.loc[:, "Mediana (RNAs)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN', 'RBF']].median(axis=1, skipna=False))
df_mse.loc[:, "Mediana (RNAs sem RBF)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN']].median(axis=1, skipna=False))
df_mse.loc[:, "Mediana (MU)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN', 'RBF']].median(axis=1, skipna=False))
df_mse.loc[:, "Mediana (MU sem RBF)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN']].median(axis=1, skipna=False))
df_mse.loc[:, "Mediana (todos)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP",
                                                                       "AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN",
                                                                       "RBF","AR+RBF","ARMA+RBF"]]
                                                  .median(axis=1, skipna=False))


df_mse.loc[:, "Média (ML)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA']].mean(axis=1, skipna=False))
df_mse.loc[:, "Média (RNAs)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False))
df_mse.loc[:, "Média (RNAs sem RBF)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN']].mean(axis=1, skipna=False))
df_mse.loc[:, "Média (MU)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False))
df_mse.loc[:, "Média (MU sem RBF)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN']].mean(axis=1, skipna=False))
df_mse.loc[:, "Média (todos)"] = MSE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP",
                                                                       "AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN",
                                                                       "RBF","AR+RBF","ARMA+RBF"]]
                                                  .mean(axis=1, skipna=False))

df_MAE = df_mse[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP","AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN","RBF","AR+RBF","ARMA+RBF"]].copy()

df_MAE.loc[:, "Mediana (ML)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA']].median(axis=1, skipna=False))
df_MAE.loc[:, "Mediana (RNAs)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN', 'RBF']].median(axis=1, skipna=False))
df_MAE.loc[:, "Mediana (RNAs sem RBF)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN']].median(axis=1, skipna=False))
df_MAE.loc[:, "Mediana (MU)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN', 'RBF']].median(axis=1, skipna=False))
df_MAE.loc[:, "Mediana (MU sem RBF)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN']].median(axis=1, skipna=False))
df_MAE.loc[:, "Mediana (todos)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP",
                                                                       "AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN",
                                                                       "RBF","AR+RBF","ARMA+RBF"]]
                                                  .median(axis=1, skipna=False))



df_MAE.loc[:, "Média (ML)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA']].mean(axis=1, skipna=False))
df_MAE.loc[:, "Média (RNAs)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False))
df_MAE.loc[:, "Média (RNAs sem RBF)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False))
df_MAE.loc[:, "Média (MU)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False))
df_MAE.loc[:, "Média (MU sem RBF)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN']].mean(axis=1, skipna=False))
df_MAE.loc[:, "Média (todos)"] = MAE(y_true=df_y["ACTUAL"],
                                                          y_pred=df_y[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP",
                                                                       "AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN",
                                                                       "RBF","AR+RBF","ARMA+RBF"]]
                                                  .mean(axis=1, skipna=False))

df_mse.to_csv(".\\time-series-output\\output" + base
                + "\\all_mse.csv")

for column in df_mse.columns:
    print(column)
    print('\tmse: ', round( df_mse.iloc[0][column], 6), ', mae:', round(df_MAE.iloc[0][column], 6))