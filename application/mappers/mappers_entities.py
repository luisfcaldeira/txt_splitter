from domain.entities.line_parts import LineParts


class MapperDictionaryToLineParts():
    
    @staticmethod
    def map(dictionary : dict) -> LineParts:
        
        line_parts = LineParts()

        for item in dictionary.items():
            line_parts.add_part(item[0], item[1])

        return line_parts
