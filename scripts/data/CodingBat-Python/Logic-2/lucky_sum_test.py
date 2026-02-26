"""
Tester for luckySum - CodingBat Python
12 test cases
"""

from lucky_sum import lucky_sum


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = lucky_sum(1, 2, 3)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(1, 2, 3) expected 6, got {result}")
        failed += 1

    # Test 2
    result = lucky_sum(1, 2, 13)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(1, 2, 13) expected 3, got {result}")
        failed += 1

    # Test 3
    result = lucky_sum(1, 13, 3)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(1, 13, 3) expected 1, got {result}")
        failed += 1

    # Test 4
    result = lucky_sum(1, 13, 13)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(1, 13, 13) expected 1, got {result}")
        failed += 1

    # Test 5
    result = lucky_sum(6, 5, 2)
    if result == 13:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(6, 5, 2) expected 13, got {result}")
        failed += 1

    # Test 6
    result = lucky_sum(13, 2, 3)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(13, 2, 3) expected 0, got {result}")
        failed += 1

    # Test 7
    result = lucky_sum(13, 2, 13)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(13, 2, 13) expected 0, got {result}")
        failed += 1

    # Test 8
    result = lucky_sum(13, 13, 2)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(13, 13, 2) expected 0, got {result}")
        failed += 1

    # Test 9
    result = lucky_sum(9, 4, 13)
    if result == 13:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(9, 4, 13) expected 13, got {result}")
        failed += 1

    # Test 10
    result = lucky_sum(8, 13, 2)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(8, 13, 2) expected 8, got {result}")
        failed += 1

    # Test 11
    result = lucky_sum(7, 2, 1)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(7, 2, 1) expected 10, got {result}")
        failed += 1

    # Test 12
    result = lucky_sum(3, 3, 13)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: lucky_sum(3, 3, 13) expected 6, got {result}")
        failed += 1

    print(f"lucky_sum: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
