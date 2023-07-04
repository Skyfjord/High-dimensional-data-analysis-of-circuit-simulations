import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi

def to2d(dim,points,color="red",marker="*",angles=[],dimlabel=[],label="",alpha=0.2,s=0.1):

    t = np.linspace(0,2*np.pi,100)
    x = np.cos(t)
    y = np.sin(t) # Drawing a circle with t acting like an angle, 100 points on the unit circle are plotted
    plt.plot(x,y)

    if angles==[]:
        angles = [2*i*np.pi/dim for i in range(dim)] # Getting default angles of the dimensions if angles are not given

    if dimlabel==[]:
        dimlabel=[""]*dim 

    for i in range(dim):
        plt.plot(np.cos(angles[i]),np.sin(angles[i]), marker="o", color="crimson")
        plt.text(np.cos(angles[i]),np.sin(angles[i]), dimlabel[i], fontsize=10.0, fontweight='bold') # Plotting attrtactintg point of dimensions 

    xcor=[]
    ycor=[]

    for point in points: #points contains many datapoints in a list, point contains a datapoint
        cossum = 0
        sinsum = 0
        sum = 0

        for i in range(dim):
            cossum += point[i]*np.cos(angles[i])
            sinsum += point[i]*np.sin(angles[i])
            sum += point[i]
        
        xcor.append(cossum/sum)
        ycor.append(sinsum/sum)

        #sum=1
    plt.scatter(xcor,ycor,marker=marker,color=color,alpha=alpha,label=label,s=s) #Plotting radviz dimension reduced point


def  toPartial3d(dim,points,color="red",marker="*",angles=[],dimlabel=[],alpha=0.2):

    t = np.linspace(0,2*np.pi,100)
    x = np.cos(t)
    y = np.sin(t) # Drawing a circle with t acting like an angle, 100 points on the unit circle are plotted
    plt.plot(x,y)

    if angles==[]:
        angles = [2*i*np.pi/dim for i in range(dim)] # Getting default angles of the dimensions if angles are not given

    if dimlabel==[]:
        dimlabel=[""]*dim 

    for i in range(dim):
        plt.plot(np.cos(angles[i]),np.sin(angles[i]), 0, marker="o", color="crimson")
        #plt.text(np.cos(angles[i]),np.sin(angles[i]), 0, dimlabel[i], fontsize=10.0, fontweight='bold') # Plotting attrtactintg point of dimensions 

    for point in points: #points contains many datapoints in a list, point contains a datapoint
        cossum = 0
        sinsum = 0
        sum = 0

        for i in range(dim):
            cossum += point[i]*np.cos(angles[i])
            sinsum += point[i]*np.sin(angles[i])
            sum += point[i]

        #sum=1

        plt.plot(cossum/sum,sinsum/sum,point[dim],marker=marker,color=color,markersize=2,alpha=alpha)


def halfto2d(dim,points,color="red",marker="*",angles=[],dimlabel=[],alpha=0.2):

    if angles==[]:
        angles = [4*i*np.pi/dim for i in range(dim)]

    if dimlabel==[]:
        dimlabel=[""]*dim 

    plt.subplot(1,2,1)

    t = np.linspace(0,2*np.pi,100)
    x = np.cos(t)
    y = np.sin(t) # Drawing a circle with t acting like an angle, 100 points on the unit circle are plotted
    plt.plot(x,y)

    for i in range(dim//2):
        plt.plot(np.cos(angles[i]),np.sin(angles[i]), marker="o", color="crimson")
        plt.text(np.cos(angles[i]),np.sin(angles[i]), dimlabel[i], fontsize=10.0, fontweight='bold') # Plotting attrtactintg point of dimensions 

    for point in points: #points contains many datapoints in a list, point contains a datapoint
        cossum = 0
        sinsum = 0
        sum = 0

        for i in range(dim//2):
            cossum += point[i]*np.cos(angles[i])
            sinsum += point[i]*np.sin(angles[i])
            sum += point[i]

        plt.plot(cossum/sum,sinsum/sum,marker=marker,color=color,markersize=2,alpha=alpha)

    plt.subplot(1,2,2)

    t = np.linspace(0,2*np.pi,100)
    x = np.cos(t)
    y = np.sin(t) # Drawing a circle with t acting like an angle, 100 points on the unit circle are plotted
    plt.plot(x,y)

    for i in range(dim//2,dim):
        plt.plot(np.cos(angles[i]),np.sin(angles[i]), marker="o", color="crimson")
        plt.text(np.cos(angles[i]),np.sin(angles[i]), dimlabel[i], fontsize=10.0, fontweight='bold') # Plotting attrtactintg point of dimensions 

    for point in points: #points contains many datapoints in a list, point contains a datapoint
        cossum = 0
        sinsum = 0
        sum = 0

        for i in range(dim//2,dim):
            cossum += point[i]*np.cos(angles[i])
            sinsum += point[i]*np.sin(angles[i])
            sum += point[i]

        plt.plot(cossum/sum,sinsum/sum,marker=marker,color=color,markersize=2,alpha=alpha)

    

def from4dto3d(points,color="red",marker="*"):

    plt.plot(1/3**0.5,1/3**0.5,1/3**0.5, marker="o", color="crimson")
    plt.plot(1/3**0.5,-1/3**0.5,-1/3**0.5, marker="o", color="crimson")
    plt.plot(-1/3**0.5,1/3**0.5,-1/3**0.5, marker="o", color="crimson")
    plt.plot(-1/3**0.5,-1/3**0.5,1/3**0.5, marker="o", color="crimson")

    for point in points:
        xsum = point[0] + point[1] - point[2] - point[3]
        ysum = point[0] - point[1] + point[2] - point[3]
        zsum = point[0] - point[1] - point[2] + point[3]
        sum = point[0] + point[1] + point[2] + point[3]

        plt.plot(xsum/sum,ysum/sum,zsum/sum,marker=marker,color=color,markersize=2)

def from6dto3d(points,color="red",marker="*"):

    plt.plot(1,0,0, marker="o", color="crimson")
    plt.plot(-1,0,0, marker="o", color="crimson")
    plt.plot(0,1,0, marker="o", color="crimson")
    plt.plot(0,-1,0, marker="o", color="crimson")
    plt.plot(0,0,1, marker="o", color="crimson")
    plt.plot(0,0,-1, marker="o", color="crimson")

    for point in points:
        xsum = point[0] - point[1]
        ysum = point[2] - point[3]
        zsum = point[4] - point[5]
        sum = point[0] + point[1] + point[2] + point[3] + point[4] + point[5]

        plt.plot(xsum/sum,ysum/sum,zsum/sum,marker=marker,color=color,markersize=2)

def from14dto3d(points,zangle=60,color="red",marker="*",dimlabel=[],alpha=0.1):

    zangle*=pi/180

    if dimlabel==[]:
        dimlabel=[""]*14

    for i in range(12):

        plt.plot(cos(i*pi/6)*sin(zangle),sin(i*pi/6)*sin(zangle),cos(zangle)*(-1)**i, marker="o", color="crimson")
        #plt.text(cos(i*pi/6)*sin(zangle),sin(i*pi/6)*sin(zangle),cos(zangle)*(-1)**i, dimlabel[i]

    plt.plot(0,0,1, marker="o", color="crimson")
    #plt.text(0,0,1, dimlabel[12])
    plt.plot(0,0,-1, marker="o", color="crimson")
    #plt.text(0,0,1, dimlabel[13])

    for point in points:

        xsum,ysum,zsum,sum=0,0,0,0

        for i in range(12):

            xsum+=cos(i*pi/6)*point[i]*sin(zangle)
            ysum+=sin(i*pi/6)*point[i]*sin(zangle)
            zsum+=cos(zangle)*(-1)**i*point[i]
            sum+=point[i]

        zsum+=point[12]-point[13]
        sum+=point[12]+point[13]

        plt.plot(xsum/sum,ysum/sum,zsum/sum,marker=marker,color=color,markersize=2,alpha=alpha)

        

