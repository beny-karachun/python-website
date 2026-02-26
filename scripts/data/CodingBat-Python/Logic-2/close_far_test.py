"""
Tester for closeFar - CodingBat Python
12 test cases
"""

from close_far import close_far


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = close_far(1, 2, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: close_far(1, 2, 10) expected True, got {result}")
        failed += 1

    # Test 2
    result = close_far(1, 2, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: close_far(1, 2, 3) expected False, got {result}")
        failed += 1

    # Test 3
    result = close_far(4, 1, 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: close_far(4, 1, 3) expected True, got {result}")
        failed += 1

    # Test 4
    result = close_far(4, 5, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: close_far(4, 5, 3) expected False, got {result}")
        failed += 1

    # Test 5
    result = close_far(4, 3, 5)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: close_far(4, 3, 5) expected False, got {result}")
        failed += 1

    # Test 6
    result = close_far(-1, 10, 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: close_far(-1, 10, 0) expected True, got {result}")
        failed += 1

    # Test 7
    result = close_far(0, -1, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: close_far(0, -1, 10) expected True, got {result}")
        failed += 1

    # Test 8
    result = close_far(10, 10, 8)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: close_far(10, 10, 8) expected True, got {result}")
        failed += 1

    # Test 9
    result = close_far(10, 8, 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: close_far(10, 8, 9) expected False, got {result}")
        failed += 1

    # Test 10
    result = close_far(8, 9, 10)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: close_far(8, 9, 10) expected False, got {result}")
        failed += 1

    # Test 11
    result = close_far(8, 9, 7)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: close_far(8, 9, 7) expected False, got {result}")
        failed += 1

    # Test 12
    result = close_far(8, 6, 9)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: close_far(8, 6, 9) expected True, got {result}")
        failed += 1

    print(f"close_far: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
