from MLP import MLP, target_gradient, costNN, MLP_backprop_predict
from utils import load_data, load_weights,one_hot_encoding, accuracy
from public_test import checkNNGradients,MLP_test_step
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import numpy as np



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

"""
MLPClassifier test
"""
def MLPClassifier_test(X_train,y_train, X_test, y_test, alpha, numIterations):
    mlp = MLPClassifier(hidden_layer_sizes=(25,), max_iter=numIterations, alpha=alpha, activation='logistic', random_state=0)

    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)

    accu = accuracy(y_pred, y_test)
    print(f"Accuracy with alpha: {alpha}: {accu:.5f}")
    return accu

"""
Tests de MLP
"""
def testingMLP(X_train, y_train, X_test, y_test):
    print("Testing, attention please (MLPClassifer testing)")
    print("Test 1 Calculando para lambda = 0")
    MLPClassifier_test(X_train, y_train, X_test, y_test, 0, 2000)
    print("Test 2 Calculando para lambda = 0.5")
    MLPClassifier_test(X_train, y_train, X_test, y_test, 0.5, 2000)
    print("Test 3 Calculando para lambda = 1")
    MLPClassifier_test(X_train, y_train, X_test, y_test, 1, 2000)


def main():
    print("Main program")
    x,y = load_data('data/ex3data1.mat') # A lo mejor esto no es necesario?
    y = one_hot_encoding(y)
    mlp = MLP(400, 25, 10, 0, 0.12)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)
    
    #Test 1
    #gradientTest()

    #Test 2
    #MLP_test(X_train,y_train,X_test,mlp.predict(y_test))

    #Test 3
    #testingMLP(X_train, y_train, X_test, y_test)

    

main()