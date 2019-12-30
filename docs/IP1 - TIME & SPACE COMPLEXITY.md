# IP1 - TIME & SPACE COMPLEXITY

### <u>Big-O Notation</u>

This is simply a way to identify the runtime of an algorithm. To identify the efficiency of an algorithm. 

Big-O is used to analyze the time and space complexity of an algorithm. 

- Time complexity being the runtime of our algorithm.
- Space complexity being the memory usage of our algorithm.



There are 3 measurements we focus on when talking time & space complexities:

1. Worst - Case -> **Big-O cares about this the most!**
2. Best - Case
3. Average case

Order of Big-O from fastest to slowest:

`O(1)  < O(Log N) <  O(N) < O(N LogN) < O(N^2) < O(N!)`

- Constant time(O(1)) - these are usually from calculations that don't require traversals of data structures.

  - ```python
    x = 5 #O(1)
    y = 5 #O(1)
    print (x + y) #O(1)
    ```

    

- Logarithmic time (O(Log N)) - 