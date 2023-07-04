import numpy as np
import matplotlib.pyplot as plt

import matTo

sampleno=2000

dim=5

limit1=-30
limit2=-50

mat = matTo.pydict('/Users/jason/Desktop/IISC/matfiles/Params.mat')

dim_names = ["L1","L2","L3","C1","C2"]

L1,L2,L3,C1,C2 = mat['L1'],mat['L2'],mat['L3'],mat['C1'],mat['C2']

L1 = np.log10(L1)
L2 = np.log10(L2)
L3 = np.log10(L3)
C1 = np.log10(C1)
C2 = np.log10(C2)
L1max,L1min=max(L1),min(L1)
L2max,L2min=max(L2),min(L2)
L3max,L3min=max(L3),min(L3)
C1max,C1min=max(C1),min(C1)
C2max,C2min=max(C2),min(C2)
L1 = (L1-min(L1))/(max(L1)-min(L1))
L2 = (L2-min(L2))/(max(L2)-min(L2))
L3 = (L3-min(L3))/(max(L3)-min(L3))
C1 = (C1-min(C1))/(max(C1)-min(C1))
C2 = (C2-min(C2))/(max(C2)-min(C2))

mat = matTo.pydict('/Users/jason/Desktop/IISC/matfiles/Insertion loss.mat')

frequencies = mat["freq_vect"]

Ins_losses = np.transpose(mat["Il_dB"])

dataP=[]
dataN=[]
dataC=[]
dataO=[]

for i in range(sampleno):

    cond_point1=[Ins_losses[i][j]-limit1 for j in range(len(frequencies)) if 2e6 < frequencies[j] < 6e6]
    cond_point2=[Ins_losses[i][j]-limit2 for j in range(len(frequencies)) if 30e6 < frequencies[j] < 50e6]

    if 0 > max(cond_point1) > -3 and 0 > max(cond_point2) > -3:
        dataC.append([L1[i],L2[i],L3[i],C1[i],C2[i]])

    if -15 > max(cond_point1) and -15 > max(cond_point2):
        dataO.append([L1[i],L2[i],L3[i],C1[i],C2[i]])

    if 0 > max(cond_point1) and 0 > max(cond_point2):
        dataP.append([L1[i],L2[i],L3[i],C1[i],C2[i]])#,max(cond_point1),max(cond_point2)])
    else:
        dataN.append([L1[i],L2[i],L3[i],C1[i],C2[i]])#,max(cond_point1),max(cond_point2)])

        # plt.plot(frequencies,Ins_losses[i])


targetP=["Pass"]*len(dataP)
targetN=["Fail"]*len(dataN)
targetC=["Crictical"]*len(dataC)
targetO=["Overdesigned"]*len(dataO)

target=targetP+targetN
data=dataP+dataN

def original_coordinate(norm_coord):
    
    l1=L1min+norm_coord[0]*(L1max-L1min)  
    l2=L2min+norm_coord[1]*(L2max-L2min)
    l3=L3min+norm_coord[2]*(L3max-L3min)
    c1=C1min+norm_coord[3]*(C1max-C1min)
    c2=C2min+norm_coord[4]*(C2max-C2min)

    return 10**l1,10**l2,10**l3,10**c1,10**c2
