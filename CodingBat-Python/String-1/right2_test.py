"""
Tester for right2 - CodingBat Python
6 test cases
"""

from right2 import right2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = right2(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: right2(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = right2(\"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: right2(\"java\") expected \, got {result}")
        failed += 1

    # Test 3
    result = right2(\"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: right2(\"Hi\") expected \, got {result}")
        failed += 1

    # Test 4
    result = right2(\"code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: right2(\"code\") expected \, got {result}")
        failed += 1

    # Test 5
    result = right2(\"cat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: right2(\"cat\") expected \, got {result}")
        failed += 1

    # Test 6
    result = right2(\"12345\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: right2(\"12345\") expected \, got {result}")
        failed += 1

    print(f"right2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
