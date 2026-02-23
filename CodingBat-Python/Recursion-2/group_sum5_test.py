"""
Tester for groupSum5 - CodingBat Python
3 test cases
"""

from group_sum5 import group_sum5


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = group_sum5(0, [2, 5, 10, 4], 19)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_sum5(0, [2, 5, 10, 4], 19) expected True, got {result}")
        failed += 1

    # Test 2
    result = group_sum5(0, [2, 5, 10, 4], 17)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_sum5(0, [2, 5, 10, 4], 17) expected True, got {result}")
        failed += 1

    # Test 3
    result = group_sum5(0, [2, 5, 10, 4], 12)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: group_sum5(0, [2, 5, 10, 4], 12) expected False, got {result}")
        failed += 1

    print(f"group_sum5: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
