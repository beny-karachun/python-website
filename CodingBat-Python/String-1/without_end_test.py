"""
Tester for withoutEnd - CodingBat Python
8 test cases
"""

from without_end import without_end


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = without_end(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = without_end(\"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"java\") expected \, got {result}")
        failed += 1

    # Test 3
    result = without_end(\"coding\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"coding\") expected \, got {result}")
        failed += 1

    # Test 4
    result = without_end(\"code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"code\") expected \, got {result}")
        failed += 1

    # Test 5
    result = without_end(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"ab\") expected \, got {result}")
        failed += 1

    # Test 6
    result = without_end(\"Chocolate!\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"Chocolate!\") expected \, got {result}")
        failed += 1

    # Test 7
    result = without_end(\"kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"kitten\") expected \, got {result}")
        failed += 1

    # Test 8
    result = without_end(\"woohoo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_end(\"woohoo\") expected \, got {result}")
        failed += 1

    print(f"without_end: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
