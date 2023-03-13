"""
Name: Keith Crawford
Date: 01/11/23
Sources: Class/prove assignment module
"""
import math
def kcget_width(kcstatement1):
    kcwidvalue= int(input(kcstatement1))
    return kcwidvalue
def kcget_aspect(kcstatement2):
    kcaspvalue= int(input(kcstatement2))
    return kcaspvalue
def kcget_diameter(kcstatement3):
    kcdiavalue= int(input(kcstatement3))
    return kcdiavalue
kc_wid_statement= "Enter the width of the tire in mm: "
kc_asp_statement= "Enter the aspect ratio of the tire: "
kc_dia_statement= "Enter the diameter of the wheel in inches: "

#calling functions
kcwidth= kcget_width(kc_wid_statement)
kcaspect= kcget_aspect(kc_asp_statement)
kcdiameter=kcget_diameter(kc_dia_statement)

kcbigdividenum= 10000000000
kcvolume= float(math.pi * kcwidth**2 * kcaspect * (kcwidth * kcaspect + 2540 * kcdiameter))/(kcbigdividenum)
print(f"The approximate volume is {kcvolume: .2f} in liters")

#addition for prove assignment week 2, adding date and time
from datetime import datetime
kcdatetime= datetime.now()

#opening and appending the file
with open("volume.txt", mode="at") as volume_file:
    print(f"{kcdatetime: %Y-%m-%d}, {kcwidth}, {kcaspect}, {kcdiameter}, {kcvolume: .2f}", file=volume_file)

#exceed expectations
kcresponse= input(f"Do you wish to buy tires with the same dimensions that you entered? Please enter Y/N: ")
if (kcresponse == "Y") or (kcresponse== "y"):
    kcphonenumber= input(f"Please enter your phone number: ")
    with open("volume.txt", mode= "at") as volume_file:
        print(f"{kcphonenumber}", file=volume_file)




