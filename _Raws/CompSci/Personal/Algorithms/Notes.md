# Big O Notation

Used to quantify the performance of various algorithms as input size grows.

## Constant time ($O(1)$) complexity

An algorithm that takes the same amount of time to run independent of the size of the input data

```python
def getFirst(my_list):
    return my_list[0]
```

The function `getFirst` will always take the same amount of time to retrieve the first element in a passed list

## Linear Time ($O(n)$) complexity

An algorithm whose execution time is directly proportional to the size of the input

```python
def getSum(my_list):
    sum = 0
    for item in list:
        sum += item
    return sum
```

Notice that in the main loop of the function `getSum` the number of iterations it performs increases linearly with an increasing value of $n$ resulting in $O(n)$ complexity

## Quadratic Time ($O(n^2)$) complexity

An algorithm whose execution time is proportional to the square of the input size

```python
def getSum(my_list):
    sum = 0
    for row in my_list:
         for item in row:
            sum += 0
    return sum
```

Note that the nested inner loop within the other main loop gives this code a complexity of $O(n^2)$

## Logarithmic Time ($O(\log n)$) complexity

An algorithm whose execution time is proportional to the logarithm of the input size, i.e.with each iteration the input size decreases by a constant multiple factor.

```python
def searchBinary(my_list, item):
    first = 0
    last = len(my_list) - 1
    foundFlag = False
    while first <= last and not foundFlag:
        mid = (first + last) // 2
        if my_list[mid] == item:
            foundFlag = True
        else:
            if item < my_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag
```

# Validating Algorithms

###### Deterministic Algorithm

A particular input always generates the exact same output

###### Randomized Algorithm

A random sequence of numbers is taken along with an input which alters the output every time the algorithm is run.

###### Exact Algorithm

Algorithms expected to produce a precise solution without introducing any assumptions or approximations

###### Approximate Algorithm

Algorithms that deal with a complex problem by making assumptions.
