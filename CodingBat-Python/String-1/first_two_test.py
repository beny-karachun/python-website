"""
Tester for firstTwo - CodingBat Python
8 test cases
"""

from first_two import first_two


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = first_two(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = first_two(\"abcdefg\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"abcdefg\") expected \, got {result}")
        failed += 1

    # Test 3
    result = first_two(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"ab\") expected \, got {result}")
        failed += 1

    # Test 4
    result = first_two(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"a\") expected \, got {result}")
        failed += 1

    # Test 5
    result = first_two(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = first_two(\"Kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"Kitten\") expected \, got {result}")
        failed += 1

    # Test 7
    result = first_two(\"hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"hi\") expected \, got {result}")
        failed += 1

    # Test 8
    result = first_two(\"hiya\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_two(\"hiya\") expected \, got {result}")
        failed += 1

    print(f"first_two: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
