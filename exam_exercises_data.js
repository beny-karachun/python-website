// Auto-generated Exam Exercises data
const EXERCISES_DATA = {
    "categories": [
        {
            "name": "Recursion Patterns",
            "problems": [
                {
                    "id": "subset_count",
                    "name": "Subset Sum (Count Ways)",
                    "description": "Write a function `count_ways(lst, summ)` that receives a list of numbers `lst` and a target sum `summ`. The function should return the number of different ways to choose a subset from the list whose sum exactly equals `summ`.\n\n**Instructions:**\n- You must use recursion.\n- You may assume all numbers are positive.",
                    "stub": "def count_ways(lst, summ):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "count_ways([1, 5, 3, 2, 6, 8, 3], 9)", "expected": "4" },
                        { "call": "count_ways([1, 2, 3], 3)", "expected": "2" },
                        { "call": "count_ways([1, 2], 5)", "expected": "0" }
                    ]
                },
                {
                    "id": "subset_max",
                    "name": "Max Fit Items",
                    "description": "Write a function `max_items(lst, summ)` that receives a list of numbers and a target sum. The function should return the **maximum number** of elements that can be taken from the list such that their sum equals exactly the target.\n\nIf there is no subset that matches the sum, return `-1`.",
                    "stub": "def max_items(lst, summ):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "max_items([1, 5, 3, 2, 6, 8, 3], 9)", "expected": "3" },
                        { "call": "max_items([4, 5], 10)", "expected": "-1" },
                        { "call": "max_items([1, 1, 1, 1], 2)", "expected": "2" }
                    ]
                },
                {
                    "id": "subset_bool",
                    "name": "Is Possible (Subset Sum)",
                    "description": "Write a function `is_possible(lst, summ)` that returns `True` if a subset can be chosen from the list whose sum is exactly equal to `summ`, and `False` otherwise.",
                    "stub": "def is_possible(lst, summ):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "is_possible([1, 5, 3, 2, 6, 8, 3], 8)", "expected": "True" },
                        { "call": "is_possible([1, 5, 3, 2, 6, 8, 3], 135)", "expected": "False" },
                        { "call": "is_possible([10, 20], 30)", "expected": "True" }
                    ]
                },
                {
                    "id": "subset_closest",
                    "name": "Closest Sum Under Max",
                    "description": "Write a function `closest_sum(lst, max_val, value=0)` that returns the largest sum that can be formed from the list which **does not exceed** `max_val`.",
                    "stub": "def closest_sum(lst, max_val, value=0):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "closest_sum([5, 3, 9, 4], 11)", "expected": "9" },
                        { "call": "closest_sum([1, 2, 3], 10)", "expected": "6" },
                        { "call": "closest_sum([10, 20], 5)", "expected": "0" }
                    ]
                }
            ]
        },
        {
            "name": "Sorting Algorithms",
            "problems": [
                {
                    "id": "bucket_sort",
                    "name": "Bucket Sort (Histogram)",
                    "description": "Implement the function `bucket_sort(lst, max_val)` which receives a list of positive integers (including 0) and the maximum possible value `max_val`, and sorts the list using the counting array method (histogram). The function should return a new sorted list.\n\n**Required Time Complexity: O(n)**",
                    "stub": "def bucket_sort(lst, max_val):\n    # TODO: implement array counting approach\n    pass\n",
                    "tests": [
                        { "call": "bucket_sort([4, 2, 2, 8, 3, 3, 1], 8)", "expected": "[1, 2, 2, 3, 3, 4, 8]" },
                        { "call": "bucket_sort([0, 1, 0, 1], 1)", "expected": "[0, 0, 1, 1]" }
                    ]
                },
                {
                    "id": "bubble_sort",
                    "name": "Bubble Sort",
                    "description": "Write a function `bubble_sort(lst)` that sorts the list in-place by bubbling the largest element to the end of the array in each iteration. Return the list.",
                    "stub": "def bubble_sort(lst):\n    # TODO: implement\n    pass\n",
                    "tests": [
                        { "call": "bubble_sort([64, 34, 25, 12, 22, 11, 90])", "expected": "[11, 12, 22, 25, 34, 64, 90]" },
                        { "call": "bubble_sort([3, 2, 1])", "expected": "[1, 2, 3]" }
                    ]
                }
            ]
        },
        {
            "name": "Search Algorithms",
            "problems": [
                {
                    "id": "binary_search",
                    "name": "Binary Search (Iterative)",
                    "description": "Write a function `binary_search(lst, target)` that receives a sorted list of numbers `lst` and a target number `target`. The function will perform a binary search using a loop (iterative) and return the **index** of the target. If it does not exist, return `-1`.",
                    "stub": "def binary_search(lst, target):\n    # TODO: implement iterative binary search\n    pass\n",
                    "tests": [
                        { "call": "binary_search([2, 3, 4, 10, 40], 10)", "expected": "3" },
                        { "call": "binary_search([2, 3, 4, 10, 40], 5)", "expected": "-1" }
                    ]
                },
                {
                    "id": "binary_search_rec",
                    "name": "Binary Search (Recursive)",
                    "description": "Write a function `binary_search_rec(lst, target, low, high)` that performs the same binary search on the sorted array, but this time using a **recursive** approach.",
                    "stub": "def binary_search_rec(lst, target, low, high):\n    # TODO: implement recursive binary search\n    pass\n",
                    "tests": [
                        { "call": "binary_search_rec([2, 3, 4, 10, 40], 10, 0, 4)", "expected": "3" },
                        { "call": "binary_search_rec([2, 3, 4, 10, 40], 5, 0, 4)", "expected": "-1" }
                    ]
                }
            ]
        }
    ]
};
