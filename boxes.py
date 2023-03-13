"""
Name: Keith Crawford
Date: 01/09/23
Sources: Class
"""
def get_items(kcstatement):
    kcitems= int(input(kcstatement))
    return kcitems
def get_items_boxes(kcstatement2):
    kcitemsperbox= int(input(kcstatement2))
    return kcitemsperbox
import math
#calling the functions
kcstring="Enter the number of items:"
kcitem=get_items(kcstring)
kcstring2="Enter the number of items per box:"
kcbox=get_items_boxes(kcstring2)

#Finding the number of boxes needed
kcboxes= kcitem/kcbox

kcprint= print(f"For {kcitem} items, packing {kcbox} items in each box, you will need {math.ceil(kcboxes)} boxes.")