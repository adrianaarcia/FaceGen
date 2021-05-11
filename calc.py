import numpy as np

def normalize(x):
    z = []

    min_val = min(x)
    d = max(x) - min_val

    # if d == 0:
    #     return np.zeros(len(x))

    for xi in x:
        zi = (xi - min_val)/d
        z.append(zi)

    return z

def normalize_multi(xs):
    zs = [[] for x in xs]
    flat = [xi for x in xs for xi in x]

    min_val = min(flat)
    d = max(flat) - min_val

    for i in range(len(xs)):
        x = xs[i]
        z = zs[i]
        for xi in x:
            zi = (xi - min_val)/d
            z.append(zi)
    
    return zs

def norms(verts1, verts2):
    norms = []
    n = len(verts1)

    # if n != len(verts2):
    #     raise ValueError('Arrays must be the same size!')
    
    for i in range(n):
        v1 = verts1[i]
        v2 = verts2[i]
        norms.append(np.linalg.norm(v1-v2))
    return norms