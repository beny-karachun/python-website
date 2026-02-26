"""
Tester for extraEnd - CodingBat Python
5 test cases
"""

from extra_end import extra_end


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = extra_end(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_end(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = extra_end(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_end(\"ab\") expected \, got {result}")
        failed += 1

    # Test 3
    result = extra_end(\"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_end(\"Hi\") expected \, got {result}")
        failed += 1

    # Test 4
    result = extra_end(\"Candy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_end(\"Candy\") expected \, got {result}")
        failed += 1

    # Test 5
    result = extra_end(\"Code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_end(\"Code\") expected \, got {result}")
        failed += 1

    print(f"extra_end: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
