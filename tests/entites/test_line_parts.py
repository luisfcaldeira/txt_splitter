from domain.entities.line_parts import LineParts, DefaultField


def test_the_order_of_elements():
    line_part = LineParts()
    line_part.add_part('field_name3', 3)
    line_part.add_part('field_name', 1)
    line_part.add_part('field_name2', 2)

    assert line_part.get_all_positions() == (1, 2, 3)


def test_theres_no_field():
    line_part = LineParts()

    assert len(line_part) == 0
    assert DefaultField() == line_part.get_all_field_names()[0]

def test_if_it_is_counting_right():
    line_part = LineParts()
    line_part.add_part('field_name', 1)
    line_part.add_part('field_name2', 2)
    line_part.add_part('field_name3', 3)
    assert len(line_part) == 3


def test_result_all_parts():
    line_part = LineParts()
    line_part.add_part('field_name', 1)
    line_part.add_part('field_name2', 2)
    line_part.add_part('field_name3', 3)

    print(line_part.get_all_positions())