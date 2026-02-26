"""
Tester for countTriple - CodingBat Python
12 test cases
"""

from count_triple import count_triple


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_triple(\"abcXXXabc\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"abcXXXabc\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_triple(\"xxxabyyyycd\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"xxxabyyyycd\") expected 3, got {result}")
        failed += 1

    # Test 3
    result = count_triple(\"a\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"a\") expected 0, got {result}")
        failed += 1

    # Test 4
    result = count_triple(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"\") expected 0, got {result}")
        failed += 1

    # Test 5
    result = count_triple(\"XXXabc\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"XXXabc\") expected 1, got {result}")
        failed += 1

    # Test 6
    result = count_triple(\"XXXXabc\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"XXXXabc\") expected 2, got {result}")
        failed += 1

    # Test 7
    result = count_triple(\"XXXXXabc\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"XXXXXabc\") expected 3, got {result}")
        failed += 1

    # Test 8
    result = count_triple(\"222abyyycdXXX\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"222abyyycdXXX\") expected 3, got {result}")
        failed += 1

    # Test 9
    result = count_triple(\"abYYYabXXXXXab\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"abYYYabXXXXXab\") expected 4, got {result}")
        failed += 1

    # Test 10
    result = count_triple(\"abYYXabXXYXXab\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"abYYXabXXYXXab\") expected 0, got {result}")
        failed += 1

    # Test 11
    result = count_triple(\"abYYXabXXYXXab\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"abYYXabXXYXXab\") expected 0, got {result}")
        failed += 1

    # Test 12
    result = count_triple(\"122abhhh2\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_triple(\"122abhhh2\") expected 1, got {result}")
        failed += 1

    print(f"count_triple: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
