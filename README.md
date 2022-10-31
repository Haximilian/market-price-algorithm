# market-price-algorithm

This implements the algorithm described by David Easley and Jon Kleinberg in their [Networks, Crowds and Markets](https://www.cs.cornell.edu/home/kleinber/networks-book/) book.

For example, if buyers have valuations equal to

```
[
    [10, 2, 5, 2, 0, 0, 0, 0],
    [32, 23, 23, 6, 0, 0, 0, 0],
    [12, 55, 77, 11, 0, 0, 0, 0],
    [5, 6, 23, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 10, 2, 5, 2],
    [0, 0, 0, 0, 32, 23, 23, 6],
    [0, 0, 0, 0, 12, 55, 77, 11],
    [5, 6, 23, 3, 0, 0, 0, 0]
]
```

The prices that results in a perfect match equal to

```
[10, 5, 22, 2, 8, 0, 3, 0]
```
