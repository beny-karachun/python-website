"""
Tester for evenlySpaced - CodingBat Python
14 test cases
"""

from evenly_spaced import evenly_spaced


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = evenly_spaced(2, 4, 6)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(2, 4, 6) expected True, got {result}")
        failed += 1

    # Test 2
    result = evenly_spaced(4, 6, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(4, 6, 2) expected True, got {result}")
        failed += 1

    # Test 3
    result = evenly_spaced(4, 6, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(4, 6, 3) expected False, got {result}")
        failed += 1

    # Test 4
    result = evenly_spaced(6, 2, 4)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(6, 2, 4) expected True, got {result}")
        failed += 1

    # Test 5
    result = evenly_spaced(6, 2, 8)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(6, 2, 8) expected False, got {result}")
        failed += 1

    # Test 6
    result = evenly_spaced(2, 2, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(2, 2, 2) expected True, got {result}")
        failed += 1

    # Test 7
    result = evenly_spaced(2, 2, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(2, 2, 3) expected False, got {result}")
        failed += 1

    # Test 8
    result = evenly_spaced(9, 10, 11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(9, 10, 11) expected True, got {result}")
        failed += 1

    # Test 9
    result = evenly_spaced(10, 9, 11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(10, 9, 11) expected True, got {result}")
        failed += 1

    # Test 10
    result = evenly_spaced(10, 9, 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(10, 9, 9) expected False, got {result}")
        failed += 1

    # Test 11
    result = evenly_spaced(2, 4, 4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(2, 4, 4) expected False, got {result}")
        failed += 1

    # Test 12
    result = evenly_spaced(2, 2, 4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(2, 2, 4) expected False, got {result}")
        failed += 1

    # Test 13
    result = evenly_spaced(3, 6, 12)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(3, 6, 12) expected False, got {result}")
        failed += 1

    # Test 14
    result = evenly_spaced(12, 3, 6)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: evenly_spaced(12, 3, 6) expected False, got {result}")
        failed += 1

    print(f"evenly_spaced: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
