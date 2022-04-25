import os
from application.file_conversor import FileConversor


def test_create_file():
    file_src = 'test_file.txt'
    file_dest = 'test_file.csv'

    fields = {
        'field_1' : 10 
        ,'field_2' : 20 
        ,'field_3' : 30 
        ,'field_4' : 40 
    }

    with open(file_src, 'w') as fp:
        fp.write("        01        X2        A3       123")
        fp.write("        01        Y2        B3       456")
        fp.write("        01        Z2        C3       789")
        fp.close()

    file_conversor = FileConversor(fields)
    file_conversor.to_csv(file_src = file_src, file_destination=file_dest, sep=';')

    lines_test = [
        'field_1;field_2;field_3;field_4\n'
        , '01;X2;A3;123\n'
        , '01;Y2;B3;456\n'
        , '01;Z2;C3;789\n'
    ]

    with open(file_dest, 'r') as fp:
        lines_result = fp.readlines()
        
        for i in range(0, len(lines_result)):
            assert lines_result[i] == lines_test[i]

        fp.close()

    os.remove(file_src)
    os.remove(file_dest)
    