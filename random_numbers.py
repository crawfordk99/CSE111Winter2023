"""
Name: Keith Crawford
Date: 02/15/23
"""
import random
#main function

def main():
    #Sets up and prints out list each time the append_random_numbers list is called
    #No parameters
    kcnumbers= [16.2, 75.1, 52.3]
   
    print(f"{kcnumbers}")
    append_random_numbers(kcnumbers)
    print(f"{kcnumbers}")
    append_random_numbers(kcnumbers, 3)
    print(f"{kcnumbers}")
    
def append_random_numbers(kclist, kcnum= 1):
    #Create random numbers to add to list
    for i in range(kcnum):
        kcrandom= random.uniform(0, 100)
        kcround_random= round(kcrandom, 1)
        kclist.append(kcround_random)

if __name__ == "__main__":
    main()