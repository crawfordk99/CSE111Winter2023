"""
Name: Keith Crawford
Date: 03/01/23
"""
# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
A common task for many knowledge workers is to use a number, key,
or ID to look up information about a person. For example, a
knowledge worker may use a phone number or e-mail address as a key
to find (or look up) additional information about a customer.
During this activity, your team will write a Python program that
uses a student's I-Number to look up the student's name."""
import csv

def read_dictionary(filename, key_column_index):
    """ Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #create dictionary to put the file into 
    kcdict= {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named kccsv_file.
    with open (filename) as kccsv_file:
        kcreader= csv.reader(kccsv_file)
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(kcreader)
        #Read the rows in the CSV file one row at a time.
        #The reader object returns each row as a list.
        for kcrow_list in kcreader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(kcrow_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = kcrow_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                kcdict[key] = kcrow_list

    # Return the dictionary.
    return kcdict

def main():
    # The column headings and indexes.
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    # Read the contents of a CSV file named students.csv
    # into a dictionary named students_dict. Use the I-Number
    # as the key in the dictionary.
    kcstudents_dict = read_dictionary("students.csv", I_NUMBER_INDEX)

    # Get an I-Number from the user.
    kcinumber = input("Please enter an I-Number (xx-xxx-xxxx): ")

    # The I-Numbers are stored in the CSV file as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    kcinumber = kcinumber.replace("-", "")

    # Determine if the user input is formatted correctly.
    if not kcinumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(kcinumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(kcinumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if kcinumber not in kcstudents_dict:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = kcstudents_dict[kcinumber]
                name = value[NAME_INDEX]

                # Print the student name.
                print(name)



if __name__ == "__main__":
    main()
