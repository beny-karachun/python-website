"""
Tester for notString - CodingBat Python
7 test cases
"""

from not_string import not_string


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = not_string(\"candy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_string(\"candy\") expected \, got {result}")
        failed += 1

    # Test 2
    result = not_string(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_string(\"x\") expected \, got {result}")
        failed += 1

    # Test 3
    result = not_string(\"not bad\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_string(\"not bad\") expected \, got {result}")
        failed += 1

    # Test 4
    result = not_string(\"bad\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_string(\"bad\") expected \, got {result}")
        failed += 1

    # Test 5
    result = not_string(\"not\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_string(\"not\") expected \, got {result}")
        failed += 1

    # Test 6
    result = not_string(\"is not\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_string(\"is not\") expected \, got {result}")
        failed += 1

    # Test 7
    result = not_string(\"no\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_string(\"no\") expected \, got {result}")
        failed += 1

    print(f"not_string: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
