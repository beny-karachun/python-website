"""
Tester for love6 - CodingBat Python
20 test cases
"""

from love6 import love6


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = love6(6, 4)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(6, 4) expected True, got {result}")
        failed += 1

    # Test 2
    result = love6(4, 5)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(4, 5) expected False, got {result}")
        failed += 1

    # Test 3
    result = love6(1, 5)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(1, 5) expected True, got {result}")
        failed += 1

    # Test 4
    result = love6(1, 6)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(1, 6) expected True, got {result}")
        failed += 1

    # Test 5
    result = love6(1, 8)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(1, 8) expected False, got {result}")
        failed += 1

    # Test 6
    result = love6(1, 7)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(1, 7) expected True, got {result}")
        failed += 1

    # Test 7
    result = love6(7, 5)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(7, 5) expected False, got {result}")
        failed += 1

    # Test 8
    result = love6(8, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(8, 2) expected True, got {result}")
        failed += 1

    # Test 9
    result = love6(6, 6)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(6, 6) expected True, got {result}")
        failed += 1

    # Test 10
    result = love6(-6, 2)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(-6, 2) expected False, got {result}")
        failed += 1

    # Test 11
    result = love6(-4, -10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(-4, -10) expected True, got {result}")
        failed += 1

    # Test 12
    result = love6(-7, 1)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(-7, 1) expected False, got {result}")
        failed += 1

    # Test 13
    result = love6(7, -1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(7, -1) expected True, got {result}")
        failed += 1

    # Test 14
    result = love6(-6, 12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(-6, 12) expected True, got {result}")
        failed += 1

    # Test 15
    result = love6(-2, -4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(-2, -4) expected False, got {result}")
        failed += 1

    # Test 16
    result = love6(7, 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(7, 1) expected True, got {result}")
        failed += 1

    # Test 17
    result = love6(0, 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(0, 9) expected False, got {result}")
        failed += 1

    # Test 18
    result = love6(8, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(8, 3) expected False, got {result}")
        failed += 1

    # Test 19
    result = love6(3, 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: love6(3, 3) expected True, got {result}")
        failed += 1

    # Test 20
    result = love6(3, 4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: love6(3, 4) expected False, got {result}")
        failed += 1

    print(f"love6: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
