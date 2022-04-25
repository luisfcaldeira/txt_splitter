import os
from typing import Any
from domain.entities.line_parts import LineParts
from services.splitter import Splitter
from domain.conversors.line_part_conversors import ConversorDictToLineParts
from services.string_service import StringService

class FileConversor():
     
    @property
    def line_parts(self) -> LineParts:
        return self.__line_parts

    def __init__(self, fields : dict) -> None:
        self.__set_file_configuration(fields)
        
    def __set_file_configuration(self, fields : dict) -> None:
        conversor = ConversorDictToLineParts()
        self.__line_parts = conversor.map(fields)

    def __set_header(self, keys, sep) -> None:
        self.__header = StringService.join_it_in_a_line(keys, sep)

    def add_field(self, field_name : str, position_of_last_char : int) -> None:
        self.__line_parts.add_part(field_name, position_of_last_char)

    def to_csv(self, file_src : str, file_destination : str, sep = ';', open_mode='w') -> None:
        print('convertin file:', file_src, 'into file', file_destination, '...', end=' ')
        self.__set_header(self.__line_parts.get_all_field_names(), sep)
        splitter = Splitter()
        
        with open(file_src, "r", encoding="utf-8") as fp:
            lines = fp.readlines()

        with open(file_destination, open_mode, encoding='utf-8') as fp:
            
            fp.writelines(self.__header)
            
            size_source = os.path.getsize(file_src) 

            for line in lines:
                size = os.path.getsize(file_destination) 

                print(round(min(size/size_source * 100, 100), 2), '%',end='\r ')
                splitted = splitter.split_by_pos(line, *self.__line_parts.get_all_positions())
                data_line = StringService.join_it_in_a_line(splitted, sep)

                fp.writelines(data_line)

