"""
Tester for countAbc - CodingBat Python
12 test cases
"""

from count_abc import count_abc


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_abc(\"abc\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"abc\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_abc(\"abcxxabc\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"abcxxabc\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_abc(\"abaxxaba\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"abaxxaba\") expected 2, got {result}")
        failed += 1

    # Test 4
    result = count_abc(\"ababc\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"ababc\") expected 2, got {result}")
        failed += 1

    # Test 5
    result = count_abc(\"abxbc\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"abxbc\") expected 0, got {result}")
        failed += 1

    # Test 6
    result = count_abc(\"aaabc\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"aaabc\") expected 1, got {result}")
        failed += 1

    # Test 7
    result = count_abc(\"hello\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"hello\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = count_abc(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"\") expected 0, got {result}")
        failed += 1

    # Test 9
    result = count_abc(\"ab\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"ab\") expected 0, got {result}")
        failed += 1

    # Test 10
    result = count_abc(\"aba\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"aba\") expected 1, got {result}")
        failed += 1

    # Test 11
    result = count_abc(\"aca\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"aca\") expected 0, got {result}")
        failed += 1

    # Test 12
    result = count_abc(\"aaa\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_abc(\"aaa\") expected 0, got {result}")
        failed += 1

    print(f"count_abc: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
