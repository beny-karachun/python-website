"""
Tester for groupNoAdj - CodingBat Python
3 test cases
"""

from group_no_adj import group_no_adj


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = group_no_adj(0, [2, 5, 10, 4], 12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: group_no_adj(0, [2, 5, 10, 4], 12) expected True, got {result}")
        failed += 1

    # Test 2
    result = group_no_adj(0, [2, 5, 10, 4], 14)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: group_no_adj(0, [2, 5, 10, 4], 14) expected False, got {result}")
        failed += 1

    # Test 3
    result = group_no_adj(0, [2, 5, 10, 4], 7)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: group_no_adj(0, [2, 5, 10, 4], 7) expected False, got {result}")
        failed += 1

    print(f"group_no_adj: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
