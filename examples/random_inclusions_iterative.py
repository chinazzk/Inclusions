'''This example simulates flow and transport in a domain with
 a random arangement of inclusions.'''
from Inclusions import *
run_simulation(Lx=1., Ny=400,
                   pack='rnd',n_incl_y=10, Kfactor=0.1,
                   target_incl_area=0.4, radius=None,
                   bcc='flow', isPeriodic=True, integrateInTime=False,
                   tmax=9e4, dt=None, Npart=int(1e4),
                   plotPerm=False, plotFlow=False,
                   plotTpt=False, plotBTC=True,
                   filename='test-rnd-iter', doPost=True,
                   directSolver=False, tol=1e-10, maxiter=2000)
