# Lists

The **list** is the most versatile datatype available in python. It can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.
```
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
```

Similar to string indices, list indices start at 0, and lists can be sliced, concatenated and so on.

### Basic List Operations
Lists respond to the + and * operators much like strings, except that the result is a new list, not a string.

|  Python Expression 	      |  	      Results            |    Description   |
|:---:	                    |:---:	                     |:---:	            |
|    len([1, 2, 3])         |   	       3               |      Length 	    |
| [1, 2, 3]+[4, 5, 6]       |     [1, 2, 3, 4, 5, 6]     |   Concatenation	|  
|   	 ['Hi!']*4            |['Hi!', 'Hi!', 'Hi!', 'Hi!']|    Repetition	  |
|    3 in [1, 2, 3]         |           True           	 |    Membership	  |
| for x in [1,2,3]: print x |           1 2 3            |    Iteration	    |

#### Accessing Values in Lists
```
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print('list1[0]: ', list1[0]) # physics
print('list2[1:5]', list2[1:5]) # [2, 3, 4, 5]
```

#### Updating Lists
```
list = ['physics', 'chemistry', 1997, 2000]
print('Value at index 2: ', list[2]) # Value at index 2: 1997

list[2] = 2001
print('New value at index 2: ', list[2]) # New value at index 2: 2001
```

#### Delete List Elements
To remove an element, you can use either the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know.
```
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1) # ['physics', 'chemistry', 1997, 2000]

del list1[2]
print('New list1: ', list1) # ['physics', 'chemistry', 2000]
```
