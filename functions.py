
class Functions:

    @classmethod
    def three_longest_names(cls, object_list):
        long_names = []
        for area in object_list:
            long_names.append(area.nazwa)
        long_names.sort(key=len)
        return reversed(long_names[-3:])  # reversed becouse list need to be from longest to smolest

