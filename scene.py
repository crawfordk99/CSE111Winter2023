"""
Name: Keith Crawford
Date: 01/18/23
"""
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    kcscene_width = 800
    kcscene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    kccanvas = start_drawing("Scene", kcscene_width, kcscene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_sky(kccanvas, 0, 0, kcscene_width, kcscene_height)
    draw_ground(kccanvas, kcscene_width, kcscene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(kccanvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sun(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2):
    """
    Drawing the sun
    Paramaters:
    kccanvas= The canvas for drawing
    kcwidth1 & 2= the width for the sun
    kcheight 1 & 2= the height for the sun
    """
   
    draw_oval(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2, width=1, fill= "yellow") #sun
def draw_clouds(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2):
    """
    Drawing the clouds
    Parameters:
    kccanvas= the canvas for drawing
    kcwidth1 and 2= the width of the cloud
    kcheight1 and 2= the height of the cloud
    """
    draw_oval(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2, outline="", fill="white")
    

def draw_sky(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2):
    """
    Drawing the sky
    Parameters:
    kccanvas= The canvas for drawing
    kcwidth1 * 2= the width of the sky
    kcheight1 * 2= the height of the sky
    """
    draw_rectangle(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2, width=1, fill="skyBlue") #sky
    #calling other functions
    draw_sun(kccanvas, 450, 400, 550, 500)
    draw_clouds(kccanvas, 275, 300, 400, 415)
    draw_clouds(kccanvas, 250, 300, 450, 400)
    draw_clouds(kccanvas, 500, 350, 650, 450)
    draw_clouds(kccanvas, 450, 350, 700, 425)
    draw_clouds(kccanvas, 225, 275, 425, 375)
    draw_clouds(kccanvas, 450, 300, 675, 375)

def draw_ground(kccanvas, kcwidth, kcheight):
    """
    Drawing the ground
    Parameters:
    kccanvas= the canvas for drawing
    kcwidth= the width of the canvas
    kcheight1 and 2= the height of the initial grass
    kcintv= the interval for the for loop
    """ 
    #calling functions
    draw_grass(kccanvas, kcwidth, 0, 50, 1, "green", 1)
    draw_grass(kccanvas, kcwidth, 150, 200, 1, "green", 1)
    draw_street(kccanvas, kcwidth, 50, 150, 1, "gray30")
    draw_markers(kccanvas, kcwidth, 100, 110, 10, 20, "yellow")
    draw_building(kccanvas, 10, 200, 50, 300, "gray", "steelblue")
    draw_building(kccanvas, 30, 300, 40, 325, "", "white")
    draw_building(kccanvas, 60, 200, 110, 400, "black", "navyblue")
    draw_building(kccanvas, 150, 200, 450, 250, "gray85", "gray25")
    draw_building(kccanvas, 150, 225, 450, 230, "", "steelblue")
    draw_train_head(kccanvas, 450, 250, 450, 200, 500, "orange", "steelblue")

def draw_train_head(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2, kcwidth3, kcoutline, kcfill):
    """
    Drawing the train's head
    """    
    draw_polygon(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2, kcwidth3, kcheight2, outline=kcoutline, fill=kcfill)
def draw_grass(kccanvas, kcwidth, kcheight1, kcheight2, kcthickness, kcfill, kcintv):
    """
    Drawing the ground
    Parameters:
    kccanvas= the canvas for drawing
    kcwidth= the width of the canvas
    kcheight1 and 2= the height of the initial grass
    kcthickness= The thickness of the lines
    kcfill=The color of the lines
    kcintv= the interval for the for loop
    """
    for x in range(1, kcwidth, kcintv): #grass
        draw_line(kccanvas, x, kcheight1, x, kcheight2, width=kcthickness, fill= kcfill)


def draw_street(kccanvas, kcwidth, kcheight1, kcheight2, kcintv, kcfill):
    """
    Drawing the street
    Parameters:
    kccanvas= The canvas for drawing
    kcheight1 and 2= the height of the street
    kcwidth=the width of the street 
    kcintv= the interval between lines drawn for for loops
    """
    
    for x in range(1, kcwidth, kcintv):
        draw_line(kccanvas, x, kcheight1, x, kcheight2, width=1, fill= kcfill)
    
    

def draw_markers(kccanvas, kcwidth, kcheight1, kcheight2, kcthickness, kcintv, kcfill):
    """
    Drawing the yellow street markers
    Parameters:
    kccanvas= The canvas for drawing
    kcwidth= The length of the markers
    kcheight1 and 2= The height of the markers
    kcthickness= The thickness of each individual marker
    kcintv= The space between single markers
    kcfill= The color of the markers
    """
    for x in range(1, kcwidth, kcintv):#yellow markers
        draw_line(kccanvas, x, kcheight1, x, kcheight2, width=kcthickness, fill= kcfill)
    

def draw_building(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2, kcoutline, kcfill):
    """
    Drawing buildings
    Parameters:
    kccanvas= The canvas for drawing
    kcwidth1 and 2= the width of the building
    kcheight1 and 2= the height of the building
    """
    draw_rectangle(kccanvas, kcwidth1, kcheight1, kcwidth2, kcheight2, outline= kcoutline, fill= kcfill)

# Call the main function so that
# this program will start executing.
main()