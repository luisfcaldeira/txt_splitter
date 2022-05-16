from application.file_conversor import FileConversor

fields = {
    'TIPREG' : 2
    , 'DATA' : 10
    , 'CODBDI' : 12
    , 'CODNEG' : 24
    , 'TPMERC' : 27
    , 'NOMRES' : 39
    , 'ESPECI' : 49
    , 'PRAZOT' : 52
    , 'MODREF' : 56
    , 'PREMAX' : 82
    , 'PREMIN' : 95
    , 'PREMED' : 108
    , 'PREULT' : 121
    , 'TOTNEG' : 152
    , 'QUATOT' : 170
    , 'VOLTOT' : 188
    , 'PREEXE' : 201
    , 'INDOPC' : 202
    , 'DATVEN' : 210
    , 'FATCOT' : 217
    , 'PTOEXE' : 230
    , 'CODISI' : 242
    , 'DISMES' : 245
}

file_conversor = FileConversor(fields)

file_conversor.add_field('PREOFC', 134)
file_conversor.add_field('PREOFV', 147)
file_conversor.add_field('PREABE', 69)

file_conversor.to_csv("example.txt", "example.csv", open_mode='w')
