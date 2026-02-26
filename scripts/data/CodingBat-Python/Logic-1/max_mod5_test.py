"""
Tester for maxMod5 - CodingBat Python
11 test cases
"""

from max_mod5 import max_mod5


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = max_mod5(2, 3)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: max_mod5(2, 3) expected 3, got {result}")
        failed += 1

    # Test 2
    result = max_mod5(6, 2)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: max_mod5(6, 2) expected 6, got {result}")
        failed += 1

    # Test 3
    result = max_mod5(3, 2)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: max_mod5(3, 2) expected 3, got {result}")
        failed += 1

    # Test 4
    result = max_mod5(8, 12)
    if result == 12:
        passed += 1
    else:
        print(f"FAIL: max_mod5(8, 12) expected 12, got {result}")
        failed += 1

    # Test 5
    result = max_mod5(7, 12)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: max_mod5(7, 12) expected 7, got {result}")
        failed += 1

    # Test 6
    result = max_mod5(11, 6)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: max_mod5(11, 6) expected 6, got {result}")
        failed += 1

    # Test 7
    result = max_mod5(2, 7)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: max_mod5(2, 7) expected 2, got {result}")
        failed += 1

    # Test 8
    result = max_mod5(7, 7)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: max_mod5(7, 7) expected 0, got {result}")
        failed += 1

    # Test 9
    result = max_mod5(9, 1)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: max_mod5(9, 1) expected 9, got {result}")
        failed += 1

    # Test 10
    result = max_mod5(9, 14)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: max_mod5(9, 14) expected 9, got {result}")
        failed += 1

    # Test 11
    result = max_mod5(1, 2)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: max_mod5(1, 2) expected 2, got {result}")
        failed += 1

    print(f"max_mod5: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
