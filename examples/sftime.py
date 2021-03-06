''' This test shows the stream function around a circular inclusion'''
def sft():
    import Inclusions as II
    import numpy as np

    Lx = 1.
    Ny = 101
    Ly = Lx
    Nx = Ny
    grid = II.setup_grid(Lx, Ny)

    kperm = np.ones([Ny, Nx])
    dx = Lx/(Nx-1)
    dy = Ly/(Ny-1)
    x1 = np.arange(0.0, Lx+dx, dx)
    y1 = np.arange(0.0, Ly+dy, dy)
    xx, yy = np.meshgrid(x1, y1)
    r = 0.1
    Kfactor = 0.1
    mask = ((xx - 0.5)**2.0 + (yy - 0.5)**2.0) < r**2.0
    kperm[mask] = Kfactor
    psi = II.stream_function(grid, kperm, isPeriodic=False, plotPsi=False)
    return True

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("sft()", setup="from __main__ import sft",number=1))

