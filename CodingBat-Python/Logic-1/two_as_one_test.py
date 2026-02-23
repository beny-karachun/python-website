"""
Tester for twoAsOne - CodingBat Python
12 test cases
"""

from two_as_one import two_as_one


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = two_as_one(1, 2, 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(1, 2, 3) expected True, got {result}")
        failed += 1

    # Test 2
    result = two_as_one(3, 1, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(3, 1, 2) expected True, got {result}")
        failed += 1

    # Test 3
    result = two_as_one(3, 2, 2)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: two_as_one(3, 2, 2) expected False, got {result}")
        failed += 1

    # Test 4
    result = two_as_one(2, 3, 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(2, 3, 1) expected True, got {result}")
        failed += 1

    # Test 5
    result = two_as_one(5, 3, -2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(5, 3, -2) expected True, got {result}")
        failed += 1

    # Test 6
    result = two_as_one(5, 3, -3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: two_as_one(5, 3, -3) expected False, got {result}")
        failed += 1

    # Test 7
    result = two_as_one(2, 5, 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(2, 5, 3) expected True, got {result}")
        failed += 1

    # Test 8
    result = two_as_one(9, 5, 5)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: two_as_one(9, 5, 5) expected False, got {result}")
        failed += 1

    # Test 9
    result = two_as_one(9, 4, 5)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(9, 4, 5) expected True, got {result}")
        failed += 1

    # Test 10
    result = two_as_one(5, 4, 9)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(5, 4, 9) expected True, got {result}")
        failed += 1

    # Test 11
    result = two_as_one(3, 3, 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: two_as_one(3, 3, 0) expected True, got {result}")
        failed += 1

    # Test 12
    result = two_as_one(3, 3, 2)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: two_as_one(3, 3, 2) expected False, got {result}")
        failed += 1

    print(f"two_as_one: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
