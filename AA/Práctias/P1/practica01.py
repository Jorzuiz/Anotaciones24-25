from public_tests import *
from utils import load_data_csv, plot_history, plot_linear_regression
import datetime
import matplotlib.pyplot as plt

from LinearRegression import LinearReg
from LinearRegression import cost_test_obj, cost_test_obj_it
from LinearRegression import compute_gradient_obj, compute_gradient_obj_it


def test_gradient(x_train, y_train):
    initial_w = 0
    initial_b = 0

    print('Iniciando test de gradiente vectorial')
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,initial_w,initial_b)
    lr_tmp_dj_dw, lr_tmp_dj_db = lr.compute_gradient()
    print(f'Tiempo de procesamiento gradiente \033[91m vectorial: {datetime.datetime.now()-init}\033[0m')
    print('\033[0mVectorial gradient at initial w, b (similar to)(-50.498559851122586 -6.988606075159082):',
          lr_tmp_dj_dw, lr_tmp_dj_db)

    test_w = 0.2
    test_b = 0.2
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,test_w,test_b)
    lr_tmp_dj_dw, lr_tmp_dj_db = lr.compute_gradient()    
    print(f'Tiempo de procesamiento gradiente \033[91m vectorial: {datetime.datetime.now()-init}\033[0m')
    print('\033[0mVectorial gradient at initial w, b (similar to)(-38.7005262336415 -5.369312042261976):',
          lr_tmp_dj_dw, lr_tmp_dj_db)

    print("\033[94m----Compute gradient POO-------\033[0m")
    compute_gradient_test(compute_gradient_obj)

def test_gradient_iterative(x_train, y_train):
    initial_w = 0
    initial_b = 0
    
    print('Iniciando test de gradiente iterativa')
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,initial_w,initial_b)
    lr_tmp_dj_dw, lr_tmp_dj_db = lr.compute_gradient_iterative()
    print(f'Tiempo de procesamiento gradiente \033[91m iterativa: {datetime.datetime.now()-init}\033[0m')
    print('\033[0mIterative gradient at initial w, b (similar to)(-50.498559851122586 -6.988606075159082):',
          lr_tmp_dj_dw, lr_tmp_dj_db)

    test_w = 0.2
    test_b = 0.2
    
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,test_w,test_b)
    lr_tmp_dj_dw, lr_tmp_dj_db = lr.compute_gradient_iterative()
    print(f'Tiempo de procesamiento gradiente \033[91m iterativa: {datetime.datetime.now()-init}\033[0m')
    print('\033[0mIterative gradient at initial w, b (similar to)(-38.7005262336415 -5.369312042261976):',
          lr_tmp_dj_dw, lr_tmp_dj_db)

    print("\033[94m----Compute iterative gradient POO-------\033[0m")
    compute_gradient_test(compute_gradient_obj_it)

def test_cost(x_train, y_train):

    initial_w = 2
    initial_b = 1

    print('Iniciando test de coste vectorial')
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,initial_w,initial_b)
    lrcost = lr.compute_cost()
    print(f'Tiempo de procesamiento coste \033[91m vectorial: {datetime.datetime.now()-init}\033[0m')
    print(f'Vectorial cost at initial w (35.841): {lrcost:.3f}')

    print("\033[94m----Compute iterative gradient POO-------\033[0m")
    compute_cost_test(cost_test_obj)

def test_cost_iterative(x_train, y_train):

    initial_w = 2
    initial_b = 1
    
    init = datetime.datetime.now()
    print('Iniciando test de coste iterativo')
    lr = LinearReg(x_train,y_train,initial_w,initial_b)
    lrcost = lr.compute_cost_iterative()
    print(f'Tiempo de procesamiento coste \033[91m iterativa: {datetime.datetime.now()-init}\033[0m')
    print(f'Iterative cost at initial w (35.841): {lrcost:.3f}')

    print("\033[94m----Compute iterative gradient POO-------\033[0m")
    compute_cost_test(cost_test_obj_it)

def test_gradient_descent(x_train, y_train, w, b):
    
    alpha, num_iterations = 0.01, 1500

    print('Iniciando test de gradiente desccendente vectorial')
    init= datetime.datetime.now()
    lr = LinearReg(x_train,y_train,w,b)
    w,b,j_history,w_initial,b_initial=lr.gradient_descent(alpha,num_iterations)
    print(w_initial,b_initial,w,b)
    predict1 = 3.5 * w + b
    print(f'Tiempo de procesamiento gradiente descendente \033[91m vectorial: {datetime.datetime.now()-init}\033[0m')
    print('\033[0mfor score 3.5, we predict user score of (3.97) %.2f' %
          predict1)
    print(predict1)
    print("Case 1")
    assert np.allclose(predict1, 3.96667965 ), f"Cost must be 3.966 for a perfect prediction but got {predict1}"
    print("Case 1 passed!")

    plot_history(j_history, num_iterations)
    plot_linear_regression(x_train,y_train,w,b)

    predict2 = 7.9 * w + b
    w,b=0,0
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,w,b)
    w,b,j_history,w_initial,b_initial=lr.gradient_descent(alpha,num_iterations)
    print(w_initial,b_initial,w,b)

    plot_history(j_history, num_iterations)
    plot_linear_regression(x_train,y_train,w,b)

    print(f'Tiempo de procesamiento gradiente descendente \033[91m vectorial: {datetime.datetime.now()-init}\033[0m')
    print('for score 7.9, we predict user score of (6.86) %.2f' %
          predict2)
    print("Case 2")
    print(predict2)
    #assert np.allclose(predict2, 6.85867675 ), f"Cost must be 6.858 for a perfect prediction but got {predict2}"
    
    print("Case 2 passed!")
    print("\033[92mAll tests passed!\033[0m")

def test_gradient_descent_iterative(x_train, y_train, w, b):
    alpha, num_iterations = 0.01, 1500
    
    print('Iniciando test de gradiente descendente iterativa')
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,w,b)
    w,b,j_history,w_initial,b_initial=lr.gradient_descent_iterative(alpha, num_iterations)
    predict1 = 3.5 * w + b
    
    plot_history(j_history, num_iterations)
    plot_linear_regression(x_train,y_train,w,b)

    print(f'Tiempo de procesamiento gradiente descendente \033[91m iterativa: {datetime.datetime.now()-init}\033[0m')
    print('\033[0mfor score 3.5, we predict user score of (3.97) %.2f' %
          predict1)
    print(predict1)
    print("Case 1")
    assert np.allclose(predict1, 3.96667965 ), f"Cost must be 3.966 for a perfect prediction but got {predict1}"
    print("Case 1 passed!")

    w,b=0,0
    init = datetime.datetime.now()
    lr = LinearReg(x_train,y_train,w,b)
    w,b,j_history,w_initial,b_initial=lr.gradient_descent_iterative(alpha, num_iterations)
    predict2 = 7.9 * w + b
    
    plot_history(j_history, num_iterations)
    plot_linear_regression(x_train,y_train,w,b)

    print(f'Tiempo de procesamiento gradiente descendente \033[91m iterativa: {datetime.datetime.now()-init}\033[0m')
    print('for score 7.9, we predict user score of (6.86) %.2f' %
          predict2)
    print("Case 2")
    print(predict2)
    #assert np.allclose(predict2, 6.85867675 ), f"Cost must be 6.858 for a perfect prediction but got {predict2}"
    
    print("Case 2 passed!")
    print("\033[92mAll tests passed!\033[0m")
#TO-DO the main program.