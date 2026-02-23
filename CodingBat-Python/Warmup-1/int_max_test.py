"""
Tester for intMax - CodingBat Python
11 test cases
"""

from int_max import int_max


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = int_max(1, 2, 3)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: int_max(1, 2, 3) expected 3, got {result}")
        failed += 1

    # Test 2
    result = int_max(1, 3, 2)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: int_max(1, 3, 2) expected 3, got {result}")
        failed += 1

    # Test 3
    result = int_max(3, 2, 1)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: int_max(3, 2, 1) expected 3, got {result}")
        failed += 1

    # Test 4
    result = int_max(9, 3, 3)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: int_max(9, 3, 3) expected 9, got {result}")
        failed += 1

    # Test 5
    result = int_max(3, 9, 3)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: int_max(3, 9, 3) expected 9, got {result}")
        failed += 1

    # Test 6
    result = int_max(3, 3, 9)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: int_max(3, 3, 9) expected 9, got {result}")
        failed += 1

    # Test 7
    result = int_max(8, 2, 3)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: int_max(8, 2, 3) expected 8, got {result}")
        failed += 1

    # Test 8
    result = int_max(-3, -1, -2)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: int_max(-3, -1, -2) expected -1, got {result}")
        failed += 1

    # Test 9
    result = int_max(6, 2, 5)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: int_max(6, 2, 5) expected 6, got {result}")
        failed += 1

    # Test 10
    result = int_max(5, 6, 2)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: int_max(5, 6, 2) expected 6, got {result}")
        failed += 1

    # Test 11
    result = int_max(5, 2, 6)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: int_max(5, 2, 6) expected 6, got {result}")
        failed += 1

    print(f"int_max: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
