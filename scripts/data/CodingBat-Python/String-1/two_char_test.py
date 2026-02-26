"""
Tester for twoChar - CodingBat Python
15 test cases
"""

from two_char import two_char


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = two_char(\"java\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"java\", 0) expected \, got {result}")
        failed += 1

    # Test 2
    result = two_char(\"java\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"java\", 2) expected \, got {result}")
        failed += 1

    # Test 3
    result = two_char(\"java\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"java\", 3) expected \, got {result}")
        failed += 1

    # Test 4
    result = two_char(\"java\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"java\", 4) expected \, got {result}")
        failed += 1

    # Test 5
    result = two_char(\"java\", -1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"java\", -1) expected \, got {result}")
        failed += 1

    # Test 6
    result = two_char(\"Hello\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", 0) expected \, got {result}")
        failed += 1

    # Test 7
    result = two_char(\"Hello\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", 1) expected \, got {result}")
        failed += 1

    # Test 8
    result = two_char(\"Hello\", 99)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", 99) expected \, got {result}")
        failed += 1

    # Test 9
    result = two_char(\"Hello\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", 3) expected \, got {result}")
        failed += 1

    # Test 10
    result = two_char(\"Hello\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", 4) expected \, got {result}")
        failed += 1

    # Test 11
    result = two_char(\"Hello\", 5)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", 5) expected \, got {result}")
        failed += 1

    # Test 12
    result = two_char(\"Hello\", -7)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", -7) expected \, got {result}")
        failed += 1

    # Test 13
    result = two_char(\"Hello\", 6)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", 6) expected \, got {result}")
        failed += 1

    # Test 14
    result = two_char(\"Hello\", -1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"Hello\", -1) expected \, got {result}")
        failed += 1

    # Test 15
    result = two_char(\"yay\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: two_char(\"yay\", 0) expected \, got {result}")
        failed += 1

    print(f"two_char: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
