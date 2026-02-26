"""
Tester for inOrderEqual - CodingBat Python
14 test cases
"""

from in_order_equal import in_order_equal


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = in_order_equal(2, 5, 11, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(2, 5, 11, False) expected True, got {result}")
        failed += 1

    # Test 2
    result = in_order_equal(5, 7, 6, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(5, 7, 6, False) expected False, got {result}")
        failed += 1

    # Test 3
    result = in_order_equal(5, 5, 7, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(5, 5, 7, True) expected True, got {result}")
        failed += 1

    # Test 4
    result = in_order_equal(5, 5, 7, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(5, 5, 7, False) expected False, got {result}")
        failed += 1

    # Test 5
    result = in_order_equal(2, 5, 4, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(2, 5, 4, False) expected False, got {result}")
        failed += 1

    # Test 6
    result = in_order_equal(3, 4, 3, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(3, 4, 3, False) expected False, got {result}")
        failed += 1

    # Test 7
    result = in_order_equal(3, 4, 4, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(3, 4, 4, False) expected False, got {result}")
        failed += 1

    # Test 8
    result = in_order_equal(3, 4, 3, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(3, 4, 3, True) expected False, got {result}")
        failed += 1

    # Test 9
    result = in_order_equal(3, 4, 4, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(3, 4, 4, True) expected True, got {result}")
        failed += 1

    # Test 10
    result = in_order_equal(1, 5, 5, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(1, 5, 5, True) expected True, got {result}")
        failed += 1

    # Test 11
    result = in_order_equal(5, 5, 5, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(5, 5, 5, True) expected True, got {result}")
        failed += 1

    # Test 12
    result = in_order_equal(2, 2, 1, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(2, 2, 1, True) expected False, got {result}")
        failed += 1

    # Test 13
    result = in_order_equal(9, 2, 2, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(9, 2, 2, True) expected False, got {result}")
        failed += 1

    # Test 14
    result = in_order_equal(0, 1, 0, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in_order_equal(0, 1, 0, True) expected False, got {result}")
        failed += 1

    print(f"in_order_equal: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
