import numpy as np
import copy
import math
import datetime

class LinearReg:
    
    """
    Computes the cost function for linear regression.

    Args:
        x (ndarray): Shape (m,) Input to the model
        y (ndarray): Shape (m,) the real values of the prediction
        w, b (scalar): Parameters of the model
    """
    #Self es la instancia interna de la clase
    def __init__(self, x, y, w, b):
        self.x = x
        self.y = y
        self.w = w
        self.b = b

    """
    Computes the linear regression function.
    # f(w,b) = w * x + b

    Args:
        x (ndarray): Shape (m,) Input to the model
    
    Returns:
        the linear regression value
    """

    # Esto ya viene hecho?
    def f_w_b(self, x):
        return self.w * x + self.b

    """
    Computes the cost function for linear regression.

    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    def compute_cost_iterative(self):
        
        squared_error = 0
        m = len(self.x) # Tamaño de la entrada
    
        # Mean Squared Error formula: iterative version
        for i in range(m):
            error = self.w * self.x[i] + self.b # Alternativamente podemos usar f_w_b
            squared_error += (error-self.y[i]) ** 2 
    
        total_cost = squared_error / (2*m)
        return total_cost    

    def compute_cost(self):
        
        m = len(self.y) # Tamaño de la entrada
    
        # Esta es la formula de coste de la funcion
        # Mean Squared Error formula
        squared_error = np.sum((self.f_w_b(self.x)-self.y) ** 2) / (2*m) 
    
        #total_cost = (1 / (2 * m)) * np.sum(squared_error)
        return squared_error    

    """
    Computes the gradient for linear regression 
    Args:
      x (ndarray): Shape (m,) Input to the model (Population of cities) 
      y (ndarray): Shape (m,) Label (Actual profits for the cities)
      w, b (scalar): Parameters of the model  

    Returns
      dj_dw (scalar): The gradient of the cost w.r.t. the parameters w
      dj_db (scalar): The gradient of the cost w.r.t. the parameter b     
     """
    def compute_gradient_iterative(self):

        dj_dw = 0
        dj_db = 0
        m = len(self.x)
        
        for i in range(m):
            #hypothesis = self.w * self.x[i] + self.b
            dj_dw += (self.f_w_b(self.x[i]) - self.y[i]) * self.x[i]
            dj_db += (self.f_w_b(self.x[i]) - self.y[i])

        dj_dw/=m
        dj_db/=m
        
        return dj_dw, dj_db

    def compute_gradient(self):

        dj_dw = 0
        dj_db = 0
        m = len(self.x)
        
        dj_dw = np.sum((self.f_w_b(self.x) - self.y) * self.x ) / m
        dj_db = np.sum(self.f_w_b(self.x) - self.y) / m
        
        return dj_dw, dj_db
    
    """
    Performs batch gradient descent to learn theta. Updates theta by taking 
    num_iters gradient steps with learning rate alpha

    Args:
      alpha : (float) Learning rate
      num_iters : (int) number of iterations to run gradient descent
    Returns
      w : (ndarray): Shape (1,) Updated values of parameters of the model after
          running gradient descent
      b : (scalar) Updated value of parameter of the model after
          running gradient descent
      J_history : (ndarray): Shape (num_iters,) J at each iteration,
          primarily for graphing later
      w_initial : (ndarray): Shape (1,) initial w value before running gradient descent
      b_initial : (scalar) initial b value before running gradient descent
    """
    def gradient_descent_iterative(self, alpha, num_iters):
        # An array to store cost J and w's at each iteration — primarily for graphing later
        J_history = np.zeros(num_iters)
        w_history = []
        w_initial = copy.deepcopy(self.w)  # avoid modifying global w within function
        b_initial = copy.deepcopy(self.b)  # avoid modifying global b within function
        
        init = datetime.datetime.now()
        for i in range(num_iters):
            dj_dw, dj_db = self.compute_gradient_iterative()
            self.w -= alpha * dj_dw
            self.b -= alpha * dj_db
            J_history[i] = self.compute_cost_iterative()

        print(f'Tiempo de procesamiento gradiente \033[91m iterativo: {datetime.datetime.now()-init}\033[0m')
        return self.w, self.b, J_history, w_initial, b_initial

    def gradient_descent(self, alpha, num_iters):
        # An array to store cost J and w's at each iteration — primarily for graphing later
        J_history = np.zeros(num_iters)
        w_history = []
        w_initial = copy.deepcopy(self.w)  # avoid modifying global w within function
        b_initial = copy.deepcopy(self.b)  # avoid modifying global b within function
        
        init = datetime.datetime.now()
        for i in range(0,num_iters):
            dj_dw, dj_db = self.compute_gradient()
            self.w -= alpha * dj_dw
            self.b -= alpha * dj_db
            J_history[i] = self.compute_cost()
        print(f'Tiempo de procesamiento gradiente \033[91m vectorial: {datetime.datetime.now()-init}\033[0m')
        

        return self.w, self.b, J_history, w_initial, b_initial


def cost_test_obj_it(x,y,w_init,b_init):
    lr = LinearReg(x,y,w_init,b_init)
    cost = lr.compute_cost_iterative()
    return cost

def cost_test_obj(x,y,w_init,b_init):
    lr = LinearReg(x,y,w_init,b_init)
    cost = lr.compute_cost()
    return cost

def compute_gradient_obj_it(x,y,w_init,b_init):
    lr = LinearReg(x,y,w_init,b_init)
    dw,db = lr.compute_gradient_iterative()
    return dw,db

def compute_gradient_obj(x,y,w_init,b_init):
    lr = LinearReg(x,y,w_init,b_init)
    dw,db = lr.compute_gradient()
    return dw,db