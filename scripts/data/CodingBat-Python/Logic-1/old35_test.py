"""
Tester for old35 - CodingBat Python
16 test cases
"""

from old35 import old35


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = old35(3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(3) expected True, got {result}")
        failed += 1

    # Test 2
    result = old35(10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(10) expected True, got {result}")
        failed += 1

    # Test 3
    result = old35(15)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: old35(15) expected False, got {result}")
        failed += 1

    # Test 4
    result = old35(5)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(5) expected True, got {result}")
        failed += 1

    # Test 5
    result = old35(9)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(9) expected True, got {result}")
        failed += 1

    # Test 6
    result = old35(8)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: old35(8) expected False, got {result}")
        failed += 1

    # Test 7
    result = old35(7)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: old35(7) expected False, got {result}")
        failed += 1

    # Test 8
    result = old35(6)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(6) expected True, got {result}")
        failed += 1

    # Test 9
    result = old35(17)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: old35(17) expected False, got {result}")
        failed += 1

    # Test 10
    result = old35(18)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(18) expected True, got {result}")
        failed += 1

    # Test 11
    result = old35(29)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: old35(29) expected False, got {result}")
        failed += 1

    # Test 12
    result = old35(20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(20) expected True, got {result}")
        failed += 1

    # Test 13
    result = old35(21)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(21) expected True, got {result}")
        failed += 1

    # Test 14
    result = old35(22)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: old35(22) expected False, got {result}")
        failed += 1

    # Test 15
    result = old35(45)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: old35(45) expected False, got {result}")
        failed += 1

    # Test 16
    result = old35(99)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: old35(99) expected True, got {result}")
        failed += 1

    print(f"old35: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
