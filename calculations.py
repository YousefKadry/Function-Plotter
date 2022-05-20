import numpy as np

class Calculations:
    def __init__(self):
        pass

    def evaluation(self, equation, min, max):
    #parameters: f(x), min value, max value
    #returns: x list (x values), y list (f(x))
        e = equation.replace('^', '**')
        x_val = np.linspace(min, max, 1000)
        y_val = []

        for x in x_val:
            y_val.append(eval(e))
        return x_val, y_val
