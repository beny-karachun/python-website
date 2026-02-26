"""
Tester for lessBy10 - CodingBat Python
14 test cases
"""

from less_by10 import less_by10


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = less_by10(1, 7, 11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(1, 7, 11) expected True, got {result}")
        failed += 1

    # Test 2
    result = less_by10(1, 7, 10)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less_by10(1, 7, 10) expected False, got {result}")
        failed += 1

    # Test 3
    result = less_by10(11, 1, 7)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(11, 1, 7) expected True, got {result}")
        failed += 1

    # Test 4
    result = less_by10(10, 7, 1)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less_by10(10, 7, 1) expected False, got {result}")
        failed += 1

    # Test 5
    result = less_by10(-10, 2, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(-10, 2, 2) expected True, got {result}")
        failed += 1

    # Test 6
    result = less_by10(2, 11, 11)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less_by10(2, 11, 11) expected False, got {result}")
        failed += 1

    # Test 7
    result = less_by10(3, 3, 30)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(3, 3, 30) expected True, got {result}")
        failed += 1

    # Test 8
    result = less_by10(3, 3, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less_by10(3, 3, 3) expected False, got {result}")
        failed += 1

    # Test 9
    result = less_by10(10, 1, 11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(10, 1, 11) expected True, got {result}")
        failed += 1

    # Test 10
    result = less_by10(10, 11, 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(10, 11, 1) expected True, got {result}")
        failed += 1

    # Test 11
    result = less_by10(10, 11, 2)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: less_by10(10, 11, 2) expected False, got {result}")
        failed += 1

    # Test 12
    result = less_by10(3, 30, 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(3, 30, 3) expected True, got {result}")
        failed += 1

    # Test 13
    result = less_by10(2, 2, -8)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(2, 2, -8) expected True, got {result}")
        failed += 1

    # Test 14
    result = less_by10(2, 8, 12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: less_by10(2, 8, 12) expected True, got {result}")
        failed += 1

    print(f"less_by10: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
