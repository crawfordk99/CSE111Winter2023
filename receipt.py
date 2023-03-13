"""
Name:Keith Crawford
Date:03/04/23
"""
import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
kccurrent_day= current_date_and_time.weekday()


   
key_column_index=0
product_column_index=1
price_column_index=2

def read_dictionary(kcfilename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
   

    #Creating a dictionary to put the file into
    kcdict= {}

    #opening the file to be read and put into the dictionary
    try:
        with open(kcfilename, "rt") as kccsv_file:
            kcreader=csv.reader(kccsv_file)
            next(kcreader)
            for kcrow_list in kcreader:
                if len(kcrow_list) !=0:
                    kckey= kcrow_list[key_column_index]
                    kcdict[kckey]= kcrow_list
    except (FileNotFoundError):
        print(f"File not found. Please enter an existing file name.")
    except(PermissionError):
        print(f"Permission denied. User does not have permission to access {kcfilename}.")
    except(KeyError):
        print(f"Key not found in dictionary. Please check the dictionary and enter a key in the dictionary.")
    
    return kcdict   
   
def determining_discount(kcday, kctotal_price):
    #Determining if the day is Tuesday or Wednesday to determine if there is a discount for the customer.
    kcdiscount=0
    #use to debug
    kcday=2
    if (kcday==2) or (kcday==3):
        kcdiscount=.10
        kctotal_discount= kctotal_price * kcdiscount
        kctotal_price= kctotal_price-kctotal_discount
        print(f"Discount: {kctotal_discount: .2f}")
    else:
        kcdiscount=0
    return kctotal_price

def main():
    
    #calling for the dictionary
    kcproducts_dictionary= read_dictionary("products.csv", key_column_index)
    print(f"Inkom Emporium")
    print()
     #request.csv index variables
    kcitem_number_index= 0
    kcquantity_index= 1
    #product variables
    kcproduct=""
    kcprice=0
    kcordered_items_total=0
    kcsubtotal=0
    kcsales_tax=.06
    kcsales_tax_total=0
    kctotal=0
    #opening the request.csv file
    try:
        with open ("request.csv", "rt") as kcrequest_file:
            kcreader=csv.reader(kcrequest_file)
            next(kcreader)
            #iterating through the file, turning it into a list
            for kcrow_list in kcreader:
                if len(kcrow_list) !=0:
                    kckey= kcrow_list[kcitem_number_index]
                    kcquantity=kcrow_list[kcquantity_index]
                    kcordered_items_total += int(kcquantity)
                    #looking for the item number in the dictionary to get the product name and price
                    if kckey in kcproducts_dictionary:
                        kcitems= kcproducts_dictionary[kckey]
                        kcproduct= kcitems[product_column_index]
                        kcprice= kcitems[price_column_index]
                        kcsubtotal += float(kcprice) * int(kcquantity)
                        kcsales_tax_total= float(kcsubtotal) * float(kcsales_tax)
                        kctotal= (float(kcsubtotal) + float(kcsales_tax_total))
                        print(f"{kcproduct}: {kcquantity} @ {kcprice}")    
    except (FileNotFoundError):
        print(f"File not found. Please enter an existing file name.")
    except(PermissionError):
        print(f"Permission denied. User does not have permission to access {kcfilename}.")
    except(KeyError):
        print(f"Key not found in dictionary. Please check the dictionary and enter a key in the dictionary.")
    #calling to see if there is a discount or not
        
    print()
    print(f"Number of ordered items: {kcordered_items_total}")
    print(f"Subtotal: {kcsubtotal: .2f}")
    print(f"Sales Tax: {kcsales_tax_total: .2f}")
    kctotal= determining_discount(kccurrent_day, kctotal)
    print(f"Total: {kctotal: .2f}")
    print()
    print(f"Thank you for shopping at the Inkom Emporium!")
    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")

if __name__=="__main__":
    main()