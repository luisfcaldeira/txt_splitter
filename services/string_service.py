

from abc import abstractmethod


class StringService():

    @abstractmethod
    def join_it_in_a_line(array_data : list, sep: str) -> str:
        data_line = sep.join(array_data)
        return f'{data_line}\n'