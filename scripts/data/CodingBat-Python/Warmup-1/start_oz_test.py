"""
Tester for startOz - CodingBat Python
12 test cases
"""

from start_oz import start_oz


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = start_oz(\"ozymandias\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"ozymandias\") expected \, got {result}")
        failed += 1

    # Test 2
    result = start_oz(\"bzoo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"bzoo\") expected \, got {result}")
        failed += 1

    # Test 3
    result = start_oz(\"oxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"oxx\") expected \, got {result}")
        failed += 1

    # Test 4
    result = start_oz(\"oz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"oz\") expected \, got {result}")
        failed += 1

    # Test 5
    result = start_oz(\"ounce\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"ounce\") expected \, got {result}")
        failed += 1

    # Test 6
    result = start_oz(\"o\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"o\") expected \, got {result}")
        failed += 1

    # Test 7
    result = start_oz(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"abc\") expected \, got {result}")
        failed += 1

    # Test 8
    result = start_oz(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = start_oz(\"zoo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"zoo\") expected \, got {result}")
        failed += 1

    # Test 10
    result = start_oz(\"aztec\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"aztec\") expected \, got {result}")
        failed += 1

    # Test 11
    result = start_oz(\"zzzz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"zzzz\") expected \, got {result}")
        failed += 1

    # Test 12
    result = start_oz(\"oznic\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_oz(\"oznic\") expected \, got {result}")
        failed += 1

    print(f"start_oz: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
