"""
Name: Keith Crawford
Date: 01/25/23
"""
import math
#Creating lists
kc_cans=[
["#1 Picnic",	6.83, 	10.16,	0.28],
["#1 Tall",	7.78,	11.91,	0.43],
["#2",	8.73,	11.59,	0.45],
["#2.5",	10.32,	11.91,	0.61],
["#3 Cylinder",	10.79,	17.78,	0.86],
["#5",	13.02,	14.29,	0.83],
["#6Z",	5.40,	8.89,	0.22],
["#8Z short",	6.83,	7.62,	0.26],
["#10",	15.72,	17.78,	1.53],
["#211",	6.83,	12.38,	0.34],
["#300",	7.62,	11.27,	0.38],
["#303",	8.10,	11.11,	0.42]
]

def main():
    #creating for loop to sort through the different can sizes
    for can in kc_cans:
        kc_name=can[0]
        kc_radius=can[1]
        kc_height=can[2]
        kc_volume=compute_volume(kc_radius, kc_height)
        kc_surface_area=compute_surface_area(kc_radius, kc_height)
        kc_storage_efficiency= kc_volume/kc_surface_area
        print(f"{kc_name} {kc_storage_efficiency:.2f}")
    

def compute_volume(kcradius, kcheight):
    kcvolumevalue= math.pi*(kcradius*kcradius)*kcheight
    return kcvolumevalue

def compute_surface_area(kcradius, kcheight):
    kcsurfaceareavalue= (2 * math.pi) * (kcradius) * (kcradius+kcheight)
    return kcsurfaceareavalue
main()

    
