"""
Tester for caughtSpeeding - CodingBat Python
12 test cases
"""

from caught_speeding import caught_speeding


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = caught_speeding(60, False)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(60, False) expected 0, got {result}")
        failed += 1

    # Test 2
    result = caught_speeding(65, False)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(65, False) expected 1, got {result}")
        failed += 1

    # Test 3
    result = caught_speeding(65, True)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(65, True) expected 0, got {result}")
        failed += 1

    # Test 4
    result = caught_speeding(80, False)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(80, False) expected 1, got {result}")
        failed += 1

    # Test 5
    result = caught_speeding(85, False)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(85, False) expected 2, got {result}")
        failed += 1

    # Test 6
    result = caught_speeding(85, True)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(85, True) expected 1, got {result}")
        failed += 1

    # Test 7
    result = caught_speeding(70, False)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(70, False) expected 1, got {result}")
        failed += 1

    # Test 8
    result = caught_speeding(75, False)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(75, False) expected 1, got {result}")
        failed += 1

    # Test 9
    result = caught_speeding(75, True)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(75, True) expected 1, got {result}")
        failed += 1

    # Test 10
    result = caught_speeding(40, False)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(40, False) expected 0, got {result}")
        failed += 1

    # Test 11
    result = caught_speeding(40, True)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(40, True) expected 0, got {result}")
        failed += 1

    # Test 12
    result = caught_speeding(90, False)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: caught_speeding(90, False) expected 2, got {result}")
        failed += 1

    print(f"caught_speeding: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
