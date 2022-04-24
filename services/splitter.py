class Splitter():

    def split_by_pos(self, string_to_split, *positions):
        return_value = list()
        previous = 0
        for position in positions:
            return_value.append(string_to_split[previous:position].strip())
            previous = position
        return tuple(return_value)