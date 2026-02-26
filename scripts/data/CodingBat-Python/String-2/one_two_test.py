"""
Tester for oneTwo - CodingBat Python
16 test cases
"""

from one_two import one_two


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = one_two(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"abc\") expected \, got {result}")
        failed += 1

    # Test 2
    result = one_two(\"tca\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"tca\") expected \, got {result}")
        failed += 1

    # Test 3
    result = one_two(\"tcagdo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"tcagdo\") expected \, got {result}")
        failed += 1

    # Test 4
    result = one_two(\"chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"chocolate\") expected \, got {result}")
        failed += 1

    # Test 5
    result = one_two(\"1234567890\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"1234567890\") expected \, got {result}")
        failed += 1

    # Test 6
    result = one_two(\"xabxabxabxabxabxabxab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"xabxabxabxabxabxabxab\") expected \, got {result}")
        failed += 1

    # Test 7
    result = one_two(\"abcdefx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"abcdefx\") expected \, got {result}")
        failed += 1

    # Test 8
    result = one_two(\"abcdefxy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"abcdefxy\") expected \, got {result}")
        failed += 1

    # Test 9
    result = one_two(\"abcdefxyz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"abcdefxyz\") expected \, got {result}")
        failed += 1

    # Test 10
    result = one_two(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"\") expected \, got {result}")
        failed += 1

    # Test 11
    result = one_two(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"x\") expected \, got {result}")
        failed += 1

    # Test 12
    result = one_two(\"xy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"xy\") expected \, got {result}")
        failed += 1

    # Test 13
    result = one_two(\"xyz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"xyz\") expected \, got {result}")
        failed += 1

    # Test 14
    result = one_two(\"abcdefghijklkmnopqrstuvwxyz1234567890\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"abcdefghijklkmnopqrstuvwxyz1234567890\") expected \, got {result}")
        failed += 1

    # Test 15
    result = one_two(\"abcdefghijklkmnopqrstuvwxyz123456789\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"abcdefghijklkmnopqrstuvwxyz123456789\") expected \, got {result}")
        failed += 1

    # Test 16
    result = one_two(\"abcdefghijklkmnopqrstuvwxyz12345678\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: one_two(\"abcdefghijklkmnopqrstuvwxyz12345678\") expected \, got {result}")
        failed += 1

    print(f"one_two: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
