
class LineParts():

    def __init__(self) -> None:
        self.__parts = list()

    def add_part(self, field_name: str, pos_last_char : int) -> None:
        self.__parts.append(Part(field_name, pos_last_char))
        self.sort_me()

    def sort_me(self) -> None:
        self.__parts = sorted(self.__parts, key=lambda x: x.pos_last_char, reverse=False)

    def get_all_positions(self) -> tuple:
        result = list()
        for part in self.__parts:
            result.append(part.pos_last_char)

        return tuple(result)

    def get_all_field_names(self) -> tuple:
        result = list()

        for part in self.__parts:
            result.append(part.field_name)

        if len(self.__parts) == 0:
            result.append(DefaultField())

        return tuple(result)

    def __len__(self) -> int:
        return len(self.__parts)

class Part():

    def __init__(self, field_name: str, pos_last_char) -> None:
        self.__field_name = field_name
        self.__pos_last_char = pos_last_char

    @property
    def field_name(self):
        return self.__field_name

    @property
    def pos_last_char(self):
        return self.__pos_last_char

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Part) and __o.field_name == self.field_name and __o.pos_last_char == self.pos_last_char

class DefaultField(Part):

    def __init__(self) -> None:
        super().__init__('default_field', 0)

