# Idea of the project:

The program takes an input size (n) from the user, then the program decides to use insertion sort or quick sort based on (n). If the size is greater than the threshold value, then the quicksort algorithm for that part of the array is called. Else, insertion sort is called.


## _Introduction:_

There are many different sorting algorithms, each with its advantages and disadvantages. Sorting algorithms can be classified by: The amount of extra memory they use (in-place algorithms do not use any extra memory, while others require additional memory for storing temporary results) and the type of data they can handle (some algorithms are designed specifically for sorting numbers, others for sorting strings, and so forth) The speed of the sorting algorithm (some are faster than others). sorting algorithm has many types include the selection sort, insertion sort, merge sort, quick sort, comparison sort, bubble sort, heap sort. Time complexity is of essence in sorting of algorithms as it shows how much time is taken by an algorithm to carry out a set of instructions. The table below shows different algorithms and their time complexities.

<img width="591" alt="Screen Shot 2023-04-20 at 9 07 47 PM" src="https://user-images.githubusercontent.com/109047961/233451350-5c6d80ab-a1b6-4e31-a77f-a2387232490d.png">


For this project, two algorithms are chosen: insertion sort and quick sort. Also, another algorithm is created which is a hybrid one that combines both the insertion and quick sort.


## _Implementation:_

I have used a random seed to pass the current time (time.time()). So, it is continuously giving a different seed and therefore producing random arrays. To save the results and compare between the three algorithms, I created 3 arrays having exactly the current random arrays’ values and ran them to the algorithms. Moreover, the focus was on the running time instead of the time complexity of the three algorithms due to the random seed generator. Table below shows the results, based on the average case:

<img width="595" alt="Screen Shot 2023-04-20 at 9 18 52 PM" src="https://user-images.githubusercontent.com/109047961/233453495-9c6b1660-6244-41a9-bdc1-89daa9cc1279.png">

The program clearly notices the best execution time is hybrid sort, we can illustrate from table 2 that in size 10000 the execution time for insertion and quick sort is and 4497.26ms and 26.44ms respectively while the execution time for hybrid sort only take about 18.12ms.
The time complexity of insertion sort when the size is less than 17 is linear 𝑂(𝑛), while quick sort 𝑂(𝑛 log 𝑛). Therefore, the hybrid sort significantly reduced time complexity.


## _Analysis:_

Insertion Sort is a non-recursive (iterative) sorting algorithm thus it is more efficient when the number of inputs (n) is small as the number of comparisons and swaps are fewer, On the other hand, Quick sort becomes more efficient when the size of the input is large. so, we combine the two algorithms in the Hybrid sort for an effective outcome.
The criteria we have decided to deal with is the input size (n) so the HYBRID-SORT algorithm calls one of the two algorithms based on it. The value that determines when the Hybrid algorithm should work with the Insertion, or the Quick Sort is the threshold. The threshold value determines which algorithm is best based on input size. 

After Trying different numbers to be the cross-over value with respect to the input, the conclusion is that the optimal threshold value is found to be 17. It means that whenever the input size is 17 or less, the Hybrid algorithm will direct it to the Insertion Sort, and whenever it is more than 17, the input will be directed to the Quick Sort.

## _Conclusion:_
Hybrid algorithm is often used in optimization problems, where the goal is to find the best solution from a set of possible solutions with least time taken to sort. This project had proven in detail how the Hybrid Quick sort algorithm with respect to a specific threshold value is a better solution than either Insertion sort or Quick sort algorithms individually, in terms of running time.


