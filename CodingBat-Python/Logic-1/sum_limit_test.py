"""
Tester for sumLimit - CodingBat Python
15 test cases
"""

from sum_limit import sum_limit


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = sum_limit(2, 3)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: sum_limit(2, 3) expected 5, got {result}")
        failed += 1

    # Test 2
    result = sum_limit(8, 3)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: sum_limit(8, 3) expected 8, got {result}")
        failed += 1

    # Test 3
    result = sum_limit(8, 1)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: sum_limit(8, 1) expected 9, got {result}")
        failed += 1

    # Test 4
    result = sum_limit(11, 39)
    if result == 50:
        passed += 1
    else:
        print(f"FAIL: sum_limit(11, 39) expected 50, got {result}")
        failed += 1

    # Test 5
    result = sum_limit(11, 99)
    if result == 11:
        passed += 1
    else:
        print(f"FAIL: sum_limit(11, 99) expected 11, got {result}")
        failed += 1

    # Test 6
    result = sum_limit(0, 0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_limit(0, 0) expected 0, got {result}")
        failed += 1

    # Test 7
    result = sum_limit(99, 0)
    if result == 99:
        passed += 1
    else:
        print(f"FAIL: sum_limit(99, 0) expected 99, got {result}")
        failed += 1

    # Test 8
    result = sum_limit(99, 1)
    if result == 99:
        passed += 1
    else:
        print(f"FAIL: sum_limit(99, 1) expected 99, got {result}")
        failed += 1

    # Test 9
    result = sum_limit(123, 1)
    if result == 124:
        passed += 1
    else:
        print(f"FAIL: sum_limit(123, 1) expected 124, got {result}")
        failed += 1

    # Test 10
    result = sum_limit(1, 123)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: sum_limit(1, 123) expected 1, got {result}")
        failed += 1

    # Test 11
    result = sum_limit(23, 60)
    if result == 83:
        passed += 1
    else:
        print(f"FAIL: sum_limit(23, 60) expected 83, got {result}")
        failed += 1

    # Test 12
    result = sum_limit(23, 80)
    if result == 23:
        passed += 1
    else:
        print(f"FAIL: sum_limit(23, 80) expected 23, got {result}")
        failed += 1

    # Test 13
    result = sum_limit(9000, 1)
    if result == 9001:
        passed += 1
    else:
        print(f"FAIL: sum_limit(9000, 1) expected 9001, got {result}")
        failed += 1

    # Test 14
    result = sum_limit(90000000, 1)
    if result == 90000001:
        passed += 1
    else:
        print(f"FAIL: sum_limit(90000000, 1) expected 90000001, got {result}")
        failed += 1

    # Test 15
    result = sum_limit(9000, 1000)
    if result == 9000:
        passed += 1
    else:
        print(f"FAIL: sum_limit(9000, 1000) expected 9000, got {result}")
        failed += 1

    print(f"sum_limit: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
