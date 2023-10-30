"""
Problem: Pair Difference

Description:
Given an integer array `arr` and an integer `k`, find all unique pairs `(i, j)` such that the difference between `i` and `j` is `k`. 

Example:
Input: arr = [1, 4, 2, 3, 5], k = 2
Output: [(1, 3), (3, 5), (2, 4)]

Note:
- The pairs should be unique. That is, (i, j) and (j, i) are considered the same and should not be duplicated.
- The order of the pairs in the output doesn't matter.

Approach:
Several approaches can be used to solve this problem, each with its own advantages and trade-offs:

1. **Hashmap (or Set in Python)**:
   - **Idea**: Use a hashmap to quickly determine if a given number plus `k` exists in the array.
   - **Steps**:
     1. For each number in the array, check if it plus `k` exists in the hashmap. If yes, add the pair to the result.
     2. To ensure the uniqueness of pairs, we can use a set to keep track of added numbers.
   - **Advantages**: This method is straightforward and provides O(n) time complexity.
   - **Trade-offs**: Uses additional O(n) space for the hashmap.

2. **Two-Pointers**:
   - **Idea**: After sorting the array, use two pointers to traverse the array and find pairs with the desired difference.
   - **Steps**:
     1. Sort the array.
     2. Initialize two pointers: one starting at the beginning and the other starting one position ahead.
     3. Move the pointers based on the difference between their pointed values until a pair with the desired difference is found.
   - **Advantages**: Uses O(1) auxiliary space after sorting.
   - **Trade-offs**: Requires the array to be sorted, which takes O(n log n) time.

"""
from typing import List, TypedDict
import cProfile
from memory_profiler import profile


sample_data = [
    {"arr": [1, 4, 2, 3, 5], "k": 2},
    {"arr": [1, 3, 5, 7, 9], "k": 2},
    {"arr": [1, 1, 3, 3, 5, 5], "k": 2},
    {"arr": [1, 3, 3, 5, 7, 7, 9], "k": 4},
    {"arr": [2, 4, 6, 8, 10], "k": 7},
    {"arr": [10, 20, 30, 40], "k": 15},
    {"arr": [1, 3, 3, 7, 7, 9], "k": 5},
    {"arr": [5], "k": 3},
    {"arr": [2, 2, 4, 4], "k": 0},
    {"arr": [2, 4], "k": 0},
]

sample_data = sample_data * 1000000


class PairDifferenceData(TypedDict):
    arr: List[int]
    k: int


# @profile
def find_pairs(data: PairDifferenceData) -> List[tuple[int, int]]:
    arr, k = data["arr"], data["k"]
    num_set = set(arr)
    pair_set = set()

    for n in arr:
        lookup_value = n + k
        if lookup_value in num_set:
            pair_set.add(tuple([n, lookup_value]))

    result = list(pair_set)
    return result


@profile
def main():
    for data in sample_data:
        find_pairs(data)


if __name__ == "__main__":
    # cProfile.run("main()")
    main()
