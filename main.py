from data import Data
from display import Display
from functions import Functions
import os
import time
INTRO =("""
What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program
""")

def main():
    Data.csv_to_list()  # read from csv file
    areas_list = Data.areas_list
    # 1
    areas_count = Data.get_area_count() # get touple with areas count
    # 2
    three_names = Functions.three_longest_names(areas_list)  # create a list with 3 longest names
    # 3
    largest_county = Functions.county_with_largest_communities(areas_list)
    # 4
    multiple_locations = Functions.location_belonging(areas_list)
    while True:
        # os.system("clear")
        print(INTRO)
        option = input("Choose option: ")
        if option == "1":
            print(Display.display_table_1("MAŁOPOLSKIE", areas_count))
            time.sleep(3)

        elif option == "2":
            print(Display.display_table_2("Three longest names", three_names))
            time.sleep(3)

        elif option == "3":
            print(Display.display_table_2("County with largest communities", largest_county))
            time.sleep(3)

        elif option == "4":
            print(Display.display_table_3(["Location", "Type"], multiple_locations))
            time.sleep(4)

        elif option == "5":
            pass

        elif option == "0":
            exit()

if __name__ == '__main__':
    main()
