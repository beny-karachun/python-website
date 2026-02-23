"""
Tester for nonStart - CodingBat Python
9 test cases
"""

from non_start import non_start


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = non_start(\"Hello\", \"There\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"Hello\", \"There\") expected \, got {result}")
        failed += 1

    # Test 2
    result = non_start(\"java\", \"code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"java\", \"code\") expected \, got {result}")
        failed += 1

    # Test 3
    result = non_start(\"shotl\", \"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"shotl\", \"java\") expected \, got {result}")
        failed += 1

    # Test 4
    result = non_start(\"ab\", \"xy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"ab\", \"xy\") expected \, got {result}")
        failed += 1

    # Test 5
    result = non_start(\"ab\", \"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"ab\", \"x\") expected \, got {result}")
        failed += 1

    # Test 6
    result = non_start(\"x\", \"ac\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"x\", \"ac\") expected \, got {result}")
        failed += 1

    # Test 7
    result = non_start(\"a\", \"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"a\", \"x\") expected \, got {result}")
        failed += 1

    # Test 8
    result = non_start(\"kit\", \"kat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"kit\", \"kat\") expected \, got {result}")
        failed += 1

    # Test 9
    result = non_start(\"mart\", \"dart\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: non_start(\"mart\", \"dart\") expected \, got {result}")
        failed += 1

    print(f"non_start: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
