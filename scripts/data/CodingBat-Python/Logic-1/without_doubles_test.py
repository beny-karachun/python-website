"""
Tester for withoutDoubles - CodingBat Python
12 test cases
"""

from without_doubles import without_doubles


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = without_doubles(2, 3, True)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: without_doubles(2, 3, True) expected 5, got {result}")
        failed += 1

    # Test 2
    result = without_doubles(3, 3, True)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: without_doubles(3, 3, True) expected 7, got {result}")
        failed += 1

    # Test 3
    result = without_doubles(3, 3, False)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: without_doubles(3, 3, False) expected 6, got {result}")
        failed += 1

    # Test 4
    result = without_doubles(2, 3, False)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: without_doubles(2, 3, False) expected 5, got {result}")
        failed += 1

    # Test 5
    result = without_doubles(5, 4, True)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: without_doubles(5, 4, True) expected 9, got {result}")
        failed += 1

    # Test 6
    result = without_doubles(5, 4, False)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: without_doubles(5, 4, False) expected 9, got {result}")
        failed += 1

    # Test 7
    result = without_doubles(5, 5, True)
    if result == 11:
        passed += 1
    else:
        print(f"FAIL: without_doubles(5, 5, True) expected 11, got {result}")
        failed += 1

    # Test 8
    result = without_doubles(5, 5, False)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: without_doubles(5, 5, False) expected 10, got {result}")
        failed += 1

    # Test 9
    result = without_doubles(6, 6, True)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: without_doubles(6, 6, True) expected 7, got {result}")
        failed += 1

    # Test 10
    result = without_doubles(6, 6, False)
    if result == 12:
        passed += 1
    else:
        print(f"FAIL: without_doubles(6, 6, False) expected 12, got {result}")
        failed += 1

    # Test 11
    result = without_doubles(1, 6, True)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: without_doubles(1, 6, True) expected 7, got {result}")
        failed += 1

    # Test 12
    result = without_doubles(6, 1, False)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: without_doubles(6, 1, False) expected 7, got {result}")
        failed += 1

    print(f"without_doubles: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
