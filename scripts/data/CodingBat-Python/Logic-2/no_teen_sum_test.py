"""
Tester for noTeenSum - CodingBat Python
16 test cases
"""

from no_teen_sum import no_teen_sum


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = no_teen_sum(1, 2, 3)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(1, 2, 3) expected 6, got {result}")
        failed += 1

    # Test 2
    result = no_teen_sum(2, 13, 1)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(2, 13, 1) expected 3, got {result}")
        failed += 1

    # Test 3
    result = no_teen_sum(2, 1, 14)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(2, 1, 14) expected 3, got {result}")
        failed += 1

    # Test 4
    result = no_teen_sum(2, 1, 15)
    if result == 18:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(2, 1, 15) expected 18, got {result}")
        failed += 1

    # Test 5
    result = no_teen_sum(2, 1, 16)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(2, 1, 16) expected 19, got {result}")
        failed += 1

    # Test 6
    result = no_teen_sum(2, 1, 17)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(2, 1, 17) expected 3, got {result}")
        failed += 1

    # Test 7
    result = no_teen_sum(17, 1, 2)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(17, 1, 2) expected 3, got {result}")
        failed += 1

    # Test 8
    result = no_teen_sum(2, 15, 2)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(2, 15, 2) expected 19, got {result}")
        failed += 1

    # Test 9
    result = no_teen_sum(16, 17, 18)
    if result == 16:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(16, 17, 18) expected 16, got {result}")
        failed += 1

    # Test 10
    result = no_teen_sum(17, 18, 19)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(17, 18, 19) expected 0, got {result}")
        failed += 1

    # Test 11
    result = no_teen_sum(15, 16, 1)
    if result == 32:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(15, 16, 1) expected 32, got {result}")
        failed += 1

    # Test 12
    result = no_teen_sum(15, 15, 19)
    if result == 30:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(15, 15, 19) expected 30, got {result}")
        failed += 1

    # Test 13
    result = no_teen_sum(15, 19, 16)
    if result == 31:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(15, 19, 16) expected 31, got {result}")
        failed += 1

    # Test 14
    result = no_teen_sum(5, 17, 18)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(5, 17, 18) expected 5, got {result}")
        failed += 1

    # Test 15
    result = no_teen_sum(17, 18, 16)
    if result == 16:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(17, 18, 16) expected 16, got {result}")
        failed += 1

    # Test 16
    result = no_teen_sum(17, 19, 18)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: no_teen_sum(17, 19, 18) expected 0, got {result}")
        failed += 1

    print(f"no_teen_sum: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
