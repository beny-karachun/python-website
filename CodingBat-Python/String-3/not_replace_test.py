"""
Tester for notReplace - CodingBat Python
11 test cases
"""

from not_replace import not_replace


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = not_replace(\"is test\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"is test\") expected \, got {result}")
        failed += 1

    # Test 2
    result = not_replace(\"is-is\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"is-is\") expected \, got {result}")
        failed += 1

    # Test 3
    result = not_replace(\"This is right\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"This is right\") expected \, got {result}")
        failed += 1

    # Test 4
    result = not_replace(\"This is isabell\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"This is isabell\") expected \, got {result}")
        failed += 1

    # Test 5
    result = not_replace(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = not_replace(\"is\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"is\") expected \, got {result}")
        failed += 1

    # Test 7
    result = not_replace(\"isis\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"isis\") expected \, got {result}")
        failed += 1

    # Test 8
    result = not_replace(\"Dis is bliss is\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"Dis is bliss is\") expected \, got {result}")
        failed += 1

    # Test 9
    result = not_replace(\"is his\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"is his\") expected \, got {result}")
        failed += 1

    # Test 10
    result = not_replace(\"xis yis\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"xis yis\") expected \, got {result}")
        failed += 1

    # Test 11
    result = not_replace(\"AAAis is\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: not_replace(\"AAAis is\") expected \, got {result}")
        failed += 1

    print(f"not_replace: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
