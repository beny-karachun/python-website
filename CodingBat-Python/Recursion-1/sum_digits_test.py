"""
Tester for sumDigits - CodingBat Python
11 test cases
"""

from sum_digits import sum_digits


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = sum_digits(126)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: sum_digits(126) expected 9, got {result}")
        failed += 1

    # Test 2
    result = sum_digits(49)
    if result == 13:
        passed += 1
    else:
        print(f"FAIL: sum_digits(49) expected 13, got {result}")
        failed += 1

    # Test 3
    result = sum_digits(12)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: sum_digits(12) expected 3, got {result}")
        failed += 1

    # Test 4
    result = sum_digits(10)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: sum_digits(10) expected 1, got {result}")
        failed += 1

    # Test 5
    result = sum_digits(1)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: sum_digits(1) expected 1, got {result}")
        failed += 1

    # Test 6
    result = sum_digits(0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_digits(0) expected 0, got {result}")
        failed += 1

    # Test 7
    result = sum_digits(730)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: sum_digits(730) expected 10, got {result}")
        failed += 1

    # Test 8
    result = sum_digits(1111)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: sum_digits(1111) expected 4, got {result}")
        failed += 1

    # Test 9
    result = sum_digits(11111)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: sum_digits(11111) expected 5, got {result}")
        failed += 1

    # Test 10
    result = sum_digits(10110)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: sum_digits(10110) expected 3, got {result}")
        failed += 1

    # Test 11
    result = sum_digits(235)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: sum_digits(235) expected 10, got {result}")
        failed += 1

    print(f"sum_digits: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
