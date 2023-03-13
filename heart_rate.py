"""
Name: Keith Crawford 
Date: 1/4/23
"""
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

kcage= int(input("Please enter your age: "))
kcheartratemax= 220 - kcage
kcuppermax= kcheartratemax * .85
kclowermax= kcheartratemax * .65
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {kclowermax} and {kcuppermax} beats per minute!")
