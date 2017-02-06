import csv
from area import Area


class Data:
    areas_list = []  # list of objects

    @classmethod
    def csv_to_list(cls):
        with open("malopolska.csv", "r") as f:
            reader = csv.reader(f)
            for line in reader:
                Data.areas_list.append(Area(line[0], line[1], line[2], line[3], line[4], line[5]))

    @classmethod
    def get_area_count(cls):
        wojewodztwo_count = 0
        powiat_count = 0
        gmina_miejska_count = 0
        gmina_wiejska_count = 0
        gmina_miejsko_wiejska_count = 0
        obszar_wiejski_count = 0
        miasto_count = 0
        miasto_na_prawach_count = 0

        for area in cls.areas_list:
            if area.typ == "województwo":
                wojewodztwo_count += 1
            elif area.typ == "powiat":
                powiat_count += 1
            elif area.typ == "gmina miejska":
                gmina_miejska_count += 1
            elif area.typ == "gmina wiejska":
                gmina_wiejska_count += 1
            elif area.typ == "gmina miejsko-wiejska":
                gmina_miejsko_wiejska_count += 1
            elif area.typ == "obszar wiejski":
                obszar_wiejski_count += 1
            elif area.typ == "miasto":
                miasto_count += 1
            elif area.typ == "miasto na prawach powiatu":
                miasto_na_prawach_count += 1
        return powiat_count, gmina_miejska_count, gmina_wiejska_count, gmina_miejsko_wiejska_count, obszar_wiejski_count, miasto_count, miasto_na_prawach_count
