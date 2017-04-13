from z_matrix import create_Z
from simulator import Simulator
import numpy as np
import itertools


##### INITIALIZE HYPERPARAMETERS #####
loci_num = 50
samples_num = 10
locus_read_depth = 25
clone_test_vals = [3,4,5]
p = 0.7


##### SIMULATE DATA #####
simulator = Simulator(loci_num=loci_num, \
                      samples_num=samples_num, \
                      locus_read_depth=locus_read_depth, \
                      clone_test_vals=clone_test_vals)
simulated_Xs, simulated_R = simulator.simulate_Xs_R(p=p)
simulated_Vs = simulator.simulate_Vs(simulated_Xs=simulated_Xs, simulated_R=simulated_R, print_bool=True)
