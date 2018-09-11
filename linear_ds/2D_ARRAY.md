# 2D Array

A **two dimensional** array is an array within an array (an array of arrays). In this type of array, positions of elements are referred to by two indices.

Consider this dataset of recorded temperatures taken 4 times a day, for 4 days.
```
Day 1 - 11 12 5 2
Day 2 - 15 6 10
Day 3 - 10 8 12 5
Day 4 - 12 15 8 6
```
The above data can be represented as a 2D array:
`T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]`

### Accessing Values in a 2D Array
The data elements in two dimensional arrays can be accessed using two indices. One index referring to the parent array and another index referring to the position of the data element in the inner array.
```
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

print(T[0]) # [11, 12, 5, 2]
print(T[1][2]) # 10
```

###  Inserting Values in a 2D Array
We can insert new data elements at specific positions by using the `insert()` method and specifying
the index.
```
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

T.insert(2, [0, 5, 11, 13, 6])
print(T[2]) # [0, 5, 11, 13, 6]
```

### Updating Values in a 2D Array
We can update the entire inner array or some specific data element of the inner array by reassigning the values using the array index.
```
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

T[2] = [11, 9]
T[0][3] = 7

print(T) # [[11, 12, 5, 7], [15, 6, 10], [11, 9], [12, 15, 8, 6]]
```

### Deleting Values in a 2D Array
We can delete the entire inner array of some specific data elements of the inner array by reassigning the values using the `del()` method with index.
```
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

del T[3]

print(T) # [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5]]
```
