import numpy as np
from scipy import integrate

from scipy.linalg import expm

# rotates 3D array v around zero by the 3 angles in xyz
def rot_euler(v, xyz):
    ''' Rotate vector v (or array of vectors) by the euler angles xyz '''
    # https://stackoverflow.com/questions/6802577/python-rotation-of-3d-vector
    for theta, axis in zip(xyz, np.eye(3)):
        v = np.dot(np.array(v), expm(np.cross(np.eye(3), axis*-theta)))
    return v

#normalize an array to be in [0,1]
def norm(arr) :
    mx=np.amax(arr)
    mn=np.amin(arr)
    rng=mx-mn
    return [(v-mn)/rng for v in arr]

# lorenz equation
def lorenz_deriv(w, t0, sigma=10., beta=8./3, rho=28.0):
    """Compute the time-derivative of a Lorentz system."""
    x=w[0]
    y=w[1]
    z=w[2]
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]



def makeLorenzTrajectory(tspacing, genlen) :
    # Choose random starting points, uniformly distributed from -15 to 15
    #np.random.seed(1)
    N_trajectories=1
    x0 = -15 + 30 * np.random.random((N_trajectories, 3))
    t = np.linspace(0, tspacing, genlen)
    x_t = np.asarray([integrate.odeint(lorenz_deriv, x0i, t) for x0i in x0])

    # do a random rotation on the lorenz shape, then normalize it *in each dimension* individually
    rx = (rot_euler(np.squeeze(x_t)-.5, 2*np.pi*np.random.rand(3))+.5).transpose()
    nx=np.array([norm(rx[i]) for i in range(3)])

    return nx


    
        
