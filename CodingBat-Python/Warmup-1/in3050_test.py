"""
Tester for in3050 - CodingBat Python
12 test cases
"""

from in3050 import in3050


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = in3050(30, 31)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in3050(30, 31) expected True, got {result}")
        failed += 1

    # Test 2
    result = in3050(30, 41)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in3050(30, 41) expected False, got {result}")
        failed += 1

    # Test 3
    result = in3050(40, 50)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in3050(40, 50) expected True, got {result}")
        failed += 1

    # Test 4
    result = in3050(40, 51)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in3050(40, 51) expected False, got {result}")
        failed += 1

    # Test 5
    result = in3050(39, 50)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in3050(39, 50) expected False, got {result}")
        failed += 1

    # Test 6
    result = in3050(50, 39)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in3050(50, 39) expected False, got {result}")
        failed += 1

    # Test 7
    result = in3050(40, 39)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in3050(40, 39) expected True, got {result}")
        failed += 1

    # Test 8
    result = in3050(49, 48)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in3050(49, 48) expected True, got {result}")
        failed += 1

    # Test 9
    result = in3050(50, 40)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in3050(50, 40) expected True, got {result}")
        failed += 1

    # Test 10
    result = in3050(50, 51)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in3050(50, 51) expected False, got {result}")
        failed += 1

    # Test 11
    result = in3050(35, 36)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in3050(35, 36) expected True, got {result}")
        failed += 1

    # Test 12
    result = in3050(35, 45)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in3050(35, 45) expected False, got {result}")
        failed += 1

    print(f"in3050: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
