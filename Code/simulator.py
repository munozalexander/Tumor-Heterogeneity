import numpy as np
import pandas as pd

##### SIMULATOR IMPLEMENTATION #####

class Simulator(object):
    ''' N is number of loci, M is number of samples, D_locus is average read depth per locus,
        c_range is possible number of clones to test '''

    def __init__(self, loci_num, samples_num, locus_read_depth, clone_test_vals=[3,4,5]):
        self.N = loci_num
        self.M = samples_num
        self.D_locus = locus_read_depth
        self.c_range = clone_test_vals

    def simulate_R(self, print_bool=False):
        simulated_R = np.zeros((self.N,self.M))
        for col_num in range(self.M):
            simulated_R[:,col_num] = np.random.multinomial(self.D_locus * self.N, [1/self.N]*self.N)
        if print_bool:
            print(simulated_R)
        return simulated_R

    def simulate_Zs(self, p, print_bool=False):
        simulated_Zs = [np.zeros((self.N, c)) for c in self.c_range]
        for z_index in range(len(simulated_Zs)):
            simulated_z = simulated_Zs[z_index]
            for col_idx in range(simulated_z.shape[1]-1):
                simulated_Zs[z_index][:,col_idx+1] = [np.random.binomial(1,p) for j in range(simulated_z.shape[0])]
        if print_bool:
            print(simulated_Zs)
        return simulated_Zs

    def simulate_Ps(self, print_bool=False):
        simulated_Ps = [np.zeros((c, self.M)) for c in self.c_range]
        for p_index in range(len(simulated_Ps)):
            simulated_Ps[p_index][0,0] = 1
            simulated_p = simulated_Ps[p_index]
            for col_idx in range(simulated_p.shape[1]-1):
                curr_col = np.array([np.random.uniform() for j in range(simulated_p.shape[0])])
                simulated_Ps[p_index][:,col_idx+1] = curr_col / np.sum(curr_col)
        if print_bool:
            print(simulated_Ps)
        return simulated_Ps

    def simulate_Xs_R (self, p=0.7, print_bool=False):
        simulated_R = self.simulate_R()
        simulated_Zs = self.simulate_Zs(p=p)
        simulated_Ps = self.simulate_Ps()
        simulated_Xs = [np.zeros((self.N, self.M)) for c in self.c_range]
        for x_index in range(len(simulated_Xs)):
            for x_row in range(self.N):
                for x_col in range(self.M):
                    simulated_Xs[x_index][x_row, x_col] = \
                    np.random.binomial(simulated_R[x_row, x_col], \
                                       0.5*np.dot(simulated_Zs[x_index][x_row,:], \
                                                  simulated_Ps[x_index][:, x_col]))
        if print_bool:
            print(simulated_Xs)
        return (simulated_Xs, simulated_R)

    def simulate_Vs (self, simulated_Xs, simulated_R, print_bool=False):
        #let V be the percent variant reads at each locus and sample, [N x M] matrix
        simulated_Vs = []
        for i in range(len(simulated_Xs)):
            simulated_V_curr = simulated_Xs[i] / simulated_R
            simulated_Vs.append(simulated_V_curr)
        if print_bool:
            for idx in range(len(simulated_Vs)):
                print("Testing with %i clones." % self.c_range[idx])
                print("V shape: ", simulated_Vs[idx].shape)
                print(simulated_Vs[idx])
                print()
        return simulated_Vs
