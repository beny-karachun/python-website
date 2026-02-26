"""
Tester for withoutX - CodingBat Python
12 test cases
"""

from without_x import without_x


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = without_x(\"xHix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"xHix\") expected \, got {result}")
        failed += 1

    # Test 2
    result = without_x(\"xHi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"xHi\") expected \, got {result}")
        failed += 1

    # Test 3
    result = without_x(\"Hxix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"Hxix\") expected \, got {result}")
        failed += 1

    # Test 4
    result = without_x(\"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"Hi\") expected \, got {result}")
        failed += 1

    # Test 5
    result = without_x(\"xxHi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"xxHi\") expected \, got {result}")
        failed += 1

    # Test 6
    result = without_x(\"Hix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"Hix\") expected \, got {result}")
        failed += 1

    # Test 7
    result = without_x(\"xaxbx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"xaxbx\") expected \, got {result}")
        failed += 1

    # Test 8
    result = without_x(\"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"xx\") expected \, got {result}")
        failed += 1

    # Test 9
    result = without_x(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"x\") expected \, got {result}")
        failed += 1

    # Test 10
    result = without_x(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"\") expected \, got {result}")
        failed += 1

    # Test 11
    result = without_x(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 12
    result = without_x(\"Hexllo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x(\"Hexllo\") expected \, got {result}")
        failed += 1

    print(f"without_x: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
