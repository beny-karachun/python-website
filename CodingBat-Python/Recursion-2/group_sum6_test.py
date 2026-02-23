"""
Tester for groupSum6 - CodingBat Python
3 test cases
"""

from group_sum6 import group_sum6


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = group_sum6(0, [5, 6, 2], 8)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_sum6(0, [5, 6, 2], 8) expected True, got {result}")
        failed += 1

    # Test 2
    result = group_sum6(0, [5, 6, 2], 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: group_sum6(0, [5, 6, 2], 9) expected False, got {result}")
        failed += 1

    # Test 3
    result = group_sum6(0, [5, 6, 2], 7)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: group_sum6(0, [5, 6, 2], 7) expected False, got {result}")
        failed += 1

    print(f"group_sum6: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
