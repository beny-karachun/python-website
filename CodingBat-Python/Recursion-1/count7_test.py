"""
Tester for count7 - CodingBat Python
13 test cases
"""

from count7 import count7


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count7(717)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count7(717) expected 2, got {result}")
        failed += 1

    # Test 2
    result = count7(7)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count7(7) expected 1, got {result}")
        failed += 1

    # Test 3
    result = count7(123)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count7(123) expected 0, got {result}")
        failed += 1

    # Test 4
    result = count7(77)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count7(77) expected 2, got {result}")
        failed += 1

    # Test 5
    result = count7(7123)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count7(7123) expected 1, got {result}")
        failed += 1

    # Test 6
    result = count7(771237)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count7(771237) expected 3, got {result}")
        failed += 1

    # Test 7
    result = count7(771737)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count7(771737) expected 4, got {result}")
        failed += 1

    # Test 8
    result = count7(47571)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count7(47571) expected 2, got {result}")
        failed += 1

    # Test 9
    result = count7(777777)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: count7(777777) expected 6, got {result}")
        failed += 1

    # Test 10
    result = count7(70701277)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count7(70701277) expected 4, got {result}")
        failed += 1

    # Test 11
    result = count7(777576197)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: count7(777576197) expected 5, got {result}")
        failed += 1

    # Test 12
    result = count7(99999)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count7(99999) expected 0, got {result}")
        failed += 1

    # Test 13
    result = count7(99799)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count7(99799) expected 1, got {result}")
        failed += 1

    print(f"count7: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
