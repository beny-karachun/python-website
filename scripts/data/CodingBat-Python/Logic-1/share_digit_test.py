"""
Tester for shareDigit - CodingBat Python
10 test cases
"""

from share_digit import share_digit


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = share_digit(12, 23)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: share_digit(12, 23) expected True, got {result}")
        failed += 1

    # Test 2
    result = share_digit(12, 43)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: share_digit(12, 43) expected False, got {result}")
        failed += 1

    # Test 3
    result = share_digit(12, 44)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: share_digit(12, 44) expected False, got {result}")
        failed += 1

    # Test 4
    result = share_digit(23, 12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: share_digit(23, 12) expected True, got {result}")
        failed += 1

    # Test 5
    result = share_digit(23, 39)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: share_digit(23, 39) expected True, got {result}")
        failed += 1

    # Test 6
    result = share_digit(23, 19)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: share_digit(23, 19) expected False, got {result}")
        failed += 1

    # Test 7
    result = share_digit(30, 90)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: share_digit(30, 90) expected True, got {result}")
        failed += 1

    # Test 8
    result = share_digit(30, 91)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: share_digit(30, 91) expected False, got {result}")
        failed += 1

    # Test 9
    result = share_digit(55, 55)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: share_digit(55, 55) expected True, got {result}")
        failed += 1

    # Test 10
    result = share_digit(55, 44)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: share_digit(55, 44) expected False, got {result}")
        failed += 1

    print(f"share_digit: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
