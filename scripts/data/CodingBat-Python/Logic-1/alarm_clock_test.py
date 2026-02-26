"""
Tester for alarmClock - CodingBat Python
9 test cases
"""

from alarm_clock import alarm_clock


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = alarm_clock(1, False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(1, False) expected \, got {result}")
        failed += 1

    # Test 2
    result = alarm_clock(5, False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(5, False) expected \, got {result}")
        failed += 1

    # Test 3
    result = alarm_clock(0, False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(0, False) expected \, got {result}")
        failed += 1

    # Test 4
    result = alarm_clock(6, False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(6, False) expected \, got {result}")
        failed += 1

    # Test 5
    result = alarm_clock(0, True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(0, True) expected \, got {result}")
        failed += 1

    # Test 6
    result = alarm_clock(6, True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(6, True) expected \, got {result}")
        failed += 1

    # Test 7
    result = alarm_clock(1, True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(1, True) expected \, got {result}")
        failed += 1

    # Test 8
    result = alarm_clock(3, True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(3, True) expected \, got {result}")
        failed += 1

    # Test 9
    result = alarm_clock(5, True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alarm_clock(5, True) expected \, got {result}")
        failed += 1

    print(f"alarm_clock: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
