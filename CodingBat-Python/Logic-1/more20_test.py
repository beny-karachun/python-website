"""
Tester for more20 - CodingBat Python
21 test cases
"""

from more20 import more20


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = more20(20)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(20) expected False, got {result}")
        failed += 1

    # Test 2
    result = more20(21)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(21) expected True, got {result}")
        failed += 1

    # Test 3
    result = more20(22)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(22) expected True, got {result}")
        failed += 1

    # Test 4
    result = more20(23)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(23) expected False, got {result}")
        failed += 1

    # Test 5
    result = more20(25)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(25) expected False, got {result}")
        failed += 1

    # Test 6
    result = more20(30)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(30) expected False, got {result}")
        failed += 1

    # Test 7
    result = more20(31)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(31) expected False, got {result}")
        failed += 1

    # Test 8
    result = more20(59)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(59) expected False, got {result}")
        failed += 1

    # Test 9
    result = more20(60)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(60) expected False, got {result}")
        failed += 1

    # Test 10
    result = more20(61)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(61) expected True, got {result}")
        failed += 1

    # Test 11
    result = more20(62)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(62) expected True, got {result}")
        failed += 1

    # Test 12
    result = more20(1020)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(1020) expected False, got {result}")
        failed += 1

    # Test 13
    result = more20(1021)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(1021) expected True, got {result}")
        failed += 1

    # Test 14
    result = more20(1000)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(1000) expected False, got {result}")
        failed += 1

    # Test 15
    result = more20(1001)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(1001) expected True, got {result}")
        failed += 1

    # Test 16
    result = more20(50)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(50) expected False, got {result}")
        failed += 1

    # Test 17
    result = more20(55)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(55) expected False, got {result}")
        failed += 1

    # Test 18
    result = more20(40)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(40) expected False, got {result}")
        failed += 1

    # Test 19
    result = more20(41)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(41) expected True, got {result}")
        failed += 1

    # Test 20
    result = more20(39)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: more20(39) expected False, got {result}")
        failed += 1

    # Test 21
    result = more20(42)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: more20(42) expected True, got {result}")
        failed += 1

    print(f"more20: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
