"""
Tester for or35 - CodingBat Python
22 test cases
"""

from or35 import or35


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = or35(3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(3) expected True, got {result}")
        failed += 1

    # Test 2
    result = or35(10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(10) expected True, got {result}")
        failed += 1

    # Test 3
    result = or35(8)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(8) expected False, got {result}")
        failed += 1

    # Test 4
    result = or35(15)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(15) expected True, got {result}")
        failed += 1

    # Test 5
    result = or35(5)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(5) expected True, got {result}")
        failed += 1

    # Test 6
    result = or35(9)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(9) expected True, got {result}")
        failed += 1

    # Test 7
    result = or35(4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(4) expected False, got {result}")
        failed += 1

    # Test 8
    result = or35(7)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(7) expected False, got {result}")
        failed += 1

    # Test 9
    result = or35(6)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(6) expected True, got {result}")
        failed += 1

    # Test 10
    result = or35(17)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(17) expected False, got {result}")
        failed += 1

    # Test 11
    result = or35(18)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(18) expected True, got {result}")
        failed += 1

    # Test 12
    result = or35(29)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(29) expected False, got {result}")
        failed += 1

    # Test 13
    result = or35(20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(20) expected True, got {result}")
        failed += 1

    # Test 14
    result = or35(21)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(21) expected True, got {result}")
        failed += 1

    # Test 15
    result = or35(22)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(22) expected False, got {result}")
        failed += 1

    # Test 16
    result = or35(45)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(45) expected True, got {result}")
        failed += 1

    # Test 17
    result = or35(99)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(99) expected True, got {result}")
        failed += 1

    # Test 18
    result = or35(100)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(100) expected True, got {result}")
        failed += 1

    # Test 19
    result = or35(101)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(101) expected False, got {result}")
        failed += 1

    # Test 20
    result = or35(121)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(121) expected False, got {result}")
        failed += 1

    # Test 21
    result = or35(122)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: or35(122) expected False, got {result}")
        failed += 1

    # Test 22
    result = or35(123)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: or35(123) expected True, got {result}")
        failed += 1

    print(f"or35: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
