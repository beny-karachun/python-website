"""
Tester for allStar - CodingBat Python
8 test cases
"""

from all_star import all_star


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = all_star(\"hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = all_star(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"abc\") expected \, got {result}")
        failed += 1

    # Test 3
    result = all_star(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"ab\") expected \, got {result}")
        failed += 1

    # Test 4
    result = all_star(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"a\") expected \, got {result}")
        failed += 1

    # Test 5
    result = all_star(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = all_star(\"3.14\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"3.14\") expected \, got {result}")
        failed += 1

    # Test 7
    result = all_star(\"Chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"Chocolate\") expected \, got {result}")
        failed += 1

    # Test 8
    result = all_star(\"1234\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: all_star(\"1234\") expected \, got {result}")
        failed += 1

    print(f"all_star: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
