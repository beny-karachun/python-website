"""
Tester for doubleChar - CodingBat Python
9 test cases
"""

from double_char import double_char


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = double_char(\"The\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"The\") expected \, got {result}")
        failed += 1

    # Test 2
    result = double_char(\"AAbb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"AAbb\") expected \, got {result}")
        failed += 1

    # Test 3
    result = double_char(\"Hi-There\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"Hi-There\") expected \, got {result}")
        failed += 1

    # Test 4
    result = double_char(\"Word!\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"Word!\") expected \, got {result}")
        failed += 1

    # Test 5
    result = double_char(\"!!\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"!!\") expected \, got {result}")
        failed += 1

    # Test 6
    result = double_char(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"\") expected \, got {result}")
        failed += 1

    # Test 7
    result = double_char(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"a\") expected \, got {result}")
        failed += 1

    # Test 8
    result = double_char(\".\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\".\") expected \, got {result}")
        failed += 1

    # Test 9
    result = double_char(\"aa\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: double_char(\"aa\") expected \, got {result}")
        failed += 1

    print(f"double_char: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
