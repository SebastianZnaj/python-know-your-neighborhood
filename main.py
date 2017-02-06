from data import Data
from area import Area
from display import Display


def main():
    Data.csv_to_list()
    # print(Data.areas_list)
    areas_count = Data.get_area_count()
    print(areas_count)
    print(areas_count[0])
    print(Display.display_table_1("MAŁOPOLSKIE", areas_count))
if __name__ == '__main__':
    main()
