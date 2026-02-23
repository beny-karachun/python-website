"""
Tester for sortaSum - CodingBat Python
9 test cases
"""

from sorta_sum import sorta_sum


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = sorta_sum(3, 4)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(3, 4) expected 7, got {result}")
        failed += 1

    # Test 2
    result = sorta_sum(9, 4)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(9, 4) expected 20, got {result}")
        failed += 1

    # Test 3
    result = sorta_sum(10, 11)
    if result == 21:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(10, 11) expected 21, got {result}")
        failed += 1

    # Test 4
    result = sorta_sum(12, -3)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(12, -3) expected 9, got {result}")
        failed += 1

    # Test 5
    result = sorta_sum(-3, 12)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(-3, 12) expected 9, got {result}")
        failed += 1

    # Test 6
    result = sorta_sum(4, 5)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(4, 5) expected 9, got {result}")
        failed += 1

    # Test 7
    result = sorta_sum(4, 6)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(4, 6) expected 20, got {result}")
        failed += 1

    # Test 8
    result = sorta_sum(14, 7)
    if result == 21:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(14, 7) expected 21, got {result}")
        failed += 1

    # Test 9
    result = sorta_sum(14, 6)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: sorta_sum(14, 6) expected 20, got {result}")
        failed += 1

    print(f"sorta_sum: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
