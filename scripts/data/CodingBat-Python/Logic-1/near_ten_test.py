"""
Tester for nearTen - CodingBat Python
15 test cases
"""

from near_ten import near_ten


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = near_ten(12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(12) expected True, got {result}")
        failed += 1

    # Test 2
    result = near_ten(17)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_ten(17) expected False, got {result}")
        failed += 1

    # Test 3
    result = near_ten(19)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(19) expected True, got {result}")
        failed += 1

    # Test 4
    result = near_ten(31)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(31) expected True, got {result}")
        failed += 1

    # Test 5
    result = near_ten(6)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_ten(6) expected False, got {result}")
        failed += 1

    # Test 6
    result = near_ten(10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(10) expected True, got {result}")
        failed += 1

    # Test 7
    result = near_ten(11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(11) expected True, got {result}")
        failed += 1

    # Test 8
    result = near_ten(21)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(21) expected True, got {result}")
        failed += 1

    # Test 9
    result = near_ten(22)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(22) expected True, got {result}")
        failed += 1

    # Test 10
    result = near_ten(23)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_ten(23) expected False, got {result}")
        failed += 1

    # Test 11
    result = near_ten(54)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_ten(54) expected False, got {result}")
        failed += 1

    # Test 12
    result = near_ten(155)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_ten(155) expected False, got {result}")
        failed += 1

    # Test 13
    result = near_ten(158)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(158) expected True, got {result}")
        failed += 1

    # Test 14
    result = near_ten(3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_ten(3) expected False, got {result}")
        failed += 1

    # Test 15
    result = near_ten(1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_ten(1) expected True, got {result}")
        failed += 1

    print(f"near_ten: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
