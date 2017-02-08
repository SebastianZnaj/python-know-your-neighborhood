from data import Data
from display import Display
from functions import Functions
import os
import time
INTRO = ("""
What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program
""")


def main():
    Data.csv_to_list()  # Read from csv file
    areas_list = Data.areas_list

    while True:
        # os.system("clear")  #I don't know why this method causes some silly errors
        print(INTRO)
        option = input("Choose option: ")
        if option == "1":  # Get tuple with areas count
            areas_count = Data.get_area_count()
            print(Display.display_table_1("MAŁOPOLSKIE", areas_count))
            time.sleep(3)

        elif option == "2":  # Create a list with 3 longest names
            three_names = Functions.three_longest_names(areas_list)
            print(Display.display_table_2("Three longest names", three_names))
            time.sleep(3)

        elif option == "3":  # Find county with largest communities
            largest_county = Functions.county_with_largest_communities(areas_list)
            print(Display.display_table_2("County with largest communities", largest_county))
            time.sleep(3)

        elif option == "4":  # Find locations that appears more than once
            multiple_locations = Functions.location_belonging(areas_list)
            print(Display.display_table_3(["Location", "Type"], multiple_locations))
            time.sleep(4)
        elif option == "5":  # Search for inputted phrase in location names
            name = input("Searching for: ")
            result = Functions.advance_search(areas_list, name)
            if len(result) <= 0:
                print("\nNo such name in database!\nPlease don't use digit and special signs.\n")
                time.sleep(2)
            else:
                print("\nFound {} location(s):\n".format(len(result)))
                print(Display.display_table_3(["Location", "Type"], result))
                time.sleep(3)

        elif option == "0":
            exit()

        else:
            print("\nNo such option in menu !\nTry again.\n")
            time.sleep(1)

if __name__ == '__main__':
    main()
