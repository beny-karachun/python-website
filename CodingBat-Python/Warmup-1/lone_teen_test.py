"""
Tester for loneTeen - CodingBat Python
13 test cases
"""

from lone_teen import lone_teen


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = lone_teen(13, 99)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(13, 99) expected True, got {result}")
        failed += 1

    # Test 2
    result = lone_teen(21, 19)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(21, 19) expected True, got {result}")
        failed += 1

    # Test 3
    result = lone_teen(13, 13)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: lone_teen(13, 13) expected False, got {result}")
        failed += 1

    # Test 4
    result = lone_teen(14, 20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(14, 20) expected True, got {result}")
        failed += 1

    # Test 5
    result = lone_teen(20, 15)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(20, 15) expected True, got {result}")
        failed += 1

    # Test 6
    result = lone_teen(16, 17)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: lone_teen(16, 17) expected False, got {result}")
        failed += 1

    # Test 7
    result = lone_teen(16, 9)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(16, 9) expected True, got {result}")
        failed += 1

    # Test 8
    result = lone_teen(16, 18)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: lone_teen(16, 18) expected False, got {result}")
        failed += 1

    # Test 9
    result = lone_teen(13, 19)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: lone_teen(13, 19) expected False, got {result}")
        failed += 1

    # Test 10
    result = lone_teen(13, 20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(13, 20) expected True, got {result}")
        failed += 1

    # Test 11
    result = lone_teen(6, 18)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(6, 18) expected True, got {result}")
        failed += 1

    # Test 12
    result = lone_teen(99, 13)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: lone_teen(99, 13) expected True, got {result}")
        failed += 1

    # Test 13
    result = lone_teen(99, 99)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: lone_teen(99, 99) expected False, got {result}")
        failed += 1

    print(f"lone_teen: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
