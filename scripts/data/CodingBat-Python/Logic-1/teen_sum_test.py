"""
Tester for teenSum - CodingBat Python
16 test cases
"""

from teen_sum import teen_sum


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = teen_sum(3, 4)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: teen_sum(3, 4) expected 7, got {result}")
        failed += 1

    # Test 2
    result = teen_sum(10, 13)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(10, 13) expected 19, got {result}")
        failed += 1

    # Test 3
    result = teen_sum(13, 2)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(13, 2) expected 19, got {result}")
        failed += 1

    # Test 4
    result = teen_sum(3, 19)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(3, 19) expected 19, got {result}")
        failed += 1

    # Test 5
    result = teen_sum(13, 13)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(13, 13) expected 19, got {result}")
        failed += 1

    # Test 6
    result = teen_sum(10, 10)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: teen_sum(10, 10) expected 20, got {result}")
        failed += 1

    # Test 7
    result = teen_sum(6, 14)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(6, 14) expected 19, got {result}")
        failed += 1

    # Test 8
    result = teen_sum(15, 2)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(15, 2) expected 19, got {result}")
        failed += 1

    # Test 9
    result = teen_sum(19, 19)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(19, 19) expected 19, got {result}")
        failed += 1

    # Test 10
    result = teen_sum(19, 20)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(19, 20) expected 19, got {result}")
        failed += 1

    # Test 11
    result = teen_sum(2, 18)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(2, 18) expected 19, got {result}")
        failed += 1

    # Test 12
    result = teen_sum(12, 4)
    if result == 16:
        passed += 1
    else:
        print(f"FAIL: teen_sum(12, 4) expected 16, got {result}")
        failed += 1

    # Test 13
    result = teen_sum(2, 20)
    if result == 22:
        passed += 1
    else:
        print(f"FAIL: teen_sum(2, 20) expected 22, got {result}")
        failed += 1

    # Test 14
    result = teen_sum(2, 17)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(2, 17) expected 19, got {result}")
        failed += 1

    # Test 15
    result = teen_sum(2, 16)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: teen_sum(2, 16) expected 19, got {result}")
        failed += 1

    # Test 16
    result = teen_sum(6, 7)
    if result == 13:
        passed += 1
    else:
        print(f"FAIL: teen_sum(6, 7) expected 13, got {result}")
        failed += 1

    print(f"teen_sum: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
