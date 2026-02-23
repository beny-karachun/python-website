"""
Tester for startWord - CodingBat Python
15 test cases
"""

from start_word import start_word


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = start_word(\"hippo\", \"hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hippo\", \"hi\") expected \, got {result}")
        failed += 1

    # Test 2
    result = start_word(\"hippo\", \"xip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hippo\", \"xip\") expected \, got {result}")
        failed += 1

    # Test 3
    result = start_word(\"hippo\", \"i\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hippo\", \"i\") expected \, got {result}")
        failed += 1

    # Test 4
    result = start_word(\"hippo\", \"ix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hippo\", \"ix\") expected \, got {result}")
        failed += 1

    # Test 5
    result = start_word(\"h\", \"ix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"h\", \"ix\") expected \, got {result}")
        failed += 1

    # Test 6
    result = start_word(\"\", \"i\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"\", \"i\") expected \, got {result}")
        failed += 1

    # Test 7
    result = start_word(\"hip\", \"zi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hip\", \"zi\") expected \, got {result}")
        failed += 1

    # Test 8
    result = start_word(\"hip\", \"zip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hip\", \"zip\") expected \, got {result}")
        failed += 1

    # Test 9
    result = start_word(\"hip\", \"zig\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hip\", \"zig\") expected \, got {result}")
        failed += 1

    # Test 10
    result = start_word(\"h\", \"z\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"h\", \"z\") expected \, got {result}")
        failed += 1

    # Test 11
    result = start_word(\"hippo\", \"xippo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hippo\", \"xippo\") expected \, got {result}")
        failed += 1

    # Test 12
    result = start_word(\"hippo\", \"xyz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hippo\", \"xyz\") expected \, got {result}")
        failed += 1

    # Test 13
    result = start_word(\"hippo\", \"hip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"hippo\", \"hip\") expected \, got {result}")
        failed += 1

    # Test 14
    result = start_word(\"kitten\", \"cit\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"kitten\", \"cit\") expected \, got {result}")
        failed += 1

    # Test 15
    result = start_word(\"kit\", \"cit\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: start_word(\"kit\", \"cit\") expected \, got {result}")
        failed += 1

    print(f"start_word: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
