"""
Tester for lastDigit - CodingBat Python
7 test cases
"""

from last_digit import last_digit


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = last_digit(7, 17)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(7, 17) expected True, got {result}")
        failed += 1

    # Test 2
    result = last_digit(6, 17)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: last_digit(6, 17) expected False, got {result}")
        failed += 1

    # Test 3
    result = last_digit(3, 113)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(3, 113) expected True, got {result}")
        failed += 1

    # Test 4
    result = last_digit(114, 113)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: last_digit(114, 113) expected False, got {result}")
        failed += 1

    # Test 5
    result = last_digit(114, 4)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(114, 4) expected True, got {result}")
        failed += 1

    # Test 6
    result = last_digit(10, 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(10, 0) expected True, got {result}")
        failed += 1

    # Test 7
    result = last_digit(11, 0)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: last_digit(11, 0) expected False, got {result}")
        failed += 1

    print(f"last_digit: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
