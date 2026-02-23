"""
Tester for backAround - CodingBat Python
6 test cases
"""

from back_around import back_around


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = back_around(\"cat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: back_around(\"cat\") expected \, got {result}")
        failed += 1

    # Test 2
    result = back_around(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: back_around(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 3
    result = back_around(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: back_around(\"a\") expected \, got {result}")
        failed += 1

    # Test 4
    result = back_around(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: back_around(\"abc\") expected \, got {result}")
        failed += 1

    # Test 5
    result = back_around(\"read\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: back_around(\"read\") expected \, got {result}")
        failed += 1

    # Test 6
    result = back_around(\"boo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: back_around(\"boo\") expected \, got {result}")
        failed += 1

    print(f"back_around: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
