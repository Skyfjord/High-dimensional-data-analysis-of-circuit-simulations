import scipy.io
import numpy as np

def pydict(filename):
    
    """ Converts mat datafiles to python dictionaries which can be accessed using the variable names 
        Use .keys() function to find variable names"""

    mat = scipy.io.loadmat(filename)

    for key in mat.keys():
        if type(mat[key]) == np.ndarray: #there will be some unnecessary informationn with the file, this condition filters them out


            if mat[key].shape[0]==1: # changing arrays of the format (1,10000) to one dimensional arrays
                mat[key]=np.transpose(mat[key])
                mat[key]=np.array([elem[0] for elem in mat[key]])


            elif mat[key].shape[1]==1: # changing arrays of the format (10000,1) to one dimnesional arrays
                mat[key]=np.array([elem[0] for elem in mat[key]])

    return mat

def equation(filename):

    """ converts mat equations to list of strings and names of parameters used (parameters are the last string)"""

    mat=scipy.io.loadmat(filename)
    eqs=str(mat["y_f"]).replace(" ","").replace(".^","**").replace(".*","*").replace("exp","e**").replace("./","/") 
    eqs=eqs[eqs.find("0@")+2:] #attempt to generalize may not work for other exapmles
    start=eqs.find("[") #another attempt to generalize, more likely to work for other examples
    var=eqs[:start] #extracting variables
    eqs=eqs[start+1:eqs.find("]")]
    eqs=eqs.split(",")
    eqs.append(var) # adding variables to end of list of equations, remember to remove before performing eval on equations

    return eqs