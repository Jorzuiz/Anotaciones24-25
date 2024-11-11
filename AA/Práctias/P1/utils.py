import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cleanData(data):
    
    # numeros -> score(0-100), user score(0.0-10.0), critics users

    #limpia valores
    # Creamos una copia de las puntuacions SIN los valores anómalos para 
    # poder calcular la media y reemplazarlos cin corromper los resultado

    # mean = data.drop(data[data['user score'] =='tbd'].index)
    # mean = mean['user score']
    # mean = mean.astype(np.float64)
    # meanVal = mean.mean()
    # data.replace('tbd', {'user score':meanVal}, inplace = True)
    
    # Los valores de los test se asemejan más al un drop, cambia la linea de arriba por esta para comprobarlo
    data = data.drop(data[data['user score'] =='tbd'].index)
    
    data['user score'] = data['user score'].astype(np.float64)
    
    data['score'] = data['score'].astype(np.float64)
    data['score'] = data['score'].fillna(0)
    data["score"] = data["score"] / 10
    return data


def load_data_csv(path,x_colum,y_colum):
    data = pd.read_csv(path)
    data = cleanData(data)
    X = data[x_colum].to_numpy()
    y = data[y_colum].to_numpy()
    
    return X, y

def plot_data(x):

    plt.scatter(x['user score'], x['score'], marker = '.')
    plt.xlabel('User Score')
    plt.ylabel('Score')
    x.plot()
    plt.show()
    return

def plot_history(j_history, num_iterations):

    plt.plot(range(1, num_iterations + 1), j_history, color='r')
    plt.xlabel('Iteraciones')
    plt.ylabel('Coste')
    plt.title('Curva de aprendizaje')
    plt.show()

def plot_linear_regression(x_train,y_train,w,b):
    
    plt.scatter(x_train, y_train, marker='.', label='Datos')
    plt.plot(x_train, w * x_train + b, color='r', label='Regresion Lineal (Prediccion)')
    plt.xlabel('Score (1-10)')
    plt.ylabel('User score (1-10)')
    plt.legend()
    plt.show()