import numpy as np
from pandas import read_csv as csv
from pandas import DataFrame
from sklearn.metrics import mean_squared_error as MSE, mean_absolute_error as MAE


def average_relative_variance(y_true, y_pred):
    y_true = np.asarray(y_true).reshape(-1)
    y_pred = np.asarray(y_pred).reshape(-1)
    mean = np.mean(y_true)

    error_sup = np.square(np.subtract(y_true, y_pred)).sum()
    error_inf = np.square(np.subtract(y_pred, mean)).sum()

    return error_sup / error_inf


def index_agreement(y_true, y_pred):
    y_true = np.asarray(y_true).reshape(-1)
    y_pred = np.asarray(y_pred).reshape(-1)
    mean = np.mean(y_true)

    error_sup = np.square(np.abs(np.subtract(y_true, y_pred))).sum()

    error_inf = np.abs(np.subtract(y_pred, mean)) + np.abs(np.subtract(y_true, mean))
    error_inf = np.square(error_inf).sum()

    return 1 - (error_sup / error_inf)


base = "Brasilia"

df_y = csv(".\\time-series-output\\output" + base
                + "\\saida_teste_mse.csv"
           , index_col="Unnamed: 0"
           , sep=';'
           )

df_y.loc[:, "Mediana (ML)"] = df_y[['AR', 'ARMA']].median(axis=1, skipna=False)
df_y.loc[:, "Mediana (RNAs)"] = df_y[['ELM', 'MLP', 'ESN', 'RBF']].median(axis=1, skipna=False)
df_y.loc[:, "Mediana (RNAs sem RBF)"] = df_y[['ELM', 'MLP', 'ESN']].median(axis=1, skipna=False)
df_y.loc[:, "Mediana (MU)"] = df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN', 'RBF']].median(axis=1, skipna=False)
df_y.loc[:, "Mediana (MU sem RBF)"] = df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN']].median(axis=1, skipna=False)
df_y.loc[:, "Mediana (todos)"] = df_y[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP",
                                                                       "AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN",
                                                                       "RBF","AR+RBF","ARMA+RBF"]].median(axis=1, skipna=False)



df_y.loc[:, "Média (ML)"] = df_y[['AR', 'ARMA']].mean(axis=1, skipna=False)
df_y.loc[:, "Média (RNAs)"] = df_y[['ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False)
df_y.loc[:, "Média (RNAs sem RBF)"] = df_y[['ELM', 'MLP', 'ESN']].mean(axis=1, skipna=False)
df_y.loc[:, "Média (MU)"] = df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN', 'RBF']].mean(axis=1, skipna=False)
df_y.loc[:, "Média (MU sem RBF)"] = df_y[['AR', 'ARMA', 'ELM', 'MLP', 'ESN']].mean(axis=1, skipna=False)
df_y.loc[:, "Média (todos)"] = df_y[["AR","ARMA","ELM","AR+ELM","ARMA+ELM","MLP",
                                                                       "AR+MLP","ARMA+MLP","ESN","AR+ESN","ARMA+ESN",
                                                                       "RBF","AR+RBF","ARMA+RBF"]].mean(axis=1, skipna=False)

df_errors = DataFrame(columns=['MSE', 'MAE', 'ARV', 'IA'])

for model in ["AR", "ARMA", "MLP", "RBF", "ELM", "ESN", "AR+MLP", "AR+RBF", "AR+ELM", "AR+ESN", "ARMA+MLP", "ARMA+RBF",
              "ARMA+ELM", "ARMA+ESN", "Mediana (ML)", "Mediana (RNAs)",
              "Mediana (RNAs sem RBF)", "Mediana (MU)", "Mediana (MU sem RBF)",
              "Mediana (todos)", "Média (ML)", "Média (RNAs)",
              "Média (RNAs sem RBF)", "Média (MU)", "Média (MU sem RBF)",
              "Média (todos)"]:

    df_errors.loc[model, 'MSE'] = format(MSE(y_pred=df_y[[model]], y_true=df_y[['ACTUAL']]), '.4f')

    df_errors.loc[model, 'MAE'] = format(MAE(y_pred=df_y[[model]], y_true=df_y[['ACTUAL']]), '.4f')

    df_errors.loc[model, 'ARV'] = format(average_relative_variance(y_pred=df_y[[model]],
                                                            y_true=df_y[['ACTUAL']]), '.4f')

    df_errors.loc[model, 'IA'] = format(index_agreement(y_pred=df_y[[model]],
                                                 y_true=df_y[['ACTUAL']]), '.4f')
print(df_errors)
df_errors.to_csv(".\\time-series-output\\output" + base
                + "\\errors.csv")