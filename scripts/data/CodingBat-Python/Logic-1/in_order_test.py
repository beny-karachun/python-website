"""
Tester for inOrder - CodingBat Python
12 test cases
"""

from in_order import in_order


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = in_order(1, 2, 4, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order(1, 2, 4, False) expected True, got {result}")
        failed += 1

    # Test 2
    result = in_order(1, 2, 1, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order(1, 2, 1, False) expected False, got {result}")
        failed += 1

    # Test 3
    result = in_order(1, 1, 2, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order(1, 1, 2, True) expected True, got {result}")
        failed += 1

    # Test 4
    result = in_order(3, 2, 4, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order(3, 2, 4, False) expected False, got {result}")
        failed += 1

    # Test 5
    result = in_order(2, 3, 4, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order(2, 3, 4, False) expected True, got {result}")
        failed += 1

    # Test 6
    result = in_order(3, 2, 4, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order(3, 2, 4, True) expected True, got {result}")
        failed += 1

    # Test 7
    result = in_order(4, 2, 2, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order(4, 2, 2, True) expected False, got {result}")
        failed += 1

    # Test 8
    result = in_order(4, 5, 2, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order(4, 5, 2, True) expected False, got {result}")
        failed += 1

    # Test 9
    result = in_order(2, 4, 6, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order(2, 4, 6, True) expected True, got {result}")
        failed += 1

    # Test 10
    result = in_order(7, 9, 10, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order(7, 9, 10, False) expected True, got {result}")
        failed += 1

    # Test 11
    result = in_order(7, 5, 6, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order(7, 5, 6, True) expected True, got {result}")
        failed += 1

    # Test 12
    result = in_order(7, 5, 4, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order(7, 5, 4, True) expected False, got {result}")
        failed += 1

    print(f"in_order: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
