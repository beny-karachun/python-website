"""
Tester for countXX - CodingBat Python
9 test cases
"""

from count_xx import count_xx


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_xx(\"abcxx\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"abcxx\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_xx(\"xxx\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"xxx\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_xx(\"xxxx\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"xxxx\") expected 3, got {result}")
        failed += 1

    # Test 4
    result = count_xx(\"abc\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"abc\") expected 0, got {result}")
        failed += 1

    # Test 5
    result = count_xx(\"Hello there\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"Hello there\") expected 0, got {result}")
        failed += 1

    # Test 6
    result = count_xx(\"Hexxo thxxe\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"Hexxo thxxe\") expected 2, got {result}")
        failed += 1

    # Test 7
    result = count_xx(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = count_xx(\"Kittens\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"Kittens\") expected 0, got {result}")
        failed += 1

    # Test 9
    result = count_xx(\"Kittensxxx\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_xx(\"Kittensxxx\") expected 2, got {result}")
        failed += 1

    print(f"count_xx: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
