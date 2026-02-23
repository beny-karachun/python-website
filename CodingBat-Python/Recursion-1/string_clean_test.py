"""
Tester for stringClean - CodingBat Python
6 test cases
"""

from string_clean import string_clean


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_clean(\"yyzzza\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_clean(\"yyzzza\") expected \, got {result}")
        failed += 1

    # Test 2
    result = string_clean(\"abbbcdd\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_clean(\"abbbcdd\") expected \, got {result}")
        failed += 1

    # Test 3
    result = string_clean(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_clean(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 4
    result = string_clean(\"XXabcYY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_clean(\"XXabcYY\") expected \, got {result}")
        failed += 1

    # Test 5
    result = string_clean(\"112ab445\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_clean(\"112ab445\") expected \, got {result}")
        failed += 1

    # Test 6
    result = string_clean(\"Hello Bookkeeper\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_clean(\"Hello Bookkeeper\") expected \, got {result}")
        failed += 1

    print(f"string_clean: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
