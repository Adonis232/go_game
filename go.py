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
            markeredgewidth=1)

# stones on the board
def draw_stones(x, y, color):
    stone = ax.plot(x, y, 'o',
                    markersize=28,
                    markeredgecolor=(0,0,0),
                    markerfacecolor=color,
                    markeredgewidth=1)
    return stone

# event handler to handle click on the board
def on_click(event):
    print(f"x: {event.xdata} y: {event.ydata}")

    global white

    # get the points clicked on the board
    if event.xdata == None or event.ydata == None:
        return
    x = int(round(event.xdata))
    y = int(round(event.ydata))

    # drowing the stone on th eboard 
    # making sure the area clicked is within the board
    if 0 <= x <= 18 and 0 <= y  <=18:
        # if the user clicks to add a new stone on the board
        if event.button == 1 and stones[x, y] == None:
            stones[x, y] = draw_stone(x, y, 'w' if white else 'k')
            stones_values[x, y] = 1 if white else -1
            white = not white      #switch color

        # if user clicks to remove a stone on the board
        elif event.button == 3 and stones[x,y] != None:
            stones[x, y].pop().remove()   #removes the plot
            stones[x ,y] = None
            stones_values[x, y] = 0
        else:
            return
        
        plt.draw()      # update the plot
        print(stones)
        print(stones_values)
    else:
        return

#---main---
fig, ax = draw_board()
draw_grids(ax)

#drawing the 9 stars
draw_star_points(ax, 3,3)
draw_star_points(ax, 3,9)
draw_star_points(ax, 3,15)

draw_star_points(ax, 9,3)
draw_star_points(ax, 9,9)
draw_star_points(ax, 9,15)

draw_star_points(ax, 15,3)
draw_star_points(ax, 15,9)
draw_star_points(ax, 15,15)

# 0 for empty
# 1 for white
#-1 for black

# starting stone
white = True # indicates if the current stone is white, true = whitw, else black

#to store the plot( contining the stone)
stones = np.full((19, 19), None)

# to store the values( color) of each point
stones_values = np.full((19, 19), 0)

"""stone is used to plot the displaying of each stones
and stones_values stores int values for each stone on the board
either a 1. -1 or 0 """

# next the button_oress_event, is an event that fires when the mouse left button is pressed
# xdata y ydata are the position the user has clicked in the event argument

cid = fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()




