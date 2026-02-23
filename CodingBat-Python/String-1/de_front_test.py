"""
Tester for deFront - CodingBat Python
19 test cases
"""

from de_front import de_front


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = de_front(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = de_front(\"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"java\") expected \, got {result}")
        failed += 1

    # Test 3
    result = de_front(\"away\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"away\") expected \, got {result}")
        failed += 1

    # Test 4
    result = de_front(\"axy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"axy\") expected \, got {result}")
        failed += 1

    # Test 5
    result = de_front(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"abc\") expected \, got {result}")
        failed += 1

    # Test 6
    result = de_front(\"xby\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"xby\") expected \, got {result}")
        failed += 1

    # Test 7
    result = de_front(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"ab\") expected \, got {result}")
        failed += 1

    # Test 8
    result = de_front(\"ax\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"ax\") expected \, got {result}")
        failed += 1

    # Test 9
    result = de_front(\"axb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"axb\") expected \, got {result}")
        failed += 1

    # Test 10
    result = de_front(\"aaa\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"aaa\") expected \, got {result}")
        failed += 1

    # Test 11
    result = de_front(\"xbc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"xbc\") expected \, got {result}")
        failed += 1

    # Test 12
    result = de_front(\"bbb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"bbb\") expected \, got {result}")
        failed += 1

    # Test 13
    result = de_front(\"bazz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"bazz\") expected \, got {result}")
        failed += 1

    # Test 14
    result = de_front(\"ba\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"ba\") expected \, got {result}")
        failed += 1

    # Test 15
    result = de_front(\"abxyz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"abxyz\") expected \, got {result}")
        failed += 1

    # Test 16
    result = de_front(\"hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"hi\") expected \, got {result}")
        failed += 1

    # Test 17
    result = de_front(\"his\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"his\") expected \, got {result}")
        failed += 1

    # Test 18
    result = de_front(\"xz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"xz\") expected \, got {result}")
        failed += 1

    # Test 19
    result = de_front(\"zzz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: de_front(\"zzz\") expected \, got {result}")
        failed += 1

    print(f"de_front: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
