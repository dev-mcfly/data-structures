# Dictionaries

A **dictionary** is a set of key-value pairs, where each key is separated from its value by a colon (:). The items are separated by commas and the whole thing is enclosed in curly braces.

Key are unique within a dictionary while values may not be. *The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.*

#### Accessing Values in Dictionaries
To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.
```
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print('dict['Name']: ', dict['Name']) # dict['Name']: Zara
print('dict['Age']: ', dict['Age']) # dict['Age']: 7

# Attempt to access a data item with a key which is not in the dictionary
print('dict['Alice']: ', dict['Alice']) # KeyError
```

#### Updating Dictionaries
You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry.
```
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8 # Updating existing entry
dict['School'] = "DPS School" # Adding new entry
```
