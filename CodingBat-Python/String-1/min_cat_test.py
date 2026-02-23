"""
Tester for minCat - CodingBat Python
6 test cases
"""

from min_cat import min_cat


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = min_cat(\"Hello\", \"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: min_cat(\"Hello\", \"Hi\") expected \, got {result}")
        failed += 1

    # Test 2
    result = min_cat(\"Hello\", \"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: min_cat(\"Hello\", \"java\") expected \, got {result}")
        failed += 1

    # Test 3
    result = min_cat(\"java\", \"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: min_cat(\"java\", \"Hello\") expected \, got {result}")
        failed += 1

    # Test 4
    result = min_cat(\"abc\", \"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: min_cat(\"abc\", \"x\") expected \, got {result}")
        failed += 1

    # Test 5
    result = min_cat(\"x\", \"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: min_cat(\"x\", \"abc\") expected \, got {result}")
        failed += 1

    # Test 6
    result = min_cat(\"abc\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: min_cat(\"abc\", \"\") expected \, got {result}")
        failed += 1

    print(f"min_cat: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
