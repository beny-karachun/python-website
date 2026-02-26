"""
Tester for posNeg - CodingBat Python
19 test cases
"""

from pos_neg import pos_neg


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = pos_neg(1, -1, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(1, -1, False) expected True, got {result}")
        failed += 1

    # Test 2
    result = pos_neg(-1, 1, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-1, 1, False) expected True, got {result}")
        failed += 1

    # Test 3
    result = pos_neg(-4, -5, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-4, -5, True) expected True, got {result}")
        failed += 1

    # Test 4
    result = pos_neg(-4, -5, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-4, -5, False) expected False, got {result}")
        failed += 1

    # Test 5
    result = pos_neg(-4, 5, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-4, 5, False) expected True, got {result}")
        failed += 1

    # Test 6
    result = pos_neg(-4, 5, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-4, 5, True) expected False, got {result}")
        failed += 1

    # Test 7
    result = pos_neg(1, 1, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(1, 1, False) expected False, got {result}")
        failed += 1

    # Test 8
    result = pos_neg(-1, -1, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-1, -1, False) expected False, got {result}")
        failed += 1

    # Test 9
    result = pos_neg(1, -1, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(1, -1, True) expected False, got {result}")
        failed += 1

    # Test 10
    result = pos_neg(-1, 1, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-1, 1, True) expected False, got {result}")
        failed += 1

    # Test 11
    result = pos_neg(1, 1, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(1, 1, True) expected False, got {result}")
        failed += 1

    # Test 12
    result = pos_neg(-1, -1, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-1, -1, True) expected True, got {result}")
        failed += 1

    # Test 13
    result = pos_neg(5, -5, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(5, -5, False) expected True, got {result}")
        failed += 1

    # Test 14
    result = pos_neg(-6, 6, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-6, 6, False) expected True, got {result}")
        failed += 1

    # Test 15
    result = pos_neg(-5, -6, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-5, -6, False) expected False, got {result}")
        failed += 1

    # Test 16
    result = pos_neg(-2, -1, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-2, -1, False) expected False, got {result}")
        failed += 1

    # Test 17
    result = pos_neg(1, 2, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(1, 2, False) expected False, got {result}")
        failed += 1

    # Test 18
    result = pos_neg(-5, 6, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-5, 6, True) expected False, got {result}")
        failed += 1

    # Test 19
    result = pos_neg(-5, -5, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: pos_neg(-5, -5, True) expected True, got {result}")
        failed += 1

    print(f"pos_neg: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
