import numpy as np
import copy
import math

class LinearReg:
    
    """
    Computes the cost function for linear regression.

    Args:
        x (ndarray): Shape (m,) Input to the model
        y (ndarray): Shape (m,) the real values of the prediction
        w, b (scalar): Parameters of the model
    """
    #Self es la variable interna de la clase
    def __init__(self, x, y, w, b):
        self.x = x
        self.y = y
        self.w = w
        self.b = b

    """
    Computes the linear regression function.

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
    def compute_cost(self):
        
        m = len(y) # Tamaño de la entrada
        error = self.w * self.x + self.b # Valor esperado
    
        # Esta es la formula de coste de la funcion
        # Mean Squared Error formula
        squared_error = (error-self.y) **2 
    
        total_cost = (1/(2*m)) * np.sum(squared_error)
    
        # No sé que representa o significa self
        return total_cost    

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
    def compute_gradient(self):
        m = len(self.y)
        hypothesis = self.w * self.x + self.b

        dj_dw = np.sum((hypothesis-self.y)*self.x)/m
    
        dj_db = np.sum((hypothesis-self.y))/m
    
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
    def gradient_descent(self, alpha, num_iters):
        # An array to store cost J and w's at each iteration — primarily for graphing later
        J_history = np.zeros(num_iters)
        w_history = []
        w_initial = copy.deepcopy(self.w)  # avoid modifying global w within function
        b_initial = copy.deepcopy(self.b)  # avoid modifying global b within function
        
        for i in range(num_iters):
            dj_dw, dj_db = self.compute_gradient(self)
            self.w-=alpha*dj_dw
            self.b-=alpha*dj_db
            J_history[i]= self.compute_cost(self)

        return self.w, self.b, J_history, w_initial, b_initial


def cost_test_obj(x,y,w_init,b_init):
    lr = LinearReg(x,y,w_init,b_init)
    cost = lr.compute_cost()
    return cost

def compute_gradient_obj(x,y,w_init,b_init):
    lr = LinearReg(x,y,w_init,b_init)
    dw,db = lr.compute_gradient()
    return dw,db