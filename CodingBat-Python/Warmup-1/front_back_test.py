"""
Tester for frontBack - CodingBat Python
8 test cases
"""

from front_back import front_back


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = front_back(\"code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"code\") expected \, got {result}")
        failed += 1

    # Test 2
    result = front_back(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"a\") expected \, got {result}")
        failed += 1

    # Test 3
    result = front_back(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"ab\") expected \, got {result}")
        failed += 1

    # Test 4
    result = front_back(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"abc\") expected \, got {result}")
        failed += 1

    # Test 5
    result = front_back(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = front_back(\"Chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"Chocolate\") expected \, got {result}")
        failed += 1

    # Test 7
    result = front_back(\"aavJ\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"aavJ\") expected \, got {result}")
        failed += 1

    # Test 8
    result = front_back(\"hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_back(\"hello\") expected \, got {result}")
        failed += 1

    print(f"front_back: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
