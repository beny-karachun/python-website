"""
Tester for stringMatch - CodingBat Python
10 test cases
"""

from string_match import string_match


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_match(\"xxcaazz\", \"xxbaaz\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: string_match(\"xxcaazz\", \"xxbaaz\") expected 3, got {result}")
        failed += 1

    # Test 2
    result = string_match(\"abc\", \"abc\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: string_match(\"abc\", \"abc\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = string_match(\"abc\", \"axc\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: string_match(\"abc\", \"axc\") expected 0, got {result}")
        failed += 1

    # Test 4
    result = string_match(\"hello\", \"he\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: string_match(\"hello\", \"he\") expected 1, got {result}")
        failed += 1

    # Test 5
    result = string_match(\"he\", \"hello\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: string_match(\"he\", \"hello\") expected 1, got {result}")
        failed += 1

    # Test 6
    result = string_match(\"h\", \"hello\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: string_match(\"h\", \"hello\") expected 0, got {result}")
        failed += 1

    # Test 7
    result = string_match(\"\", \"hello\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: string_match(\"\", \"hello\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = string_match(\"aabbccdd\", \"abbbxxd\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: string_match(\"aabbccdd\", \"abbbxxd\") expected 1, got {result}")
        failed += 1

    # Test 9
    result = string_match(\"aaxxaaxx\", \"iaxxai\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: string_match(\"aaxxaaxx\", \"iaxxai\") expected 3, got {result}")
        failed += 1

    # Test 10
    result = string_match(\"iaxxai\", \"aaxxaaxx\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: string_match(\"iaxxai\", \"aaxxaaxx\") expected 3, got {result}")
        failed += 1

    print(f"string_match: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
