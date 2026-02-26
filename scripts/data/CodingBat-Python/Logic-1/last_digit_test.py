"""
Tester for lastDigit - CodingBat Python
13 test cases
"""

from last_digit import last_digit


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = last_digit(23, 19, 13)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(23, 19, 13) expected True, got {result}")
        failed += 1

    # Test 2
    result = last_digit(23, 19, 12)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: last_digit(23, 19, 12) expected False, got {result}")
        failed += 1

    # Test 3
    result = last_digit(23, 19, 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(23, 19, 3) expected True, got {result}")
        failed += 1

    # Test 4
    result = last_digit(23, 19, 39)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(23, 19, 39) expected True, got {result}")
        failed += 1

    # Test 5
    result = last_digit(1, 2, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: last_digit(1, 2, 3) expected False, got {result}")
        failed += 1

    # Test 6
    result = last_digit(1, 1, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(1, 1, 2) expected True, got {result}")
        failed += 1

    # Test 7
    result = last_digit(1, 2, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(1, 2, 2) expected True, got {result}")
        failed += 1

    # Test 8
    result = last_digit(14, 25, 43)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: last_digit(14, 25, 43) expected False, got {result}")
        failed += 1

    # Test 9
    result = last_digit(14, 25, 45)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(14, 25, 45) expected True, got {result}")
        failed += 1

    # Test 10
    result = last_digit(248, 106, 1002)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: last_digit(248, 106, 1002) expected False, got {result}")
        failed += 1

    # Test 11
    result = last_digit(248, 106, 1008)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(248, 106, 1008) expected True, got {result}")
        failed += 1

    # Test 12
    result = last_digit(10, 11, 20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(10, 11, 20) expected True, got {result}")
        failed += 1

    # Test 13
    result = last_digit(0, 11, 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: last_digit(0, 11, 0) expected True, got {result}")
        failed += 1

    print(f"last_digit: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
