import numpy as np


def projection(data,loading):
    data=np.array(data)
    loading=np.array(loading)
    proj_data=np.dot(data,loading)
    return proj_data


def rotateSlow(data,loadings):
    rot_data=[]
    loadings=np.transpose(np.array(loadings))
    for loading in loadings:
        rot_data.append(projection(data,loading))
    return np.transpose(rot_data)

def rotate(data,loadings):
    data=np.array(data)
    loadings=np.array(loadings)
    return np.dot(data,loadings)

def rem_vector_proj(data,vector):
    data=np.array(data)
    vector=np.array(vector)
    proj=np.dot(data,vector)
    return data-np.outer(proj,vector)
