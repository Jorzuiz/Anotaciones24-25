from MLP import MLP, target_gradient, costNN, MLP_backprop_predict
from utils import load_data, load_weights,one_hot_encoding, accuracy
from public_test import checkNNGradients,MLP_test_step
from sklearn.model_selection import train_test_split
from sklearn.neural_network  import MLPClassifier
from sklearn.metrics import accuracy_score



"""
Test 1 to be executed in Main
"""
def gradientTest():
    checkNNGradients(costNN,target_gradient,0)
    checkNNGradients(costNN,target_gradient,1)


"""
Test 2 to be executed in Main
"""
def MLP_test(X_train,y_train, X_test, y_test):
    print("We assume that: random_state of train_test_split  = 0 alpha=1, num_iterations = 2000, test_size=0.33, seed=0 and epislom = 0.12 ")
    print("Test 1 Calculando para lambda = 0")
    MLP_test_step(MLP_backprop_predict,1,X_train,y_train,X_test,y_test,0,2000,0.92606,2000/10)
    print("Test 2 Calculando para lambda = 0.5")
    MLP_test_step(MLP_backprop_predict,1,X_train,y_train,X_test,y_test,0.5,2000,0.92545,2000/10)
    print("Test 3 Calculando para lambda = 1")
    MLP_test_step(MLP_backprop_predict,1,X_train,y_train,X_test,y_test,1,2000,0.92667,2000/10)

def SKLearn_test(X_train, y_train, X_test, y_test, alpha, lambda_, num_ite, baseLineAccuracy, verbose =0):
    
    # Modelo iniciado para entrenar con nuestros datos, usa optimizador ADAM
    # El numero neuronas en la capa itnermedia es de 25
    # Parametro de regularizacion para la L2 se llama alpha y suele ser de 0.05
    # Max iter es el limite de "generaciones" para entrenar la red neuronal
    mlp = MLPClassifier(hidden_layer_sizes=(25,), alpha = lambda_, max_iter=num_ite)

    # Ajustamos los datos al modelo cargado en mlp
    # X_train contiene la matriz de tamaño n_samples * n_features
    # y_train es un vector de etiquetas de tamaño (n_samples,) SIN one-hot encoding
    mlp.fit(X_train, y_train)

    # Le pedimos al modelo que prediga el valor de X_test
    y_pred = mlp.predict(X_test)

    # Sacamos la puntuación de precisión del entrenamiento-
    accu = accuracy_score(y_pred, y_test)
    print(f"Calculate accuracy for lambda = {(lambda_):1.5f} : {(accu):1.5f} expected accuracy is aprox: {(baseLineAccuracy):1.5f}")

def MLP_test_sklearn(X_train,y_train, X_test, y_test):
    print("We assume that: random_state of train_test_split  = 0 alpha=1, num_iterations = 2000, test_size=0.33, seed=0 and epislom = 0.12 ")
    print("Test 1 Calculando para lambda = 0")
    SKLearn_test(X_train, y_train, X_test, y_test, 1, 0, 2000, 0.92606, 2000/10)
    print("Test 2 Calculando para lambda = 0.5")
    SKLearn_test(X_train,y_train,X_test,y_test, 1, 0.5,2000,0.92545,2000/10)
    print("Test 3 Calculando para lambda = 1")
    SKLearn_test(X_train,y_train,X_test,y_test,1, 1,2000,0.92667,2000/10)



def main():
    print("Main program")
    #Test 1
    #gradientTest()

    ## TO-DO: descoment both test and create the needed code to execute them.
    
    #Test 2
    #MLP_test()

    

main()