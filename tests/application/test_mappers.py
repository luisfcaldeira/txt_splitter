from domain.conversors.line_part_conversors import ConversorDictToLineParts


def test_dict_to_line_parts():

    line_parts = ConversorDictToLineParts.map({
        'field1' : 1,
        'field2' : 2,
        'field3' : 3,
    })
    
    assert line_parts.get_all_positions() == (1, 2, 3)