"""
Tester for comboString - CodingBat Python
11 test cases
"""

from combo_string import combo_string


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = combo_string(\"Hello\", \"hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"Hello\", \"hi\") expected \, got {result}")
        failed += 1

    # Test 2
    result = combo_string(\"hi\", \"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"hi\", \"Hello\") expected \, got {result}")
        failed += 1

    # Test 3
    result = combo_string(\"aaa\", \"b\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"aaa\", \"b\") expected \, got {result}")
        failed += 1

    # Test 4
    result = combo_string(\"b\", \"aaa\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"b\", \"aaa\") expected \, got {result}")
        failed += 1

    # Test 5
    result = combo_string(\"aaa\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"aaa\", \"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = combo_string(\"\", \"bb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"\", \"bb\") expected \, got {result}")
        failed += 1

    # Test 7
    result = combo_string(\"aaa\", \"1234\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"aaa\", \"1234\") expected \, got {result}")
        failed += 1

    # Test 8
    result = combo_string(\"aaa\", \"bb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"aaa\", \"bb\") expected \, got {result}")
        failed += 1

    # Test 9
    result = combo_string(\"a\", \"bb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"a\", \"bb\") expected \, got {result}")
        failed += 1

    # Test 10
    result = combo_string(\"bb\", \"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"bb\", \"a\") expected \, got {result}")
        failed += 1

    # Test 11
    result = combo_string(\"xyz\", \"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: combo_string(\"xyz\", \"ab\") expected \, got {result}")
        failed += 1

    print(f"combo_string: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
