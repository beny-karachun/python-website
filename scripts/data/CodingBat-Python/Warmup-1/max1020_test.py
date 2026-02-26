"""
Tester for max1020 - CodingBat Python
11 test cases
"""

from max1020 import max1020


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = max1020(11, 19)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: max1020(11, 19) expected 19, got {result}")
        failed += 1

    # Test 2
    result = max1020(19, 11)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: max1020(19, 11) expected 19, got {result}")
        failed += 1

    # Test 3
    result = max1020(11, 9)
    if result == 11:
        passed += 1
    else:
        print(f"FAIL: max1020(11, 9) expected 11, got {result}")
        failed += 1

    # Test 4
    result = max1020(9, 21)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: max1020(9, 21) expected 0, got {result}")
        failed += 1

    # Test 5
    result = max1020(10, 21)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: max1020(10, 21) expected 10, got {result}")
        failed += 1

    # Test 6
    result = max1020(21, 10)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: max1020(21, 10) expected 10, got {result}")
        failed += 1

    # Test 7
    result = max1020(9, 11)
    if result == 11:
        passed += 1
    else:
        print(f"FAIL: max1020(9, 11) expected 11, got {result}")
        failed += 1

    # Test 8
    result = max1020(23, 10)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: max1020(23, 10) expected 10, got {result}")
        failed += 1

    # Test 9
    result = max1020(20, 10)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: max1020(20, 10) expected 20, got {result}")
        failed += 1

    # Test 10
    result = max1020(7, 20)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: max1020(7, 20) expected 20, got {result}")
        failed += 1

    # Test 11
    result = max1020(17, 16)
    if result == 17:
        passed += 1
    else:
        print(f"FAIL: max1020(17, 16) expected 17, got {result}")
        failed += 1

    print(f"max1020: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
