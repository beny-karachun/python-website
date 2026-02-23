"""
Tester for plusOut - CodingBat Python
10 test cases
"""

from plus_out import plus_out


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = plus_out(\"12xy34\", \"xy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"12xy34\", \"xy\") expected \, got {result}")
        failed += 1

    # Test 2
    result = plus_out(\"12xy34\", \"1\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"12xy34\", \"1\") expected \, got {result}")
        failed += 1

    # Test 3
    result = plus_out(\"12xy34xyabcxy\", \"xy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"12xy34xyabcxy\", \"xy\") expected \, got {result}")
        failed += 1

    # Test 4
    result = plus_out(\"abXYabcXYZ\", \"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"abXYabcXYZ\", \"ab\") expected \, got {result}")
        failed += 1

    # Test 5
    result = plus_out(\"abXYabcXYZ\", \"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"abXYabcXYZ\", \"abc\") expected \, got {result}")
        failed += 1

    # Test 6
    result = plus_out(\"abXYabcXYZ\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"abXYabcXYZ\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 7
    result = plus_out(\"abXYxyzXYZ\", \"XYZ\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"abXYxyzXYZ\", \"XYZ\") expected \, got {result}")
        failed += 1

    # Test 8
    result = plus_out(\"--++ab\", \"++\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"--++ab\", \"++\") expected \, got {result}")
        failed += 1

    # Test 9
    result = plus_out(\"aaxxxxbb\", \"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"aaxxxxbb\", \"xx\") expected \, got {result}")
        failed += 1

    # Test 10
    result = plus_out(\"123123\", \"3\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: plus_out(\"123123\", \"3\") expected \, got {result}")
        failed += 1

    print(f"plus_out: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
