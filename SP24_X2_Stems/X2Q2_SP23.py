# region imports
from scipy.integrate import solve_ivp
from math import sin
import numpy as np
from matplotlib import pyplot as plt
# endregion

# region function definitions
def odeSystem(t,X, *args):
    """
    this is the odeSystem callback I'm using for odeint().  The *args contains a callback for the input voltage.
    :param X: the current values of the state variables
    :param t: the current time from odeint
    :param args: fn(t), L, R, C
    :return: list of derivatives of state variables
    """
    #unpack X into convenient variables
    fn, L,R,C=args
    #assign friendly variable names
    i1=#JES Missing Code
    i2=#JES Missing Code
    #calculate the current input voltage
    vt=fn(t)
    #calculate derivatives for the state variables
    i1dot=#JES Missing Code
    i2dot=#JES Missing Code
    return [i1dot, i2dot]

def plot(*args):
    t_range, I1, I2, v = args  # unpack args
    #$JES MISSING CODE  #make the plot
    pass

def main():
    """
    For solving problem 2 on exam.  Note:  I'm passing a callback through solve_ivp to model in input voltage
    :return:
    """
    vin = lambda t:  #$JES MISSING CODE  # a callback to be passed as an argument to odeSystem
    L=20
    R=10
    C=0.05
    myargs=(#$JES MISSING CODE)  # a tuple containing:  (callback for voltage source, L, R, C)
    I0 = [0,0]  # initial conditions I[0]=0, I[1]=0
    tList=np.linspace(0,10,500)  # time vector
    I=solve_ivp(odeSystem,[0,10],I0,t_eval=tList, args=myargs)  #solve using solve_IVP
    VC = #$JES MISSING CODE # create a numpy array of voltage across capacitor as function of time
    #the plotting part
    plot(tList, I.y[0], I.y[1],VC)
    pass
# endregion

# region function calls
if __name__ ==  "__main__":
    main()
# endregion