import numpy as np
from scipy.integrate import quad_vec

# THIS NEEDS TO BE OPTIMIZED SO THAT IT RUNS WAY FASTER - CURRENT MAIN BOTTLENECK FOR PROGRAM

def comp_calc(dB_dt : callable, lower_lim : float, upper_lim : float, x : float, y : float, z : float):
    comp = quad_vec(dB_dt, lower_lim, upper_lim, args=(x, y, z))[0]
    if type(comp) == float:
        comp = np.full(z.shape, comp)
    return comp


def B(lower_lim : float, upper_lim : float, dBxdt : callable, dBydt : callable, 
      dBzdt : callable, x : float, y : float, z : float) -> np.ndarray:
    '''Integrate dBdt along the length of the wire for a given point in space
    '''
    x_comp = comp_calc(dBxdt, lower_lim, upper_lim, x, y, z)
    y_comp = comp_calc(dBydt, lower_lim, upper_lim, x, y, z)
    z_comp = comp_calc(dBzdt, lower_lim, upper_lim, x, y, z)

    return np.array([x_comp, y_comp, z_comp])
