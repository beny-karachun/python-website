"""
Tester for groupSumClump - CodingBat Python
3 test cases
"""

from group_sum_clump import group_sum_clump


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = group_sum_clump(0, [2, 4, 8], 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_sum_clump(0, [2, 4, 8], 10) expected True, got {result}")
        failed += 1

    # Test 2
    result = group_sum_clump(0, [1, 2, 4, 8, 1], 14)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_sum_clump(0, [1, 2, 4, 8, 1], 14) expected True, got {result}")
        failed += 1

    # Test 3
    result = group_sum_clump(0, [2, 4, 4, 8], 14)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: group_sum_clump(0, [2, 4, 4, 8], 14) expected False, got {result}")
        failed += 1

    print(f"group_sum_clump: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
