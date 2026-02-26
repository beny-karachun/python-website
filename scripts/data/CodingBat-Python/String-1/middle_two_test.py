"""
Tester for middleTwo - CodingBat Python
5 test cases
"""

from middle_two import middle_two


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = middle_two(\"string\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_two(\"string\") expected \, got {result}")
        failed += 1

    # Test 2
    result = middle_two(\"code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_two(\"code\") expected \, got {result}")
        failed += 1

    # Test 3
    result = middle_two(\"Practice\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_two(\"Practice\") expected \, got {result}")
        failed += 1

    # Test 4
    result = middle_two(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_two(\"ab\") expected \, got {result}")
        failed += 1

    # Test 5
    result = middle_two(\"0123456789\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_two(\"0123456789\") expected \, got {result}")
        failed += 1

    print(f"middle_two: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
