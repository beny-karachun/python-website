"""
Tester for icyHot - CodingBat Python
6 test cases
"""

from icy_hot import icy_hot


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = icy_hot(120, -1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: icy_hot(120, -1) expected True, got {result}")
        failed += 1

    # Test 2
    result = icy_hot(-1, 120)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: icy_hot(-1, 120) expected True, got {result}")
        failed += 1

    # Test 3
    result = icy_hot(2, 120)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: icy_hot(2, 120) expected False, got {result}")
        failed += 1

    # Test 4
    result = icy_hot(-1, 100)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: icy_hot(-1, 100) expected False, got {result}")
        failed += 1

    # Test 5
    result = icy_hot(-2, -2)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: icy_hot(-2, -2) expected False, got {result}")
        failed += 1

    # Test 6
    result = icy_hot(120, 120)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: icy_hot(120, 120) expected False, got {result}")
        failed += 1

    print(f"icy_hot: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
