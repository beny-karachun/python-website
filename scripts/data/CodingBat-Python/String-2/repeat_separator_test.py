"""
Tester for repeatSeparator - CodingBat Python
11 test cases
"""

from repeat_separator import repeat_separator


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = repeat_separator(\"Word\", \"X\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"Word\", \"X\", 3) expected \, got {result}")
        failed += 1

    # Test 2
    result = repeat_separator(\"This\", \"And\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"This\", \"And\", 2) expected \, got {result}")
        failed += 1

    # Test 3
    result = repeat_separator(\"This\", \"And\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"This\", \"And\", 1) expected \, got {result}")
        failed += 1

    # Test 4
    result = repeat_separator(\"Hi\", \"-n-\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"Hi\", \"-n-\", 2) expected \, got {result}")
        failed += 1

    # Test 5
    result = repeat_separator(\"AAA\", \"\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"AAA\", \"\", 1) expected \, got {result}")
        failed += 1

    # Test 6
    result = repeat_separator(\"AAA\", \"\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"AAA\", \"\", 0) expected \, got {result}")
        failed += 1

    # Test 7
    result = repeat_separator(\"A\", \"B\", 5)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"A\", \"B\", 5) expected \, got {result}")
        failed += 1

    # Test 8
    result = repeat_separator(\"abc\", \"XX\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"abc\", \"XX\", 3) expected \, got {result}")
        failed += 1

    # Test 9
    result = repeat_separator(\"abc\", \"XX\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"abc\", \"XX\", 2) expected \, got {result}")
        failed += 1

    # Test 10
    result = repeat_separator(\"abc\", \"XX\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"abc\", \"XX\", 1) expected \, got {result}")
        failed += 1

    # Test 11
    result = repeat_separator(\"XYZ\", \"a\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_separator(\"XYZ\", \"a\", 2) expected \, got {result}")
        failed += 1

    print(f"repeat_separator: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
