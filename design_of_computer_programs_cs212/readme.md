# Design of Computer Programs

This course has the idea to improve the skills in the development of programs.

The main language used in this course is Python.

## Some tips learned in this course

### List Comprehension

The main ideia behind the use of list comprehension is the possibility
to help the writing for clauses and insert the same in a list structure.

```python
# A list comprehension can be defined in the following way

[ s for r,s in cards
    	    if r in 'JQK' ]

# where `s` is a term and `for r,s in cards` is a for clause used to
# create the list. It is possible to expand the list comprehension
# using more for and if clauses.

# This is equivalent to

result = []
for r,s in cards:
    if r in 'JQK':
       result.append(s)

```

### Generator Expressions

The generator expression have the similar ideia from list
comprehension. They have two differences.

First of all the generator expressions uses paretheses instead of
square brackets.

Second the computation wasn't done at once. Instead, a generator
expression returns a value with a 'promisse' to do this computation
later.

Let's take an example.

```python
# we define a function
def sq(x): print 'sq called', x; return x * x

# defining the generator
g = (sq(x) for x in xrange(4) if x%2 == 0)

# getting the next g
next(g)
>> sq called 0
# getting the next g
next(g)
>> sq called 2
# getting the next g
next(g)
>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

# This happen because the ideia is use with for loop.

# defining the generator
h = (sq(x) for x in xrange(10) if x%2 == 0)

for x2 in h:
    pass

sq called 0
sq called 2
sq called 4
sq called 6
sq called 8

# I can insert in a list, such as

# defining the generator
k = (sq(x) for x in xrange(10) if x%2 == 0)

list(k)
sq called 0
sq called 2
sq called 4
sq called 6
sq called 8
[0, 4, 16, 36, 64]
```