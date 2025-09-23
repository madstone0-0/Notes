## Prefix Sum

For an array $A$, the prefix sum $P$ is an array containing the sum of elements $A[0] + .. + A[i]$ where $i$ is the
index of the array $P$, i.e.
$$
P[i] = \sum_{j=0}^{i} A[j]
$$

## Suffix sum

For an array $A$ the suffix sum $S$ is an array containing the sum of elements $A[i] + A[i + 1]  + A[i + 2] + ... + A[i 1]$ where $i$ is the index of the array $S$, i.e.
$$
S[i] = \sum_{j=i}^{n-1} A[j]
$$

## Patterns

- Product/Sum of all array except self [238](https://leetcode.com/problems/product-of-array-except-self/description/) -
The normal prefix/suffix sum algorithm includes the current element in the sum arrays must be computed:
$$
P[i] = \sum_{j=0}^{i-1} A[j]
$$
And
$$
S[i] = \sum_{j=i+1}^{n-1} A[j]
$$
And the final result is computed as:
$$
R = P[i] * S[i]
$$
