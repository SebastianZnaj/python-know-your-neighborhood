from data import Data
from display import Display
from functions import Functions


def main():
    Data.csv_to_list()  # read from csv file
    areas_list = Data.areas_list
    # print(areas_list)
    areas_count = Data.get_area_count() # get touple with areas count
    # print(Display.display_table_1("MAŁOPOLSKIE", areas_count))
    three_names = Functions.three_longest_names(areas_list)  # create a list with 3 longest names
    print(Display.display_table_2("Three longest names", three_names))
if __name__ == '__main__':
    main()
