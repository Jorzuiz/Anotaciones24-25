import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cleanData(data):
    
    data = data.drop(data[data['user score'] =='tbd'].index)
    data['user score'] = data['user score'].astype(np.float64)
    data['user score'] = data['user score'].fillna(0)
    
    data['score'] = data['score'].astype(np.float64)
    data['score'] = data['score'].fillna(0)
    data['score'] = data['score'] / 10

    data['users'] = data['users'].astype(np.float64)
    data['users'] = data['users'].fillna(0)
    
    data['critics'] = data['critics'].astype(np.float64)
    data['critics'] = data['critics'].fillna(0)
    return data

def load_data_csv(path,x_colum,y_colum):
    data = pd.read_csv(path)
    data = cleanData(data)
    X = data[x_colum].to_numpy()
    y = data[y_colum].to_numpy()
    return X, y

def zscore_normalize_features(X):
    """
    computes  X, zcore normalized by column

    Args:
      X (ndarray (m,n))     : input data, m examples, n features

    Returns:
      X_norm (ndarray (m,n)): input normalized by column
      mu (ndarray (n,))     : mean of each feature
      sigma (ndarray (n,))  : standard deviation of each feature
    """    
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    X_norm = (X - mu) / sigma
    return X_norm, mu, sigma

def load_data_csv_multi(path,x1_colum,x2_colum,x3_colum,y_colum):
    data = pd.read_csv(path)
    data = cleanData(data)
    x1 = data[x1_colum].to_numpy()
    x2 = data[x2_colum].to_numpy()
    x3 = data[x3_colum].to_numpy()
    X = np.array([x1, x2, x3])
    X = X.T
    y = data[y_colum].to_numpy()
    return X, y

def plot_data(x,y):

    plt.scatter(x[:,0], y, marker = '.')
    plt.xlabel('Score')
    plt.ylabel('User Score')
    plt.show()

    plt.scatter(x[:,1], y, marker = '.')
    plt.xlabel('Critics')
    plt.ylabel('User Score')
    plt.show()

    plt.scatter(x[:,2], y, marker = '.')
    plt.xlabel('Users')
    plt.ylabel('User Score')
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