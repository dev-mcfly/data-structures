# Tuples

A **tuple** is a sequence of immutable Python objects. The difference between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses.
```
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = 'a', 'b', 'c', 'd'
```

The empty tuple is written as two parentheses containing nothing -
```
tup1 = ()
```

A tuple containing a single value must include a comma, even though there is only one value -
```
tup1 = (50,)
```

### Basic Tuple Operations

|  Python Expression 	      |  	      Results            |    Description   |
|:---:	                    |:---:	                     |:---:	            |
|    len((1, 2, 3))         |   	       3               |      Length 	    |
| (1, 2, 3)+(4, 5, 6)       |     (1, 2, 3, 4, 5, 6)     |   Concatenation	|  
|   	 ['Hi!']*4            |('Hi!', 'Hi!', 'Hi!', 'Hi!')|    Repetition	  |
|    3 in (1, 2, 3)         |           True           	 |    Membership	  |
| for x in (1,2,3): print x |           1 2 3            |    Iteration	    |


#### Accessing Values in Tuples
```
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)

print('tup1[0]: ', tup1[0]) # tup1[0]: physics
print('tup2[1:5]: ', tup2[1:5]) # tup2[1:5]: [2, 3, 4, 5]
```

#### Updating Tuples
Tuples are **immutable** which means you cannot update or change the values of tuple elements.

#### Delete Tuple Elements
Removing individual tuple elements is not possible. To explicitly remove an entire tuple, just use the **del** statement.
```
tup = ('physics', 'chemistry', 1997, 2000)
print(tup) # ('physics', 'chemistry', 1997, 2000)

del tup
print(tup) # NameError
```
