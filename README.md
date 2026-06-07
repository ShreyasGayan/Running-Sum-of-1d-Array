1480. Running Sum of 1D Array
Problem Statement

Given an array nums, return the running sum of the array.

The running sum of an array is defined as:

runningSum[i] = nums[0] + nums[1] + ... + nums[i]
Examples
Example 1
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Explanation:

[1,
 1+2,
 1+2+3,
 1+2+3+4]

= [1,3,6,10]
Example 2
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Explanation:

[1,
 1+1,
 1+1+1,
 1+1+1+1,
 1+1+1+1+1]

= [1,2,3,4,5]
Example 3
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
Approach

To calculate the running sum, we iterate through the array starting from index 1.

For each element:

nums[i] = nums[i] + nums[i-1]

Since nums[i-1] already contains the running sum up to the previous index, adding it to the current element gives the running sum up to i.

This allows us to modify the array in-place without using extra space.

Algorithm
Traverse the array from index 1 to n-1.
Add the previous running sum to the current element.
Store the result back in the current position.
Return the modified array.


Complexity Analysis
Time Complexity
O(n)

We traverse the array once.

Space Complexity
O(1)

The computation is performed in-place without using extra memory.

Concepts Used
Arrays
Prefix Sum
In-Place Modification
Iteration
