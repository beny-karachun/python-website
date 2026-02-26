"""
Tester for stringTimes - CodingBat Python
10 test cases
"""

from string_times import string_times


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_times(\"Hi\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"Hi\", 2) expected \, got {result}")
        failed += 1

    # Test 2
    result = string_times(\"Hi\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"Hi\", 3) expected \, got {result}")
        failed += 1

    # Test 3
    result = string_times(\"Hi\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"Hi\", 1) expected \, got {result}")
        failed += 1

    # Test 4
    result = string_times(\"Hi\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"Hi\", 0) expected \, got {result}")
        failed += 1

    # Test 5
    result = string_times(\"Hi\", 5)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"Hi\", 5) expected \, got {result}")
        failed += 1

    # Test 6
    result = string_times(\"Oh Boy!\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"Oh Boy!\", 2) expected \, got {result}")
        failed += 1

    # Test 7
    result = string_times(\"x\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"x\", 4) expected \, got {result}")
        failed += 1

    # Test 8
    result = string_times(\"\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"\", 4) expected \, got {result}")
        failed += 1

    # Test 9
    result = string_times(\"code\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"code\", 2) expected \, got {result}")
        failed += 1

    # Test 10
    result = string_times(\"code\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_times(\"code\", 3) expected \, got {result}")
        failed += 1

    print(f"string_times: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
