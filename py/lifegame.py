import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

begin = np.array([[1,1,0,1],[0,1,1,0],[0,1,0,1],[1,1,0,0]])
N=100
grid = np.zeros((N,N))

def addbegin(i,j,x):
    x[i:i+4,j:j+4]=begin
    return x
grid=addbegin(48,48,grid)

def update(frame,img,grid):
    newgrid=grid.copy()
    for i in range(N):
        for j in range(N):
            total=int(grid[i,(j-1)%N]+
            grid[i,(j+1)%N]+
            grid[(i+1)%N,(j+1)%N]+
            grid[(i+1)%N,(j-1)%N]+
            grid[(i+1)%N,j]+
            grid[(i-1)%N,(j+1)%N]+
            grid[(i-1)%N,(j-1)%N]+
            grid[(i-1)%N,j])
            if grid[i,j]==1:
                if total<2 or total>3:
                    newgrid[i,j]=0
            elif total==3:
                newgrid[i,j]=1
    img.set_data(newgrid)
    grid[:]=newgrid[:]
    return img

fig,ax=plt.subplots()
img=ax.imshow(grid)
ani=animation.FuncAnimation(fig,update,fargs=(img,grid),frames=10,interval=50)
plt.show()