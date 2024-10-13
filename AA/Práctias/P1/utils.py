import numpy as np
import pandas as pd


def cleanData(gamesData):
    # numeros -> score(0-100), user score(0.0-10.0), critics users

    #limpia valores
    gamesData['score'] = gamesData['score'].astype(np.float32)
    #gamesData['score'].fillna(gamesData['score'].mean(), inplace = True)
    #gamesData['score']= pd.to_numeric(gamesData['score'], errors='coerce')
    gamesData['score']=gamesData['score'].div(10)

    # Limpia valores tbd y convierte en float32
    gamesData['user score'].replace('tbd', np.nan, inplace = True)
    gamesData['user score'].fillna(np.nan)
    gamesData['user score'] = gamesData['user score'].astype(np.float32)

    return gamesData

def load_data_csv(path,x_colum,y_colum):
    data = pd.read_csv(path)
    data = cleanData(data)
    X = data[x_colum].to_numpy()
    y = data[y_colum].to_numpy()
    return X, y