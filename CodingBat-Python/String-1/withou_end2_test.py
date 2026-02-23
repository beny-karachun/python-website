"""
Tester for withouEnd2 - CodingBat Python
7 test cases
"""

from withou_end2 import withou_end2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = withou_end2(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: withou_end2(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = withou_end2(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: withou_end2(\"abc\") expected \, got {result}")
        failed += 1

    # Test 3
    result = withou_end2(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: withou_end2(\"ab\") expected \, got {result}")
        failed += 1

    # Test 4
    result = withou_end2(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: withou_end2(\"a\") expected \, got {result}")
        failed += 1

    # Test 5
    result = withou_end2(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: withou_end2(\"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = withou_end2(\"coldy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: withou_end2(\"coldy\") expected \, got {result}")
        failed += 1

    # Test 7
    result = withou_end2(\"java code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: withou_end2(\"java code\") expected \, got {result}")
        failed += 1

    print(f"withou_end2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
