# Two pointers

For a sorted or unsorted array, the two pointers technique uses two pointer $i$ and $j$ to traverse the array in linear
time, usually starting from the most extreme ends of the array and moving semi-independently

## Patterns

- Finding the duplicate number in an array of size $n+1$ in the range $[1, n]$ inclusive [267](https://leetcode.com/problems/find-the-duplicate-number/description/) - An array of this type can be treated as a linked list where the value at each index is the next index to visit. Using this the two pointers become the current index of the array and the next index to visit. We then:
    - Traverse the array in this way until the two pointers meet guaranteeing a meeting point inside he cycle.
    - Reset one pointer to the start of the array and move both pointer one step at a time until they meet again.
    - The meeting point is the duplicate number.
