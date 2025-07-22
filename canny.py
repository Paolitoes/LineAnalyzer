import numpy as np
from scipy import signal

def MyCanny(img: np.array):
    scharr = np.array([[ -3-3j,0-10j,+3 -3j],
                       [-10+0j,0+0j,+10 +0j],
                       [ -3+3j,0+10j,+3 +3j]])
    grad2d = signal.convolve2d(img,scharr,boundary="symm",mode='same')

    gradI  = np.arctan2(np.imag(grad2d),np.real(grad2d))

    return gradI
    

