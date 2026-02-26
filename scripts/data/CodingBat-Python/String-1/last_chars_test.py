"""
Tester for lastChars - CodingBat Python
9 test cases
"""

from last_chars import last_chars


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = last_chars(\"last\", \"chars\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"last\", \"chars\") expected \, got {result}")
        failed += 1

    # Test 2
    result = last_chars(\"yo\", \"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"yo\", \"java\") expected \, got {result}")
        failed += 1

    # Test 3
    result = last_chars(\"hi\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"hi\", \"\") expected \, got {result}")
        failed += 1

    # Test 4
    result = last_chars(\"\", \"hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"\", \"hello\") expected \, got {result}")
        failed += 1

    # Test 5
    result = last_chars(\"\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"\", \"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = last_chars(\"kitten\", \"hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"kitten\", \"hi\") expected \, got {result}")
        failed += 1

    # Test 7
    result = last_chars(\"k\", \"zip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"k\", \"zip\") expected \, got {result}")
        failed += 1

    # Test 8
    result = last_chars(\"kitten\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"kitten\", \"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = last_chars(\"kitten\", \"zip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: last_chars(\"kitten\", \"zip\") expected \, got {result}")
        failed += 1

    print(f"last_chars: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
