"""
Tester for stringX - CodingBat Python
8 test cases
"""

from string_x import string_x


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_x(\"xxHxix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"xxHxix\") expected \, got {result}")
        failed += 1

    # Test 2
    result = string_x(\"abxxxcd\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"abxxxcd\") expected \, got {result}")
        failed += 1

    # Test 3
    result = string_x(\"xabxxxcdx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"xabxxxcdx\") expected \, got {result}")
        failed += 1

    # Test 4
    result = string_x(\"xKittenx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"xKittenx\") expected \, got {result}")
        failed += 1

    # Test 5
    result = string_x(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 6
    result = string_x(\"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"xx\") expected \, got {result}")
        failed += 1

    # Test 7
    result = string_x(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"x\") expected \, got {result}")
        failed += 1

    # Test 8
    result = string_x(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_x(\"\") expected \, got {result}")
        failed += 1

    print(f"string_x: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
