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

#### General Rules of Big-O:

- Ignores constants

  - If runtime is 3n, BigO == O(n) & != O(3n), this is because as the data gets large,the constant doesn't matter anymore.

- The slower runtime gets precedence over the entire algorithm

  - Say you have the following code

    ```python
    def bigO(n,m): # O(n^2)
        x = 1 #O(1)
        y = 2 #O(1)
        for i in range(0,n): #O(n)
            for j in range(0, m): #O(n)
                x += i #O(1) * O(n^2)
                y += j #O(1) * O(n^2)
        return (x, y)
    ```

    the overall runtime of this code is now O(n^2) even though there are constant operations in the algorithm.

Order of *time complexities* from fastest to slowest:

`O(1)  < O(log n) <  O(N) < O(n*log n) < O(n^2) < O(2^n) < O(n!)`

- Constant time(O(1)) - these are operations that do not depend on the input size, N

  - ```python
def constant_example(): # O(1)
        x = 5 #O(1)
        y = 5 #O(1)
        return (x + y) #O(1)
    ```

    

- Logarithmic time (O(Log N)) - 

- Linear time (O(n)) - As the size of the input increases, the time it takes to run the algorithm increases

  - ```python
    array = [1,2,3,4,5,...,100]
    
    def linear_example(array): # O(n)
        total = 0 # O(1)
        for i in range(len(array)): # O(n)
            total += array[i] # O(1) * O(n) -> O(n)
    return (total) # O(1)
    ```
    
  - 