"""
Tester for loneSum - CodingBat Python
9 test cases
"""

from lone_sum import lone_sum


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = lone_sum(1, 2, 3)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: lone_sum(1, 2, 3) expected 6, got {result}")
        failed += 1

    # Test 2
    result = lone_sum(3, 2, 3)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: lone_sum(3, 2, 3) expected 2, got {result}")
        failed += 1

    # Test 3
    result = lone_sum(3, 3, 3)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: lone_sum(3, 3, 3) expected 0, got {result}")
        failed += 1

    # Test 4
    result = lone_sum(9, 2, 2)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: lone_sum(9, 2, 2) expected 9, got {result}")
        failed += 1

    # Test 5
    result = lone_sum(2, 2, 9)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: lone_sum(2, 2, 9) expected 9, got {result}")
        failed += 1

    # Test 6
    result = lone_sum(2, 9, 2)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: lone_sum(2, 9, 2) expected 9, got {result}")
        failed += 1

    # Test 7
    result = lone_sum(2, 9, 3)
    if result == 14:
        passed += 1
    else:
        print(f"FAIL: lone_sum(2, 9, 3) expected 14, got {result}")
        failed += 1

    # Test 8
    result = lone_sum(4, 2, 3)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: lone_sum(4, 2, 3) expected 9, got {result}")
        failed += 1

    # Test 9
    result = lone_sum(1, 3, 1)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: lone_sum(1, 3, 1) expected 3, got {result}")
        failed += 1

    print(f"lone_sum: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
