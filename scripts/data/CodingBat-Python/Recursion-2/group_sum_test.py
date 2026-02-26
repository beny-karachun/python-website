"""
Tester for groupSum - CodingBat Python
3 test cases
"""

from group_sum import group_sum


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = group_sum(0, [2, 4, 8], 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_sum(0, [2, 4, 8], 10) expected True, got {result}")
        failed += 1

    # Test 2
    result = group_sum(0, [2, 4, 8], 14)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_sum(0, [2, 4, 8], 14) expected True, got {result}")
        failed += 1

    # Test 3
    result = group_sum(0, [2, 4, 8], 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: group_sum(0, [2, 4, 8], 9) expected False, got {result}")
        failed += 1

    print(f"group_sum: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
