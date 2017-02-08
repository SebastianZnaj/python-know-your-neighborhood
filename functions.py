from collections import Counter


class Functions:

    @classmethod
    def three_longest_names(cls, object_list):
        """Return list with 3 longest names"""
        long_names = []
        for area in object_list:
            long_names.append(area.nazwa)
        long_names.sort(key=len)
        return reversed(long_names[-3:])  # reversed list from longest to least element

    @classmethod
    def county_with_largest_communities(cls, object_list):
        """Search for name county with largest number of communities"""
        pow_values = []
        for area in object_list:
            pow_values.append(area.pow)
        max_value = dict(Counter(pow_values))  # dict with counted area.pow values
        max_key = max(max_value, key=lambda i: max_value[i])  # finding key with largest value in dictionary
        for area in object_list:
            if area.pow == max_key and area.typ == "powiat":
                return [area.nazwa]

    @classmethod
    def location_belonging(cls, object_list):
        """Find location that belong to more than one community"""
        list_of_names = []
        for area in object_list:
            list_of_names.append(area.nazwa)
        counter = dict(Counter(list_of_names))
        filtered = []
        for name in counter:
            if counter[name] > 1:
                filtered.append(name)
        filtered_objects = []
        for obj in object_list:
            if obj.nazwa in filtered:
                filtered_objects.append(obj)
        return filtered_objects




