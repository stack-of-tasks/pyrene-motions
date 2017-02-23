# q_t is the time sequence of Joint states of the format (robot.nq, number_of_time_steps)
def writeJointStateToFile(q_t, filename):
    n_time_steps = q_t.shape[1]
    robot_nq = q_t.shape[0]
    file_q = open(filename,"w")
    DELIMITOR = " "
    NEWLINE = "\n"
    for k in xrange(n_time_steps):
        line = ""
        for n in xrange(robot_nq):
            if n == robot_nq-1:
                line += str(q_t[n,k]) + NEWLINE
            else:
                line += str(q_t[n,k]) + DELIMITOR
        file_q.write(line)
    file_q.close()

def writeXYZasCSVFile(filename, x,y,z=None):
    DELIMITOR = ", "
    NEWLINE = "\n"
    file_xyz = open(filename, "w")
    if z is None:
        tup_list = zip(x,y)
    else:
        tup_list = zip(x,y,z)
    for tup in tup_list:
        line = ""
        for ind,val in enumerate(tup):
            if ind == len(tup)-1:
                line+= str(val)+NEWLINE
            else:
                line+=str(val)+DELIMITOR
        file_xyz.write(line)
    file_xyz.close()

def parseJointStatesFromFile(filename):
    import pandas as pd
    import numpy as np
    DELIMITOR=" "
    dt = 0.001
    seq = np.array(pd.read_csv(filename,header=None, delim_whitespace=True)).T
    return seq
