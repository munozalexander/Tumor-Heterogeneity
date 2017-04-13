import numpy as np
import itertools

def create_Z (num_clones, clone_muts, print_bool=False):
    '''
    num_clones: int for number of clones in [3,4,5]
    clone_muts:
    if num_clones==3: [ c1,c2,c3,
                        c1c2,c1c3,c2c3,
                        c1c2c3 ]
    if num_clones==4: [ c1,c2,c3,c4
                        c1c2,c1c3,c1c4,c2c3,c2c4,c3c4,
                        c1c2c3,c1c2c4,c1c3c4,c2c3c4,
                        c1c2c3c4 ]
    if num_clones==5: [ c1,c2,c3,c4,c5
                        c1c2,c1c3,c1c4,c1c5,c2c3,c2c4,c2c5,c3c4,c3c5,c4c5,
                        c1c2c3,c1c2c4,c1c2c5,c1c3c4,c1c3c5,c1c4c5,c2c3c4,c2c3c5,c2c4c5,c3c4c5,
                        c1c2c3c4,c1c2c3c5,c1c2c4c5,c1c3c4c5,c2c3c4c5,
                        c1c2c3c4c5 ]

    '''
    z_mat = []

    #confirm correct clone_muts list, there are 2^n-1 possible non-empty subsets of clones
    if len(clone_muts) != (2**num_clones - 1):
        print("Invalid clone_muts list size.")
        return

    else:
        #generate possible rows for Z, first column should be all zero, then iterate through permutations of 1 and 0
        possible_seqs = []
        for num_ones in range(num_clones):
            possible_seqs += [[0]+np.bincount(xs, minlength=num_clones).tolist()\
                             for xs in itertools.combinations(range(num_clones), (num_ones+1))]

        #append possible seqs according to user-defined phylogenetics
        for pairing_index in range(len(clone_muts)):
            for i in range(clone_muts[pairing_index]):
                z_mat.append(possible_seqs[pairing_index])

        #print
        if print_bool==True:
            print("Successfully generated Z matrix for %i clones:" % num_clones)
            print(z_mat)
        return z_mat

##### EXAMPLES #####
# dist = create_Z(3,[4,1,2,0,0,3,5], print_bool=True)# dist2 = create_Z(3,[3,4,1,0,5,1,1], print_bool=True)
# dist3 = create_Z(5,[1,1,1,1,1,1,2,3,0,0,0,0,0,0,0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,5], print_bool=True)
