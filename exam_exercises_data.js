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
                    "id": "subset_count_scenario1",
                    "name": "Budget Variations",
                    "description": "You are organizing a Hackathon and have a specific budget `target_budget` (in thousands). You are presented with a list of project proposals, `proposals`, each with an associated cost. Write a recursive function `budget_variations(proposals, target_budget)` that calculates exactly how many different combinations of projects you can fund using exactly the target budget.",
                    "stub": "def budget_variations(proposals, target_budget):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "budget_variations([10, 20, 15, 5, 25, 30], 40)", "expected": "3" },
                        { "call": "budget_variations([5, 5, 5, 5], 10)", "expected": "6" },
                        { "call": "budget_variations([100, 200], 50)", "expected": "0" }
                    ]
                },
                {
                    "id": "subset_count_scenario2",
                    "name": "Team Weight Balance",
                    "description": "For a tug-of-war competition, you need to form a team from a list of players whose weights are given in `weights`. The team's total weight must exactly match the `weight_limit` of the category. Write a recursive function `team_formations(weights, weight_limit)` that returns how many valid teams can be formed.",
                    "stub": "def team_formations(weights, weight_limit):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "team_formations([60, 70, 80, 50, 90, 60], 140)", "expected": "3" },
                        { "call": "team_formations([50, 50], 100)", "expected": "1" },
                        { "call": "team_formations([40, 45, 50], 150)", "expected": "0" }
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
                    "id": "subset_max_scenario1",
                    "name": "File Storage Optimizer",
                    "description": "You have a flash drive with exactly `usable_space` megabytes left. You have a list of files with sizes given in `file_sizes`. You want to transfer as many files as possible, but you must use exactly 100% of the available space to satisfy a strict quota policy. Write a recursive function `max_files_transferred(file_sizes, usable_space)` that returns the maximum number of files you can move. Return -1 if it's impossible to perfectly fill the space.",
                    "stub": "def max_files_transferred(file_sizes, usable_space):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "max_files_transferred([100, 50, 200, 50, 150], 300)", "expected": "3" },
                        { "call": "max_files_transferred([500, 400], 800)", "expected": "-1" },
                        { "call": "max_files_transferred([10, 10, 10, 30], 30)", "expected": "3" }
                    ]
                },
                {
                    "id": "subset_max_scenario2",
                    "name": "Bus Capacity Fulfillment",
                    "description": "A tour bus dictates it will only leave if it is at exactly 100% capacity (`bus_seats` seats). Groups of tourists are waiting, their sizes given in `groups`. To maximize the number of distinct groups that get to go, write a recursive function `max_tourist_groups(groups, bus_seats)` that finds the maximum number of groups that perfectly fill the bus. Return -1 if it's not possible.",
                    "stub": "def max_tourist_groups(groups, bus_seats):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "max_tourist_groups([2, 4, 3, 1, 5, 6], 10)", "expected": "4" },
                        { "call": "max_tourist_groups([3, 3, 4], 5)", "expected": "-1" },
                        { "call": "max_tourist_groups([2, 2, 2, 2, 8], 8)", "expected": "4" }
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
                    "id": "subset_bool_scenario1",
                    "name": "Exact Change Checker",
                    "description": "A vending machine requires exact change. The coins a user has are provided in the list `coins`. The price of the snack is `price`. Write a recursive function `can_pay_exact(coins, price)` that returns True if the user can put in exactly the required amount without needing change, or False otherwise.",
                    "stub": "def can_pay_exact(coins, price):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "can_pay_exact([5, 10, 10, 1], 21)", "expected": "True" },
                        { "call": "can_pay_exact([5, 10, 10], 12)", "expected": "False" },
                        { "call": "can_pay_exact([1, 2, 5, 10, 20], 18)", "expected": "True" }
                    ]
                },
                {
                    "id": "subset_bool_scenario2",
                    "name": "Cargo Loading Approval",
                    "description": "A cargo plane has exactly `weight_allowance` tons of capacity remaining that must be filled. You have a manifest of shipping containers with various weights given in `containers`. Write a recursive function `approve_cargo(containers, weight_allowance)` that returns True if you can uniquely select a combination of containers to perfectly hit the remaining capacity weight limit.",
                    "stub": "def approve_cargo(containers, weight_allowance):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "approve_cargo([2.5, 3.0, 1.5, 5.0, 4.0], 8.0)", "expected": "True" },
                        { "call": "approve_cargo([10, 20, 30], 15)", "expected": "False" },
                        { "call": "approve_cargo([2, 2, 2, 4], 6)", "expected": "True" }
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
                },
                {
                    "id": "subset_closest_scenario1",
                    "name": "Gift Card Maximizer",
                    "description": "You received a gift card with a balance of `card_limit`. You want to spend as much of the card's balance as possible without going over. You find a list of items you like, with prices given in `prices`. Write a recursive function `maximize_gift_card(prices, card_limit)` to figure out the closest amount under or equal to the limit you can spend.",
                    "stub": "def maximize_gift_card(prices, card_limit, current=0):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "maximize_gift_card([45, 20, 15, 60, 10], 100)", "expected": "95" },
                        { "call": "maximize_gift_card([150, 200, 300], 100)", "expected": "0" },
                        { "call": "maximize_gift_card([10, 20, 30], 60)", "expected": "60" }
                    ]
                },
                {
                    "id": "subset_closest_scenario2",
                    "name": "Elevator Weight Sensor",
                    "description": "An elevator has a maximum structural limit of `elevator_max`. A group of people are waiting to enter, their weights listed in `people`. To avoid setting off the alarm while moving as much weight as possible, what is the maximum combined weight that can board the elevator safely? Write a recursive function `safe_elevator_load(people, elevator_max)`.",
                    "stub": "def safe_elevator_load(people, elevator_max, current=0):\n    # TODO: recursion\n    pass\n",
                    "tests": [
                        { "call": "safe_elevator_load([70, 80, 65, 90, 110], 300)", "expected": "295" },
                        { "call": "safe_elevator_load([200, 200], 150)", "expected": "0" },
                        { "call": "safe_elevator_load([50, 50, 60], 160)", "expected": "160" }
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
                    "id": "bucket_sort_scenario1",
                    "name": "Age Demographics Sorter",
                    "description": "A municipal database holds thousands of citizens' ages in an unordered list `ages`. You know for a fact the maximum recorded age in this dataset is `max_recorded_age`. Because the range is small and constant, normal O(n log n) sorting is too slow. Write an O(n) function `sort_ages_fast(ages, max_recorded_age)` that utilizes bucket/histogram mapping to return the sorted ages list.",
                    "stub": "def sort_ages_fast(ages, max_recorded_age):\n    # TODO: O(n) histogram sorting\n    pass\n",
                    "tests": [
                        { "call": "sort_ages_fast([25, 12, 88, 25, 12, 4], 100)", "expected": "[4, 12, 12, 25, 25, 88]" },
                        { "call": "sort_ages_fast([5, 5, 5, 1, 1], 10)", "expected": "[1, 1, 5, 5, 5]" },
                        { "call": "sort_ages_fast([], 100)", "expected": "[]" }
                    ]
                },
                {
                    "id": "bucket_sort_scenario2",
                    "name": "Test Score Ranker",
                    "description": "The Ministry of Education needs to sort exactly 1 million student scores. Every score ranges perfectly from 0 up to a known `max_score` (like 100). Implement `rank_scores(scores, max_score)` running in O(n) time, mapping the frequencies into a histogram to recreate a fully ordered list of scores.",
                    "stub": "def rank_scores(scores, max_score):\n    # TODO: O(n) histogram sorting\n    pass\n",
                    "tests": [
                        { "call": "rank_scores([95, 80, 100, 95, 80, 50], 100)", "expected": "[50, 80, 80, 95, 95, 100]" },
                        { "call": "rank_scores([1, 2, 0, 1, 2], 5)", "expected": "[0, 1, 1, 2, 2]" },
                        { "call": "rank_scores([42], 50)", "expected": "[42]" }
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
                },
                {
                    "id": "bubble_sort_scenario1",
                    "name": "Book Shelf Organizer",
                    "description": "A librarian noticed a small array of books `books_thickness` is nearly sorted. She prefers repeatedly swapping adjacent books that are out of order, shifting the thickest books to the right side of the shelf until no more swaps are needed. Write `organize_shelf(books_thickness)` reflecting this Bubble Sort methodology.",
                    "stub": "def organize_shelf(books_thickness):\n    # TODO: implement bubble sort\n    pass\n",
                    "tests": [
                        { "call": "organize_shelf([40, 20, 60, 10, 50])", "expected": "[10, 20, 40, 50, 60]" },
                        { "call": "organize_shelf([5, 4, 3, 2, 1])", "expected": "[1, 2, 3, 4, 5]" },
                        { "call": "organize_shelf([1, 2, 3])", "expected": "[1, 2, 3]" }
                    ]
                },
                {
                    "id": "bubble_sort_scenario2",
                    "name": "Network Traffic Prioritizer",
                    "description": "A basic hardware switch processes data packets and assigns an integer `urgency_level` to them. It needs to sort a small backlog queue by repeatedly iterating through adjacent packets and swapping them if the one on the left has a higher urgency. Implement `prioritize_packets(urgency_levels)` returning the sorted queue.",
                    "stub": "def prioritize_packets(urgency_levels):\n    # TODO: implement bubble sort\n    pass\n",
                    "tests": [
                        { "call": "prioritize_packets([8, 1, 4, 9, 2])", "expected": "[1, 2, 4, 8, 9]" },
                        { "call": "prioritize_packets([100, 50, 200])", "expected": "[50, 100, 200]" }
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
                    "id": "binary_search_scenario1",
                    "name": "Contact Directory Lookup",
                    "description": "A very large mobile contacts list has already extracted everyone's phone ID iteratively and stored it in an alphabetically sorted list `contact_ids`. Because of scale, looping O(n) is forbidden. Write an iterative Binary Search algorithm `find_contact(contact_ids, target_id)` to quickly find and return the index of the queried `target_id`. Return -1 if the contact doesn't exist.",
                    "stub": "def find_contact(contact_ids, target_id):\n    # TODO: iterative O(log n) lookup\n    pass\n",
                    "tests": [
                        { "call": "find_contact([1001, 1005, 1022, 1045, 1099, 1105], 1045)", "expected": "3" },
                        { "call": "find_contact([1001, 1005, 1022, 1045, 1099, 1105], 1000)", "expected": "-1" },
                        { "call": "find_contact([5, 10, 15], 15)", "expected": "2" }
                    ]
                },
                {
                    "id": "binary_search_scenario2",
                    "name": "Inventory ID Verification",
                    "description": "A warehouse system stores millions of product serials in a sorted array `serials`. An associate scanned a box reading `scanned_serial`. You must quickly verify if it belongs in the warehouse using a while-loop based Binary Search `verify_inventory(serials, scanned_serial)`. Return its list position or -1 if unauthorized.",
                    "stub": "def verify_inventory(serials, scanned_serial):\n    # TODO: iterative binary search\n    pass\n",
                    "tests": [
                        { "call": "verify_inventory([100, 200, 300, 400, 500, 600, 700], 600)", "expected": "5" },
                        { "call": "verify_inventory([100, 200, 300, 400, 500, 600, 700], 350)", "expected": "-1" },
                        { "call": "verify_inventory([42], 42)", "expected": "0" }
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
                },
                {
                    "id": "binary_search_rec_scenario1",
                    "name": "Medical Records Drill Down",
                    "description": "Hospital records are stored by sorted chronologically assigned ID arrays, `records`. Rather than a loop, the principal architect wants an elegant recursive dive `find_record(records, target, low, high)` to cut the search space in half each functional call. Return the index if found, else -1.",
                    "stub": "def find_record(records, target, low, high):\n    # TODO: recursive binary search\n    pass\n",
                    "tests": [
                        { "call": "find_record([100, 150, 200, 250, 300, 350], 200, 0, 5)", "expected": "2" },
                        { "call": "find_record([10, 20, 30], 40, 0, 2)", "expected": "-1" },
                        { "call": "find_record([55], 55, 0, 0)", "expected": "0" }
                    ]
                },
                {
                    "id": "binary_search_rec_scenario2",
                    "name": "E-Commerce Catalog Slicer",
                    "description": "To locate a product ID `query` inside a pre-sorted giant `catalog_ids` slice, the frontend web application uses a recursive method `locate_product(catalog_ids, query, low, high)` that passes the bounds recursively until the element is either flagged or missed. Implement it returning the index or -1.",
                    "stub": "def locate_product(catalog_ids, query, low, high):\n    # TODO: recursive binary search\n    pass\n",
                    "tests": [
                        { "call": "locate_product([1, 4, 9, 16, 25, 36, 49], 36, 0, 6)", "expected": "5" },
                        { "call": "locate_product([1, 4, 9, 16, 25, 36, 49], 10, 0, 6)", "expected": "-1" },
                        { "call": "locate_product([100, 200], 100, 0, 1)", "expected": "0" }
                    ]
                }
            ]
        }
    ]
};
