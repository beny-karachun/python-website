"""
Tester for left2 - CodingBat Python
8 test cases
"""

from left2 import left2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = left2(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = left2(\"java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"java\") expected \, got {result}")
        failed += 1

    # Test 3
    result = left2(\"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"Hi\") expected \, got {result}")
        failed += 1

    # Test 4
    result = left2(\"code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"code\") expected \, got {result}")
        failed += 1

    # Test 5
    result = left2(\"cat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"cat\") expected \, got {result}")
        failed += 1

    # Test 6
    result = left2(\"12345\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"12345\") expected \, got {result}")
        failed += 1

    # Test 7
    result = left2(\"Chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"Chocolate\") expected \, got {result}")
        failed += 1

    # Test 8
    result = left2(\"bricks\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: left2(\"bricks\") expected \, got {result}")
        failed += 1

    print(f"left2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
