"""
 /---------------------------------\
|       MAŁOPOLSKIE               |
|-----+---------------------------|
|   1 | wojewódźtwo               |
|-----+---------------------------|
|  22 | powiaty                   |
|-----+---------------------------|
|  14 | gmina miejska             |
|-----+---------------------------|
| 122 | gmina wiejska             |
|-----+---------------------------|
|  46 | gmina miejsko-wiejska     |
|-----+---------------------------|
|  46 | obszar wiejski            |
|-----+---------------------------|
|  46 | miasto                    |
|-----+---------------------------|
|   3 | miasto na prawach powiatu |
|-----+---------------------------|
|   4 | delegatura                |
\---------------------------------/
"""
class Display:
    main1_headers = [35, 3, 32]
    main1_elements = ["województwo", "powiaty", "gmina miejska", "gmina wiejska", "gmina miejsko-wiejska", "obszar wiejski", "miasto", "miasto na prawach powiatu", "delagatura"]
    main2_headers = [30, 5, 25]
    main3_headers = [52, 5, 25, 27]


    @staticmethod
    def fill_with_spaces(element, lenght):
        """ Fills table cell with spaces to desired length"""
        element = "|" + element
        while len(element) < lenght:
            element += " "
        return element + "|"

    @classmethod
    def display_table_1(cls, title, values):  # argument values is a tuple
        """Print table with title, values, headers and elements """
        # top/bottom
        top_and_bottom = "%s" % chr(0x26e8) + Display.main1_headers[0] * "-" + "%s\n" % chr(0x26e8)

        # title
        table_name = cls.fill_with_spaces(title, Display.main1_headers[0]+2) + "\n"

        # middle
        middle = ""
        separator = "|" + Display.main1_headers[1] * "-" + "++" + (Display.main1_headers[2]-1) * "-" + "|\n"
        for i, area_name in enumerate(cls.main1_elements):
                row = cls.fill_with_spaces(str(values[i]), 4) + cls.fill_with_spaces(area_name, Display.main1_headers[2]) + "\n"
                middle += separator + row
        return top_and_bottom + table_name + middle + top_and_bottom

    @classmethod
    def display_table_2(cls, title, long_names):  # argument values is a tuple
        """Print table with title and list of long names """
        # top/bottom
        top_and_bottom = "%s" % chr(0x26e8) + Display.main2_headers[0] * "-" + "%s\n" % chr(0x26e8)

        # title
        table_name = cls.fill_with_spaces(title, Display.main2_headers[0]+2) + "\n"

        # middle
        middle = ""
        separator = "|" + Display.main2_headers[1] * "-" + "++" + (Display.main2_headers[2]-1) * "-" + "|\n"
        for i, name in enumerate(long_names):
                row = cls.fill_with_spaces(str(i+1) + ".", 6) + cls.fill_with_spaces(name, Display.main2_headers[2]) + "\n"
                middle += separator + row
        return top_and_bottom + table_name + middle + top_and_bottom

    @classmethod
    def display_table_3(cls, title, object_list):  # argument is a list of objects
        """Print table with title as a list of str and object list as an argument"""
        # top/bottom
        top_and_bottom = "%s" % chr(0x26e8) + (Display.main2_headers[0] + Display.main2_headers[2] +2 ) * "-" + "%s\n" % chr(0x26e8)

        # title
        table_name = "|Lp. |" + cls.fill_with_spaces(title[0], Display.main3_headers[2]) + cls.fill_with_spaces(title[1], Display.main3_headers[3]) + "\n"

        # middle
        middle = ""
        separator = "|" + (Display.main3_headers[1]-1) * "-" + "++" + (Display.main3_headers[2]-1) * "-" + "++" + + (Display.main3_headers[3]-1) * "-" + "|\n"
        for i, obj in enumerate(object_list):
                row = cls.fill_with_spaces(str(i + 1) + ".", Display.main3_headers[1]) + cls.fill_with_spaces(obj.nazwa, Display.main3_headers[2]) +cls.fill_with_spaces(obj.typ, Display.main3_headers[3]) + "\n"
                middle += separator + row
        return top_and_bottom + table_name + middle + top_and_bottom
