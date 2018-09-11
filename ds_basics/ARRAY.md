# Array

An **array** is a container which can hold a fix number of items and these items should be of the same type. Most of the data structures make use of arrays to implement their algorithms.

- **Element**: Each item stored in an array is called an element.
- **Index**: Each location of an element in an array has a numerical index, which is used to identify the element.

### Array Representation
Arrays can be declared in various ways in different languages.
```
int array[10] = { 35, 33, 42, 10, 14, 19, 27, 44, 26, 31 }

elements : 35 33 42 10 14 19 27 44 26 31
index    :  0  1  2  3  4  5  6  7  8  9
```
- Index starts with 0.
- Array length is 10 which means it can store 10 elements.
- Each element can be accessed via its index.

#### Basic Operations
Following are the basic operations supported by an array.
- **Traverse**: print all the elements one by one.
- **Insertion**: Adds an element at the given index.
- **Deletion**: Deletes an element at the given index.
- **Search**: Searches an element using the given index or by the value.
- **Update**: Updates an element at the given index.

```
from array import *

<!-- arrayName = array(typecode, [Initializers]) -->
array1 = array('i', [10, 20, 30, 40, 50])

for x in array1:
  print(x) # 10 20 30 40 50
```

#### Accessing Array Elements
We can access each element of an array using the index of the element.
```
print(array1[0]) # 10
print(array1[2]) # 30
```

#### Insertion Operation
Insert operation is to insert one or more data elements into an array. A new element can be added at the beginning, end, or any given index of array.
```
array1.insert(1, 60)

for x in array1:
  print(x) # 10 60 20 30 40 50
```

#### Deletion Operation
Deletion refers to removing an existing element from the array and re-organizing all elements of an array.
```
array1 = array('i', [10, 20, 30, 40, 50])

array1.remove(40)

for x in array1:
  print(x) # 10 20 30 50
```

#### Search Operation
You can perform a search for an array element based on its value or its index.
```
array1 = array('i', [10, 20, 30, 40, 50])

print(array1.index(40)) # 3
```

#### Update Operation
Update operation refers to updating an existing element from the array at a given index.
```
array1 = array('i', [10, 20, 30, 40, 50])

array1[2] = 80

for x in array1:
  print(x) # 10 20 80 40 50
```
