"""
Tester for fizzString - CodingBat Python
16 test cases
"""

from fizz_string import fizz_string


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = fizz_string(\"fig\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"fig\") expected \, got {result}")
        failed += 1

    # Test 2
    result = fizz_string(\"dib\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"dib\") expected \, got {result}")
        failed += 1

    # Test 3
    result = fizz_string(\"fib\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"fib\") expected \, got {result}")
        failed += 1

    # Test 4
    result = fizz_string(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"abc\") expected \, got {result}")
        failed += 1

    # Test 5
    result = fizz_string(\"fooo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"fooo\") expected \, got {result}")
        failed += 1

    # Test 6
    result = fizz_string(\"booo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"booo\") expected \, got {result}")
        failed += 1

    # Test 7
    result = fizz_string(\"ooob\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"ooob\") expected \, got {result}")
        failed += 1

    # Test 8
    result = fizz_string(\"fooob\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"fooob\") expected \, got {result}")
        failed += 1

    # Test 9
    result = fizz_string(\"f\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"f\") expected \, got {result}")
        failed += 1

    # Test 10
    result = fizz_string(\"b\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"b\") expected \, got {result}")
        failed += 1

    # Test 11
    result = fizz_string(\"abcb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"abcb\") expected \, got {result}")
        failed += 1

    # Test 12
    result = fizz_string(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 13
    result = fizz_string(\"Hellob\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"Hellob\") expected \, got {result}")
        failed += 1

    # Test 14
    result = fizz_string(\"af\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"af\") expected \, got {result}")
        failed += 1

    # Test 15
    result = fizz_string(\"bf\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"bf\") expected \, got {result}")
        failed += 1

    # Test 16
    result = fizz_string(\"fb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string(\"fb\") expected \, got {result}")
        failed += 1

    print(f"fizz_string: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
