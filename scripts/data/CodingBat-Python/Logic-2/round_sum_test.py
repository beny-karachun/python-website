"""
Tester for roundSum - CodingBat Python
19 test cases
"""

from round_sum import round_sum


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = round_sum(16, 17, 18)
    if result == 60:
        passed += 1
    else:
        print(f"FAIL: round_sum(16, 17, 18) expected 60, got {result}")
        failed += 1

    # Test 2
    result = round_sum(12, 13, 14)
    if result == 30:
        passed += 1
    else:
        print(f"FAIL: round_sum(12, 13, 14) expected 30, got {result}")
        failed += 1

    # Test 3
    result = round_sum(6, 4, 4)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: round_sum(6, 4, 4) expected 10, got {result}")
        failed += 1

    # Test 4
    result = round_sum(4, 6, 5)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: round_sum(4, 6, 5) expected 20, got {result}")
        failed += 1

    # Test 5
    result = round_sum(4, 4, 6)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: round_sum(4, 4, 6) expected 10, got {result}")
        failed += 1

    # Test 6
    result = round_sum(9, 4, 4)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: round_sum(9, 4, 4) expected 10, got {result}")
        failed += 1

    # Test 7
    result = round_sum(0, 0, 1)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: round_sum(0, 0, 1) expected 0, got {result}")
        failed += 1

    # Test 8
    result = round_sum(0, 9, 0)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: round_sum(0, 9, 0) expected 10, got {result}")
        failed += 1

    # Test 9
    result = round_sum(10, 10, 19)
    if result == 40:
        passed += 1
    else:
        print(f"FAIL: round_sum(10, 10, 19) expected 40, got {result}")
        failed += 1

    # Test 10
    result = round_sum(20, 30, 40)
    if result == 90:
        passed += 1
    else:
        print(f"FAIL: round_sum(20, 30, 40) expected 90, got {result}")
        failed += 1

    # Test 11
    result = round_sum(45, 21, 30)
    if result == 100:
        passed += 1
    else:
        print(f"FAIL: round_sum(45, 21, 30) expected 100, got {result}")
        failed += 1

    # Test 12
    result = round_sum(23, 11, 26)
    if result == 60:
        passed += 1
    else:
        print(f"FAIL: round_sum(23, 11, 26) expected 60, got {result}")
        failed += 1

    # Test 13
    result = round_sum(23, 24, 25)
    if result == 70:
        passed += 1
    else:
        print(f"FAIL: round_sum(23, 24, 25) expected 70, got {result}")
        failed += 1

    # Test 14
    result = round_sum(25, 24, 25)
    if result == 80:
        passed += 1
    else:
        print(f"FAIL: round_sum(25, 24, 25) expected 80, got {result}")
        failed += 1

    # Test 15
    result = round_sum(23, 24, 29)
    if result == 70:
        passed += 1
    else:
        print(f"FAIL: round_sum(23, 24, 29) expected 70, got {result}")
        failed += 1

    # Test 16
    result = round_sum(11, 24, 36)
    if result == 70:
        passed += 1
    else:
        print(f"FAIL: round_sum(11, 24, 36) expected 70, got {result}")
        failed += 1

    # Test 17
    result = round_sum(24, 36, 32)
    if result == 90:
        passed += 1
    else:
        print(f"FAIL: round_sum(24, 36, 32) expected 90, got {result}")
        failed += 1

    # Test 18
    result = round_sum(14, 12, 26)
    if result == 50:
        passed += 1
    else:
        print(f"FAIL: round_sum(14, 12, 26) expected 50, got {result}")
        failed += 1

    # Test 19
    result = round_sum(12, 10, 24)
    if result == 40:
        passed += 1
    else:
        print(f"FAIL: round_sum(12, 10, 24) expected 40, got {result}")
        failed += 1

    print(f"round_sum: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
