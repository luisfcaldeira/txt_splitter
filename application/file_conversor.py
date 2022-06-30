import os
from typing import Any
from domain.entities.line_parts import LineParts
from services.splitter import Splitter
from domain.conversors.line_part_conversors import ConversorDictToLineParts
from services.string_service import StringService

class FileConversor():

    def __init__(self, fields : dict) -> None:
        self.__set_file_configuration(fields)
        self.__encoding = 'utf-8'
     
    @property
    def line_parts(self) -> LineParts:
        return self.__line_parts

    def set_encoding(self, encoding: str):
        if isinstance(encoding, str):
            self.__encoding = encoding
        
    def __set_file_configuration(self, fields : dict) -> None:
        conversor = ConversorDictToLineParts()
        self.__line_parts = conversor.map(fields)

    def __set_header(self, keys, sep) -> None:
        self.__header = StringService.join_it_in_a_line(keys, sep)

    def add_field(self, field_name : str, position_of_last_char : int) -> None:
        self.__line_parts.add_part(field_name, position_of_last_char)

    def to_csv(self, file_src : str, file_destination : str, sep = ';', open_mode='w', ignore_header=False) -> None:
        print('converting file:', file_src, 'into file', file_destination, '...', end='\n\r')
        self.__set_header(self.__line_parts.get_all_field_names(), sep)
        splitter = Splitter()
        
        with open(file_src, "r", encoding=self.__encoding) as fp:
            lines = fp.readlines()

        size = 0
        with open(file_destination, open_mode, encoding=self.__encoding) as fp:
            if ignore_header == False:
                fp.writelines(self.__header)
            
            size_source = os.path.getsize(file_src) 

            for line in lines:

                splitted = splitter.split_by_pos(line, *self.__line_parts.get_all_positions())
                data_line = StringService.join_it_in_a_line(splitted, sep)

                size = size + len(line.encode(self.__encoding))
                print(str(round(size/size_source * 100, 2)).rjust(5, ' '), '%' ,end='\r')

                fp.writelines(data_line)

        print('it is done!', end='\r\n')

