import matplotlib.pyplot as plt
import numpy as np

def draw_board():
    #create a figure to draw the board of 9x9 in size
    fig = plt.figure(figsize=[9,9])

    #set background color
    fig.patch.set_facecolor((0.85, 0.64, 0.125)) #patch is the obeject we set the color to

    # turn off axes
    ax = fig.add_subplot(111)


    ax.set_axis_off()

    return fig, ax

# drawing the grids 
def draw_grids(ax):
    #vertical lines
    for x in range(19):
        ax.plot([x ,x], [0,18], 'k')
    
    #horizontal lines
    for y in range(19):
        ax.plot([0, 18], [y,y], 'k')

    # new we center the gird on position
    ax.set_position([0,0.2,1,1])
    #prints positions  of the grid
    print(ax.get_position().bounds)


def draw_star_points(ax, x, y):
    # method to draw the stars on the grid
    ax.plot(x, y, 'o', markersize=8,
            markeredgecolor=(0,0,0),
            markerfacecolor='k',
            makeredgewidth=1)



    

fig, ax = draw_board()
draw_grids(ax)

#drawing the 9 stars
draw_star_points
plt.show()


