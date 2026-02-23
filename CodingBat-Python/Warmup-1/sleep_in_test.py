"""
Tester for sleepIn - CodingBat Python
4 test cases
"""

from sleep_in import sleep_in


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = sleep_in(False, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: sleep_in(False, False) expected True, got {result}")
        failed += 1

    # Test 2
    result = sleep_in(True, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: sleep_in(True, False) expected False, got {result}")
        failed += 1

    # Test 3
    result = sleep_in(False, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: sleep_in(False, True) expected True, got {result}")
        failed += 1

    # Test 4
    result = sleep_in(True, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: sleep_in(True, True) expected True, got {result}")
        failed += 1

    print(f"sleep_in: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
