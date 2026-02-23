"""
Tester for sumDouble - CodingBat Python
8 test cases
"""

from sum_double import sum_double


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = sum_double(1, 2)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: sum_double(1, 2) expected 3, got {result}")
        failed += 1

    # Test 2
    result = sum_double(3, 2)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: sum_double(3, 2) expected 5, got {result}")
        failed += 1

    # Test 3
    result = sum_double(2, 2)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: sum_double(2, 2) expected 8, got {result}")
        failed += 1

    # Test 4
    result = sum_double(-1, 0)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: sum_double(-1, 0) expected -1, got {result}")
        failed += 1

    # Test 5
    result = sum_double(3, 3)
    if result == 12:
        passed += 1
    else:
        print(f"FAIL: sum_double(3, 3) expected 12, got {result}")
        failed += 1

    # Test 6
    result = sum_double(0, 0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_double(0, 0) expected 0, got {result}")
        failed += 1

    # Test 7
    result = sum_double(0, 1)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: sum_double(0, 1) expected 1, got {result}")
        failed += 1

    # Test 8
    result = sum_double(3, 4)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: sum_double(3, 4) expected 7, got {result}")
        failed += 1

    print(f"sum_double: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
