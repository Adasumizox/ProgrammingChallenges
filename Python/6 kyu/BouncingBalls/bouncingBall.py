from math import log

def bouncingBall(h, bounce, window):
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    return 1 + 2*int(log(window/float(h), bounce))