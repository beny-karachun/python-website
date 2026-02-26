"""
Tester for repeatEnd - CodingBat Python
8 test cases
"""

from repeat_end import repeat_end


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = repeat_end(\"Hello\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"Hello\", 3) expected \, got {result}")
        failed += 1

    # Test 2
    result = repeat_end(\"Hello\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"Hello\", 2) expected \, got {result}")
        failed += 1

    # Test 3
    result = repeat_end(\"Hello\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"Hello\", 1) expected \, got {result}")
        failed += 1

    # Test 4
    result = repeat_end(\"Hello\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"Hello\", 0) expected \, got {result}")
        failed += 1

    # Test 5
    result = repeat_end(\"abc\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"abc\", 3) expected \, got {result}")
        failed += 1

    # Test 6
    result = repeat_end(\"1234\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"1234\", 2) expected \, got {result}")
        failed += 1

    # Test 7
    result = repeat_end(\"1234\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"1234\", 3) expected \, got {result}")
        failed += 1

    # Test 8
    result = repeat_end(\"\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_end(\"\", 0) expected \, got {result}")
        failed += 1

    print(f"repeat_end: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
