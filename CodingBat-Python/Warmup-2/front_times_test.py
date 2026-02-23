"""
Tester for frontTimes - CodingBat Python
7 test cases
"""

from front_times import front_times


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = front_times(\"Chocolate\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_times(\"Chocolate\", 2) expected \, got {result}")
        failed += 1

    # Test 2
    result = front_times(\"Chocolate\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_times(\"Chocolate\", 3) expected \, got {result}")
        failed += 1

    # Test 3
    result = front_times(\"Abc\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_times(\"Abc\", 3) expected \, got {result}")
        failed += 1

    # Test 4
    result = front_times(\"Ab\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_times(\"Ab\", 4) expected \, got {result}")
        failed += 1

    # Test 5
    result = front_times(\"A\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_times(\"A\", 4) expected \, got {result}")
        failed += 1

    # Test 6
    result = front_times(\"\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_times(\"\", 4) expected \, got {result}")
        failed += 1

    # Test 7
    result = front_times(\"Abc\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front_times(\"Abc\", 0) expected \, got {result}")
        failed += 1

    print(f"front_times: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
