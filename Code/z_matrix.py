import numpy as np

def create_Z (num_clones, clone_muts):
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
    z_mat = np.zeros()
    if len(clone_muts) != (2**num_clones - 1): #2^n-1 possible subsets of clones
        print("Invalid clone_muts list size!")
        return

    if arg1 == 3:
        for x in range(arg2[0]):
            dist.append([0,1,0,0])
        for x in range(arg2[1]):
            dist.append([0,0,1,0])
        for x in range(arg2[2]):
            dist.append([0,0,0,1])
        for x in range(arg2[3]):
            dist.append([0,1,1,0])
        for x in range(arg2[4]):
            dist.append([0,1,0,1])
        for x in range(arg2[5]):
            dist.append([0,0,1,1])
        for x in range(arg2[6]):
            dist.append([0,1,1,1])
    elif arg1 == 4:
        for x in range(arg2[0]):
            dist.append([0,1,0,0,0])
        for x in range(arg2[1]):
            dist.append([0,0,1,0,0])
        for x in range(arg2[2]):
            dist.append([0,0,0,1,0])
        for x in range(arg2[3]):
            dist.append([0,0,0,0,1])
        for x in range(arg2[4]):
            dist.append([0,1,1,0,0])
        for x in range(arg2[5]):
            dist.append([0,1,0,1,0])
        for x in range(arg2[6]):
            dist.append([0,1,0,0,1])
        for x in range(arg2[7]):
            dist.append([0,0,1,1,0])
        for x in range(arg2[8]):
            dist.append([0,0,1,0,1])
        for x in range(arg2[9]):
            dist.append([0,0,0,1,1])
        for x in range(arg2[10]):
            dist.append([0,1,1,1,0])
        for x in range(arg2[11]):
            dist.append([0,1,1,0,1])
        for x in range(arg2[12]):
            dist.append([0,1,0,1,1])
        for x in range(arg2[13]):
            dist.append([0,0,1,1,1])
        for x in range(arg2[14]):
            dist.append([0,1,1,1,1])
    else:
        for x in range(arg2[0]):
            dist.append([0,1,0,0,0,0])
        for x in range(arg2[1]):
            dist.append([0,0,1,0,0,0])
        for x in range(arg2[2]):
            dist.append([0,0,0,1,0,0])
        for x in range(arg2[3]):
            dist.append([0,0,0,0,1,0])
        for x in range(arg2[4]):
            dist.append([0,0,0,0,0,1])
        for x in range(arg2[5]):
            dist.append([0,1,1,0,0,0])
        for x in range(arg2[6]):
            dist.append([0,1,0,1,0,0])
        for x in range(arg2[7]):
            dist.append([0,1,0,0,1,0])
        for x in range(arg2[8]):
            dist.append([0,1,0,0,0,1])
        for x in range(arg2[9]):
            dist.append([0,0,1,1,0,0])
        for x in range(arg2[10]):
            dist.append([0,0,1,0,1,0])
        for x in range(arg2[11]):
            dist.append([0,0,1,0,0,1])
        for x in range(arg2[12]):
            dist.append([0,0,0,1,1,0])
        for x in range(arg2[13]):
            dist.append([0,0,0,1,0,1])
        for x in range(arg2[14]):
            dist.append([0,0,0,0,1,1])
        for x in range(arg2[15]):
            dist.append([0,1,1,1,0,0])
        for x in range(arg2[16]):
            dist.append([0,1,1,0,1,0])
        for x in range(arg2[17]):
            dist.append([0,1,1,0,0,1])
        for x in range(arg2[18]):
            dist.append([0,1,0,1,1,0])
        for x in range(arg2[19]):
            dist.append([0,1,0,1,0,1])
        for x in range(arg2[20]):
            dist.append([0,1,0,0,1,1])
        for x in range(arg2[21]):
            dist.append([0,0,1,1,1,0])
        for x in range(arg2[22]):
            dist.append([0,0,1,1,0,1])
        for x in range(arg2[23]):
            dist.append([0,0,1,0,1,1])
        for x in range(arg2[24]):
            dist.append([0,0,0,1,1,1])
        for x in range(arg2[25]):
            dist.append([0,1,1,1,1,0])
        for x in range(arg2[26]):
            dist.append([0,1,1,1,0,1])
        for x in range(arg2[27]):
            dist.append([0,1,1,0,1,1])
        for x in range(arg2[28]):
            dist.append([0,1,0,1,1,1])
        for x in range(arg2[29]):
            dist.append([0,0,1,1,1,1])
        for x in range(arg2[30]):
            dist.append([0,1,1,1,1,1])
    return dist

dist = Z_mtx_creation(3,[4,1,2,0,0,3,5])
print(np.array(dist))
# dist = Z_mtx_creation(3,[3,4,1,0,5,1,1])
# dist2 = Z_mtx_creation(5,[1,1,1,1,1,1,2,3,0,0,0,0,0,0,0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,5])
# print(dist)
# print(dist2)
