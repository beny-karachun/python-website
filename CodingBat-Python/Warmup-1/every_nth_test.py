"""
Tester for everyNth - CodingBat Python
7 test cases
"""

from every_nth import every_nth


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = every_nth(\"Miracle\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: every_nth(\"Miracle\", 2) expected \, got {result}")
        failed += 1

    # Test 2
    result = every_nth(\"abcdefg\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: every_nth(\"abcdefg\", 2) expected \, got {result}")
        failed += 1

    # Test 3
    result = every_nth(\"abcdefg\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: every_nth(\"abcdefg\", 3) expected \, got {result}")
        failed += 1

    # Test 4
    result = every_nth(\"Chocolate\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: every_nth(\"Chocolate\", 3) expected \, got {result}")
        failed += 1

    # Test 5
    result = every_nth(\"Chocolates\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: every_nth(\"Chocolates\", 3) expected \, got {result}")
        failed += 1

    # Test 6
    result = every_nth(\"Chocolates\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: every_nth(\"Chocolates\", 4) expected \, got {result}")
        failed += 1

    # Test 7
    result = every_nth(\"Chocolates\", 100)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: every_nth(\"Chocolates\", 100) expected \, got {result}")
        failed += 1

    print(f"every_nth: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
