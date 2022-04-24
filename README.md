# How to Split String By The Position Of Character in Python?
I got the solution for your problem right here!

# How to do

Keep this example in mind:

A file:
```txt
        01        X2        A3       123
        01        Y2        B3       456
        01        Z2        C3       789
```

All you need to do is to create a dictionary with the names of columns and what's the last char position in the source file of that field, so you should to do as the example below:

```python

fields = {
    'field_1' : 10 # note that the first field ends in the position #10. Count it to checkout what I'm saying...
    'field_2' : 20 
    'field_3' : 30 
    'field_4' : 40 # note that the last field ends in the position #40
}

file_conversor = FileConversor()

file_conversor.set_file_configuration(fields)

file_conversor.to_csv("source_file.txt", "dest_file.csv")

```

This will generate a csv file as it follows that you can use in any other tool (Pandas, for example):

```python
field_1;field_2;field_3;field_4
01;X2;A3;123
01;Y2;B3;456
01;Z2;C3;789
```

You can call add_field if you want to add more fields after instanciated a ```FileConversor``` object. You don't need to worry about order, since the fields are allways sorted by its position. 

The file main.py already have a working example code you can try. 

I hope this can be helpfull!

# Requisitions

- Your file source
- A name for the output file.
