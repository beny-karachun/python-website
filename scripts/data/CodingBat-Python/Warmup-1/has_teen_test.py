"""
Tester for hasTeen - CodingBat Python
11 test cases
"""

from has_teen import has_teen


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = has_teen(13, 20, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_teen(13, 20, 10) expected True, got {result}")
        failed += 1

    # Test 2
    result = has_teen(20, 19, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_teen(20, 19, 10) expected True, got {result}")
        failed += 1

    # Test 3
    result = has_teen(20, 10, 13)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_teen(20, 10, 13) expected True, got {result}")
        failed += 1

    # Test 4
    result = has_teen(1, 20, 12)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_teen(1, 20, 12) expected False, got {result}")
        failed += 1

    # Test 5
    result = has_teen(19, 20, 12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_teen(19, 20, 12) expected True, got {result}")
        failed += 1

    # Test 6
    result = has_teen(12, 20, 19)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_teen(12, 20, 19) expected True, got {result}")
        failed += 1

    # Test 7
    result = has_teen(12, 9, 20)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_teen(12, 9, 20) expected False, got {result}")
        failed += 1

    # Test 8
    result = has_teen(12, 18, 20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_teen(12, 18, 20) expected True, got {result}")
        failed += 1

    # Test 9
    result = has_teen(14, 2, 20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_teen(14, 2, 20) expected True, got {result}")
        failed += 1

    # Test 10
    result = has_teen(4, 2, 20)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_teen(4, 2, 20) expected False, got {result}")
        failed += 1

    # Test 11
    result = has_teen(11, 22, 22)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_teen(11, 22, 22) expected False, got {result}")
        failed += 1

    print(f"has_teen: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
