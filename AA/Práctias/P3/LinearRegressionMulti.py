import numpy as np
import copy
import math
from LinearRegression import LinearReg


class LinearRegMulti(LinearReg):

    """
    Computes the cost function for linear regression.

    Args:
        x (ndarray): Shape (m,) Input to the model
        y (ndarray): Shape (m,) the real values of the prediction
        w, b (scalar): Parameters of the model
        lambda: Regularization parameter. Most be between 0..1. 
        Determinate the weight of the regularization.
    """
    #Supuestamente esto hereda de la clase padre pero la sobreescribimos?
    def __init__(self, x, y, w, b, lambda_):
        super().__init__(x, y, w, b)
        self.lambda_ = lambda_
        self.m = x.shape[0]

    """
    Compute the regularization cost (is private method: start with _ )
    This method will be reuse in the future.

    Returns
        _regularizationL2Cost (float): the regularization value of the current model
    """
    
    def _regularizationL2Cost(self):
        w = self.w ** 2
        reg_cost = np.sum(w)
        reg_cost_final = (self.lambda_ / (2 * self.m)) * reg_cost
        return reg_cost_final
    
    """
    Compute the regularization gradient (is private method: start with _ )
    This method will be reuse in the future.

    Returns
        _regularizationL2Gradient (vector size n): the regularization gradient of the current model
    """ 
    
    def _regularizationL2Gradient(self):
        reg_gradient_final = (self.lambda_ / self.m) * self.w
        return reg_gradient_final

    """
    Computes the linear regression function.
    # f(w,b) = w * x + b

    Args:
        x (matrix): Shape (m,n) Input to the model
    
    Returns:
        the linear regression value
    """
    def f_w_b_multi(self, x):
        return self.w @ x.T + self.b
    
    """
    Computes the cost function for linear regression.

    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    def compute_cost(self):
        
        # Esta es la formula de coste de la funcion
        # Mean Squared Error formula
        squared_error = np.sum((self.f_w_b_multi(self.x)-self.y) ** 2) / (2*self.m) 
        squared_error = squared_error + self._regularizationL2Cost()

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
    
    def compute_gradient(self):

        dj_dw = 0
        dj_db = 0
        
        # Check Transpose
        dj_dw = ((self.f_w_b_multi(self.x) - self.y) @ self.x ) / self.m
        dj_db = np.sum(self.f_w_b_multi(self.x) - self.y) / self.m
        dj_dw = dj_dw + self._regularizationL2Gradient()
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
        
        for i in range(0,num_iters):
            dj_dw, dj_db = self.compute_gradient()
            self.w -= alpha * dj_dw
            self.b -= alpha * dj_db
            J_history[i] = self.compute_cost() 

        return self.w, self.b, J_history, w_initial, b_initial
    

    
def cost_test_multi_obj(x,y,w_init,b_init):
    lr = LinearRegMulti(x,y,w_init,b_init,0)
    cost = lr.compute_cost()
    return cost

def compute_gradient_multi_obj(x,y,w_init,b_init):
    lr = LinearRegMulti(x,y,w_init,b_init,0)
    dw,db = lr.compute_gradient()
    return dw,db
