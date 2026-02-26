"""
Tester for atFirst - CodingBat Python
7 test cases
"""

from at_first import at_first


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = at_first(\"hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: at_first(\"hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = at_first(\"hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: at_first(\"hi\") expected \, got {result}")
        failed += 1

    # Test 3
    result = at_first(\"h\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: at_first(\"h\") expected \, got {result}")
        failed += 1

    # Test 4
    result = at_first(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: at_first(\"\") expected \, got {result}")
        failed += 1

    # Test 5
    result = at_first(\"kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: at_first(\"kitten\") expected \, got {result}")
        failed += 1

    # Test 6
    result = at_first(\"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: at_first(\"java\") expected \, got {result}")
        failed += 1

    # Test 7
    result = at_first(\"j\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: at_first(\"j\") expected \, got {result}")
        failed += 1

    print(f"at_first: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
