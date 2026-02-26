"""
Tester for powerN - CodingBat Python
11 test cases
"""

from power_n import power_n


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = power_n(3, 1)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: power_n(3, 1) expected 3, got {result}")
        failed += 1

    # Test 2
    result = power_n(3, 2)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: power_n(3, 2) expected 9, got {result}")
        failed += 1

    # Test 3
    result = power_n(3, 3)
    if result == 27:
        passed += 1
    else:
        print(f"FAIL: power_n(3, 3) expected 27, got {result}")
        failed += 1

    # Test 4
    result = power_n(2, 1)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: power_n(2, 1) expected 2, got {result}")
        failed += 1

    # Test 5
    result = power_n(2, 2)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: power_n(2, 2) expected 4, got {result}")
        failed += 1

    # Test 6
    result = power_n(2, 3)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: power_n(2, 3) expected 8, got {result}")
        failed += 1

    # Test 7
    result = power_n(2, 4)
    if result == 16:
        passed += 1
    else:
        print(f"FAIL: power_n(2, 4) expected 16, got {result}")
        failed += 1

    # Test 8
    result = power_n(2, 5)
    if result == 32:
        passed += 1
    else:
        print(f"FAIL: power_n(2, 5) expected 32, got {result}")
        failed += 1

    # Test 9
    result = power_n(10, 1)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: power_n(10, 1) expected 10, got {result}")
        failed += 1

    # Test 10
    result = power_n(10, 2)
    if result == 100:
        passed += 1
    else:
        print(f"FAIL: power_n(10, 2) expected 100, got {result}")
        failed += 1

    # Test 11
    result = power_n(10, 3)
    if result == 1000:
        passed += 1
    else:
        print(f"FAIL: power_n(10, 3) expected 1000, got {result}")
        failed += 1

    print(f"power_n: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
