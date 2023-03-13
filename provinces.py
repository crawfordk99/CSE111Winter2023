"""
Name: Keith Crawford  
Date: 02/27/23
"""

def make_list(filename):
    #creating empty list to import text file into
    kctext_list= []
    #opening file
    with open (filename, "rt") as text_file:
        for kcline in text_file:
            kcclean_line=kcline.strip()
            kctext_list.append(kcclean_line)
    print(f"{kctext_list}")
    kctext_list.pop(0)
    kctext_list.pop()
    return kctext_list
    
def main():
    #Calling functions here
    kcprovinces_list= make_list("provinces.txt")
    kcalberta=0
    #Sorting through list to replace AB with Alberta, and count number of occurences
    for i in range(len(kcprovinces_list)):
        if (kcprovinces_list[i]== "AB"):
            kcprovinces_list[i]="Alberta"       
    kcalberta = kcprovinces_list.count("Alberta")
    print(f"Alberta occurs {kcalberta} times in the modified list")

# Call main to start this program.
if __name__ == "__main__":
    main()