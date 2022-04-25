from services.splitter import Splitter

def test_split_right():
    splitter = Splitter()
    line = 'ABC DEF GHI'

    assert splitter.split_by_pos(line, 3)[0] == 'ABC'

def test_split_many_columns():
    splitter = Splitter()
    line = 'ABC DEF GHI'

    fields = splitter.split_by_pos(line, 4, 8, 11)

    assert len(fields) == 3
    assert fields[0] == 'ABC'
    assert fields[1] == 'DEF'
    assert fields[2] == 'GHI'