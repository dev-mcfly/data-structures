# Sets

Mathematically a **set** is a collection of items not in any particular order.

- The elements in the set cannot be duplicates.
- The elements in the set are immutable but the set as a whole is mutable.
- There is no index attached to any element in a python set.

the **sets** in python are typically used for mathematical operations like union, intersection, difference and complement etc.

#### Creating a Set
A set is created by using the *set()* function or placing all the elements within curly braces.
```
Days = set(['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
print(Days) #  set(['Wed', 'Sun', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])

Months = {'Jan', 'Feb', 'Mar'}
print(Months) # set(['Jan', 'Mar', 'Feb'])

Dates = {21, 22, 17}
print(Dates) # set([17, 21, 22])
```

#### Accessing Values in a Set
We cannot access individual values in a set. But we can get a list of individual elements by looping through the set.
```
Days = set(['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

for d in Days:
  print(d) # Wed, Sun, Fri, Tue, Mon, Thu, Sat
```

#### Adding Items to a Set
We can add elements to a set by using the *add()* method.
```
Days = set(['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat'])
Days.add('Sun')

print(Days) # set(['Wed', 'Sun', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])
```

#### Removing Item from a Set
We can remove elements from a set by using the *discard()* method.
```
Days = set(['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
Days.discard('Sun')

print(Days) # set(['Wed', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])
```

### Union of Sets (|)
The union operation on two sets produces a new set containing all the distinct elements from both sets.
```
DaysA = set(['Mon', 'Tue', 'Wed'])
DaysB = set(['Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

AllDays = DaysA | DaysB
print(AllDays) # set(['Wed', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])
```

### Intersection of Sets (&)
The intersection operation on two sets produces a new set containing only the common elements from both sets.
```
DaysA = set(['Mon', 'Tue', 'Wed'])
DaysB = set(['Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

AllDays = DaysA & DaysB
print(AllDays) # set(['Wed'])
```

### Difference of Sets (-)
The difference operation on two sets produces a new set containing only the elements from the first set and none from the second set.
```
DaysA = set(['Mon', 'Tue', 'Wed'])
DaysB = set(['Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

AllDays = DaysA - DaysB
print(AllDays) # set(['Mon', 'Tue'])
```

### Compare Sets
We can check if a given set is a subset or superset of another set. The result is True or False depending on the elements present in the sets.
```
DaysA = set(['Mon', 'Tue', 'Wed'])
DaysB = set(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

SubsetRes = DaysA <= DaysB
print(SubsetRes) # True

SupersetRes = DaysB >= DaysA
print(SupersetRes) # True
```
