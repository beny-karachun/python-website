"""
Tester for specialEleven - CodingBat Python
20 test cases
"""

from special_eleven import special_eleven


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = special_eleven(22)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(22) expected True, got {result}")
        failed += 1

    # Test 2
    result = special_eleven(23)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(23) expected True, got {result}")
        failed += 1

    # Test 3
    result = special_eleven(24)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(24) expected False, got {result}")
        failed += 1

    # Test 4
    result = special_eleven(21)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(21) expected False, got {result}")
        failed += 1

    # Test 5
    result = special_eleven(11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(11) expected True, got {result}")
        failed += 1

    # Test 6
    result = special_eleven(12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(12) expected True, got {result}")
        failed += 1

    # Test 7
    result = special_eleven(10)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(10) expected False, got {result}")
        failed += 1

    # Test 8
    result = special_eleven(9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(9) expected False, got {result}")
        failed += 1

    # Test 9
    result = special_eleven(8)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(8) expected False, got {result}")
        failed += 1

    # Test 10
    result = special_eleven(0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(0) expected True, got {result}")
        failed += 1

    # Test 11
    result = special_eleven(1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(1) expected True, got {result}")
        failed += 1

    # Test 12
    result = special_eleven(2)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(2) expected False, got {result}")
        failed += 1

    # Test 13
    result = special_eleven(121)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(121) expected True, got {result}")
        failed += 1

    # Test 14
    result = special_eleven(122)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(122) expected True, got {result}")
        failed += 1

    # Test 15
    result = special_eleven(123)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(123) expected False, got {result}")
        failed += 1

    # Test 16
    result = special_eleven(46)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(46) expected False, got {result}")
        failed += 1

    # Test 17
    result = special_eleven(49)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(49) expected False, got {result}")
        failed += 1

    # Test 18
    result = special_eleven(52)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(52) expected False, got {result}")
        failed += 1

    # Test 19
    result = special_eleven(54)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: special_eleven(54) expected False, got {result}")
        failed += 1

    # Test 20
    result = special_eleven(55)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: special_eleven(55) expected True, got {result}")
        failed += 1

    print(f"special_eleven: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
