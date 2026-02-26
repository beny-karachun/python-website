"""
Tester for mixString - CodingBat Python
13 test cases
"""

from mix_string import mix_string


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = mix_string(\"abc\", \"xyz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"abc\", \"xyz\") expected \, got {result}")
        failed += 1

    # Test 2
    result = mix_string(\"Hi\", \"There\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"Hi\", \"There\") expected \, got {result}")
        failed += 1

    # Test 3
    result = mix_string(\"xxxx\", \"There\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"xxxx\", \"There\") expected \, got {result}")
        failed += 1

    # Test 4
    result = mix_string(\"xxx\", \"X\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"xxx\", \"X\") expected \, got {result}")
        failed += 1

    # Test 5
    result = mix_string(\"2/\", \"27 around\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"2/\", \"27 around\") expected \, got {result}")
        failed += 1

    # Test 6
    result = mix_string(\"\", \"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"\", \"Hello\") expected \, got {result}")
        failed += 1

    # Test 7
    result = mix_string(\"Abc\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"Abc\", \"\") expected \, got {result}")
        failed += 1

    # Test 8
    result = mix_string(\"\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"\", \"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = mix_string(\"a\", \"b\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"a\", \"b\") expected \, got {result}")
        failed += 1

    # Test 10
    result = mix_string(\"ax\", \"b\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"ax\", \"b\") expected \, got {result}")
        failed += 1

    # Test 11
    result = mix_string(\"a\", \"bx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"a\", \"bx\") expected \, got {result}")
        failed += 1

    # Test 12
    result = mix_string(\"So\", \"Long\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"So\", \"Long\") expected \, got {result}")
        failed += 1

    # Test 13
    result = mix_string(\"Long\", \"So\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mix_string(\"Long\", \"So\") expected \, got {result}")
        failed += 1

    print(f"mix_string: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
