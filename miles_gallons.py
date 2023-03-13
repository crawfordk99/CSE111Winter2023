"""
Name: Keith Crawford
Date: 01/17/23
"""
def main():
    # Get an odometer value in U.S. miles from the user.

    # Get another odometer value in U.S. miles from the user.

    # Get a fuel amount in U.S. gallons from the user.

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.

    # Display the results for the user to see.
    kcsta_miles= int(input(f"Enter the first odometer reading (miles): "))
    kcfinal_miles= int(input(f"Enter the second odometer reading (miles): "))
    kcgallons= float(input(f"Enter the amount of fuel used (gallons): "))
    
    kcm_p_g=miles_per_gallon(kcsta_miles, kcfinal_miles, kcgallons)
    kcliters_per_km= lp100k_from_mpg(kcm_p_g)

    print(f"{kcm_p_g: .1f} miles per gallon")
    print(f"{kcliters_per_km: .2f} liters per 100 kilometers")
    pass



def miles_per_gallon(kcstart_miles, kcend_miles, kcamount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    kcfuel_effiency=(kcend_miles - kcstart_miles)/(kcamount_gallons)
    return kcfuel_effiency


def lp100k_from_mpg(kcmpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    kcnumber=float(235.125)
    kclpkg= kcnumber/kcmpg
    return kclpkg


# Call the main function so that
# this program will start executing.
main()