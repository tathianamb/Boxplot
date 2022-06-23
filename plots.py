from pandas import read_csv as csv, to_datetime as dateTime, Series, DataFrame
from sklearn.model_selection import train_test_split

base = "Brasilia"

def __convertTime(minutes):
    minutes = minutes % (24 * 60)
    hour = minutes // 60
    minutes %= 60
    return "%02d:%02d" % (hour, minutes)


def __convertDate(days):
    if days <= 31:
        date = "%02d/01" % (days)
    else:
        days = days - 31
        date = "%02d/02" % (days)
    return date


def fileToSerie(name: str):
    dataframe = csv("C:\\Users\\Licon\\Dropbox\\Utfpr\\Mestrado\\Matérias\\IA\\Boxplot\\time-series-input\\" + name, names=['year', 'day', 'min', 'ws_10m'], delimiter=';', keep_default_na=False)
    dataframe['min'] = dataframe['min'].apply(__convertTime)
    dataframe['day'] = dataframe['day'].apply(__convertDate)

    dataframe['date'] = dataframe['day'] + '/' + dataframe['year'].astype(str) + '-' + dataframe['min']
    dataframe['date'] = dateTime(dataframe['date'], format='%d/%m/%Y-%H:%M')
    dataframe = dataframe[dataframe['date'] < "2019-02-01"]
    return Series(data=list(dataframe['ws_10m'].astype(float)), index=list(dataframe['date']), name='Actual').asfreq('min')

serie = fileToSerie(base + ".csv")
train, valTest = train_test_split(serie, train_size=0.6, shuffle=False)
validation, test = train_test_split(valTest, test_size=0.5, shuffle=False)

print('Total: ', len(serie))
print('Treinamento: ', len(train))
print('Validação: ', len(validation))
print('Teste: ', len(test))

'''df_resultado = DataFrame(columns=['Média', 'Desvio padrão', 'Mínimo', 'Máximo'], index=['Total', 'Treinamento', 'Validação', 'Teste'])

for index in df_resultado.index:
    if index == 'Total':
        data = serie
    elif index == 'Treinamento':
        data = train
    elif index == 'Validação':
        data = validation
    elif index == 'Teste':
        data = test

    for column in df_resultado.columns:

        if column == 'Média':
            value = round(data.mean(), 4)
        elif column == 'Desvio padrão':
            value = round(data.std(), 4)
        elif column == 'Mínimo':
            value = round(data.min(), 4)
        elif column == 'Máximo':
            value = round(data.max(), 4)

        df_resultado.loc[index, column] = value

print(df_resultado)'''
