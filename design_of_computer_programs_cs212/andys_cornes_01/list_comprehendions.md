# Tips for python

## List Comprehensions

### First example: Turn uppercase 

```python
udacity_tas = ['Peter', 'Andy', 'Sarah', 'Gundega', 'Job', 'Sean']

uppercase_tas = [name.upper() for name in udacity_tas]
```

### Second example: working with tuple

```python
ta_data = [('Peter','USA', 'CS262'), ('Andy','USA', 'CS212'), ('Sarah','England', 'CS101'), ('Gundega','Latvia', 'CS373'), ('Job','USA', 'CS387'), ('Sean','USA', 'CS253')]

ta_facts = [name + ' lives in ' + country + ' and is the TA for ' + course for name, country, course in ta_data]

for row in ta_facts:
    print row
```

### Third example: if statment in list comprehensions

```python
ta_data = [('Peter','USA', 'CS262'), ('Andy','USA', 'CS212'), ('Sarah','England', 'CS101'), ('Gundega','Latvia', 'CS373'), ('Job','USA', 'CS387'), ('Sean','USA', 'CS253')]

ta_facts = [name + ' lives in ' + country + ' and is the TA for ' + course for name, country, course in ta_data if country != 'USA']

for row in ta_facts:
    print row

```

