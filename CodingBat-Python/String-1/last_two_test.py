"""
Tester for lastTwo - CodingBat Python
5 test cases
"""

from last_two import last_two


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = last_two(\"coding\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_two(\"coding\") expected \, got {result}")
        failed += 1

    # Test 2
    result = last_two(\"cat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_two(\"cat\") expected \, got {result}")
        failed += 1

    # Test 3
    result = last_two(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_two(\"ab\") expected \, got {result}")
        failed += 1

    # Test 4
    result = last_two(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_two(\"a\") expected \, got {result}")
        failed += 1

    # Test 5
    result = last_two(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_two(\"\") expected \, got {result}")
        failed += 1

    print(f"last_two: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
