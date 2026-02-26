"""
Tester for front22 - CodingBat Python
7 test cases
"""

from front22 import front22


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = front22(\"kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front22(\"kitten\") expected \, got {result}")
        failed += 1

    # Test 2
    result = front22(\"Ha\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front22(\"Ha\") expected \, got {result}")
        failed += 1

    # Test 3
    result = front22(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front22(\"abc\") expected \, got {result}")
        failed += 1

    # Test 4
    result = front22(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front22(\"ab\") expected \, got {result}")
        failed += 1

    # Test 5
    result = front22(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front22(\"a\") expected \, got {result}")
        failed += 1

    # Test 6
    result = front22(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front22(\"\") expected \, got {result}")
        failed += 1

    # Test 7
    result = front22(\"Logic\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front22(\"Logic\") expected \, got {result}")
        failed += 1

    print(f"front22: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
