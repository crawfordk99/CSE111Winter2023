"""
Name: Keith Crawford
Date: 01/18/23
"""
# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    kcgender= input(f"Please enter your gender (M or F): ")
    kcbirthdate= input(f"Enter your birthdate (YYYY-MM-DD): ")
    kcweight= int(input(f"Enter your weight in U.S. pounds: "))
    kcheight= int(input(f"Enter your height in U.S. inches: "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    kcage= compute_age(kcbirthdate)
    kcweight_in_kg= kg_from_lb(kcweight)
    kcheight_in_cm= cm_from_in(kcheight)
    kcheight_in_meters= meters_from_cm(kcheight_in_cm)
    kcbodymassindex= body_mass_index(kcweight_in_kg, kcheight_in_cm)
    kcbasalrate= basal_metabolic_rate(kcgender, kcweight_in_kg, kcheight_in_cm, kcage)
    # Print the results for the user to see.
    print(f"Age (years): {kcage}")
    print(f"Weight (kg): {kcweight_in_kg: .2f}")
    print(f"Height (m): {kcheight_in_meters: .1f}")
    print(f"Body Mass Index: {kcbodymassindex: .1f}")
    print(f"Basal Metabolic Rate (kcal/day): {kcbasalrate: .0f}")
    # Extra printing what your BMI range is, for creativity
    if (kcbodymassindex<18.5):
        print (f"Your BMI level is: underweight")
    elif (kcbodymassindex>=18.5) and (kcbodymassindex<25):
        print (f"Your BMI level is: healthy")
    elif (kcbodymassindex>=25) and (kcbodymassindex<30):
        print(f"Your BMI level is: overweight")
    elif (kcbodymassindex>=30):
        print(f"Your BMI level is: obese")
    pass


def compute_age(kcbirth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    kcbirthdate = datetime.strptime(kcbirth_str, "%Y-%m-%d")
    kctoday = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    kcyears = kctoday.year - kcbirthdate.year

    # If necessary, subtract one from the difference.
    if kcbirthdate.month > kctoday.month or \
        (kcbirthdate.month == kctoday.month and \
            kcbirthdate.day > kctoday.day):
        kcyears -= 1

    return kcyears


def kg_from_lb(kcpounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kclbs_mass_ratio=float(0.45359237)
    kckgs= kcpounds * kclbs_mass_ratio
    return kckgs


def cm_from_in(kcinches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    kcin_cm_ratio= float(2.54)
    kccentimeters= kcinches * kcin_cm_ratio
    return kccentimeters
#Extra function for creativity
def meters_from_cm(kccms):
    """
    Convert a length in centimeters to meters
    """
    kcmeters_str= kccms/100
    return kcmeters_str


def body_mass_index(kcweight_str, kcheight_str):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    kcbignum=10000
    kcbmi= (kcbignum * kcweight_str)/(kcheight_str * kcheight_str)
    return kcbmi


def basal_metabolic_rate(kcgender_str, kcweight_str, kcheight_str, kcage_str):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if (kcgender_str== "M"):
        kcbmr= (88.362) + (13.397 * kcweight_str) + (4.799 * kcheight_str) - (5.677 * kcage_str)
    elif (kcgender_str== "F"):
        kcbmr= (447.593) + (9.247 * kcweight_str) + (3.098 * kcheight_str) - (4.330 * kcage_str)
    return kcbmr
    


# Call the main function so that
# this program will start executing.
main()