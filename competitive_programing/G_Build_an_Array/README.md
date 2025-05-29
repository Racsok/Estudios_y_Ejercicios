# G. Build an Array

Yesterday, Dima found an empty array and decided to add some integers to it. He can perform the following operation an unlimited number of times:

* add any integer to the left or right end of the array.
* then, as long as there is a pair of identical adjacent elements in the array, they will be replaced by their sum.

It can be shown that there can be at most one such pair in the array at the same time.

For example, if the array is **[3,6,4]** and we add the number 3 to the left, the array will first become **[3,3,6,4]**, then the first two elements will be replaced by 6, and the array will become **[6,6,4]**, and then — **[12,4]**.

After performing the operation exactly k times, he thinks he has obtained an array a of length n, but he does not remember which operations he applied. Determine if there exists a sequence of k operations that could result in the given array a from an empty array, or determine that it is impossible.

## Input
The first line contains a single integer t *(1 ≤ t ≤ 104)* — the number of test cases. The descriptions of the test cases follow.

The first line of each test case description contains two integers n and k *(1 ≤ n ≤ 105, n ≤ k ≤ 106)* — the length of the resulting array and the number of operations.

The second line contains n integers a *(1 ≤ ai ≤ 109, ai − 1 ≠ ai)* — the elements of the resulting array.

It is guaranteed that the sum of the values of n across all test cases does not exceed 105.

## Output
For each test case, if there is no suitable sequence of operations of length k, output "NO". Otherwise, output "YES".

You may output **"YES"** and **"NO"** in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).