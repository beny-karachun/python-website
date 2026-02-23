"""
Tester for missingChar - CodingBat Python
10 test cases
"""

from missing_char import missing_char


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = missing_char(\"kitten\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"kitten\", 1) expected \, got {result}")
        failed += 1

    # Test 2
    result = missing_char(\"kitten\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"kitten\", 0) expected \, got {result}")
        failed += 1

    # Test 3
    result = missing_char(\"kitten\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"kitten\", 4) expected \, got {result}")
        failed += 1

    # Test 4
    result = missing_char(\"Hi\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"Hi\", 0) expected \, got {result}")
        failed += 1

    # Test 5
    result = missing_char(\"Hi\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"Hi\", 1) expected \, got {result}")
        failed += 1

    # Test 6
    result = missing_char(\"code\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"code\", 0) expected \, got {result}")
        failed += 1

    # Test 7
    result = missing_char(\"code\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"code\", 1) expected \, got {result}")
        failed += 1

    # Test 8
    result = missing_char(\"code\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"code\", 2) expected \, got {result}")
        failed += 1

    # Test 9
    result = missing_char(\"code\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"code\", 3) expected \, got {result}")
        failed += 1

    # Test 10
    result = missing_char(\"chocolate\", 8)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: missing_char(\"chocolate\", 8) expected \, got {result}")
        failed += 1

    print(f"missing_char: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
