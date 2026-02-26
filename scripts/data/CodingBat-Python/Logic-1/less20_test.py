"""
Tester for less20 - CodingBat Python
22 test cases
"""

from less20 import less20


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = less20(18)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less20(18) expected True, got {result}")
        failed += 1

    # Test 2
    result = less20(19)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less20(19) expected True, got {result}")
        failed += 1

    # Test 3
    result = less20(20)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(20) expected False, got {result}")
        failed += 1

    # Test 4
    result = less20(8)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(8) expected False, got {result}")
        failed += 1

    # Test 5
    result = less20(17)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(17) expected False, got {result}")
        failed += 1

    # Test 6
    result = less20(23)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(23) expected False, got {result}")
        failed += 1

    # Test 7
    result = less20(25)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(25) expected False, got {result}")
        failed += 1

    # Test 8
    result = less20(30)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(30) expected False, got {result}")
        failed += 1

    # Test 9
    result = less20(31)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(31) expected False, got {result}")
        failed += 1

    # Test 10
    result = less20(58)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less20(58) expected True, got {result}")
        failed += 1

    # Test 11
    result = less20(59)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less20(59) expected True, got {result}")
        failed += 1

    # Test 12
    result = less20(60)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(60) expected False, got {result}")
        failed += 1

    # Test 13
    result = less20(61)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(61) expected False, got {result}")
        failed += 1

    # Test 14
    result = less20(62)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(62) expected False, got {result}")
        failed += 1

    # Test 15
    result = less20(1017)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(1017) expected False, got {result}")
        failed += 1

    # Test 16
    result = less20(1018)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less20(1018) expected True, got {result}")
        failed += 1

    # Test 17
    result = less20(1019)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less20(1019) expected True, got {result}")
        failed += 1

    # Test 18
    result = less20(1020)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(1020) expected False, got {result}")
        failed += 1

    # Test 19
    result = less20(1021)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(1021) expected False, got {result}")
        failed += 1

    # Test 20
    result = less20(1022)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(1022) expected False, got {result}")
        failed += 1

    # Test 21
    result = less20(1023)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(1023) expected False, got {result}")
        failed += 1

    # Test 22
    result = less20(37)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less20(37) expected False, got {result}")
        failed += 1

    print(f"less20: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
