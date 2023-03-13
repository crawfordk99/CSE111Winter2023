"""
Name: Keith Crawford
Date: 01/11/23
"""
#calling date functions to get day of the week to check for discount
from datetime import datetime
kccurrent_date_and_time= datetime.now()
kcday_of_week=kccurrent_date_and_time.weekday()

#creating functions to calculate subtotal, and display discount, sales tax, and total
def kcget_subtotal(kcstatement):
    kcsubvalue=float(input(kcstatement))
    return kcsubvalue
def kcdisplay_discount_amount(kcdiscvalue):
    print(f"Discount: {kcdiscvalue}")
def kcdisplay_sales_tax(kcsalvalue):
    print(f"Sales Tax: {kcsalvalue: .2f}")
def kcdisplay_total(kctotvalue):
    print(f"Total: {kctotvalue}")

def main():
    #calculations
    kcquestion= "Please enter the subtotal: "
    kcsubtotal= kcget_subtotal(kcquestion)
    kcdiscount_ratio= .1
    kcdiscount= kcsubtotal * kcdiscount_ratio
    kcsalestax_ratio=.06
    kcsalestax= kcsubtotal * kcsalestax_ratio
    kctotal= (kcsubtotal-kcdiscount) + kcsalestax

    if (kcday_of_week== 2 or  kcday_of_week== 3) and (kcsubtotal > 50):
        kcdisplay_discount_amount(kcdiscount)
        kcdisplay_sales_tax(kcsalestax)
        kcdisplay_total(kctotal)
    else:
        kcdisplay_sales_tax(kcsalestax)
        kcdisplay_total(kctotal)
main()