"""
Tester for in1020 - CodingBat Python
7 test cases
"""

from in1020 import in1020


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = in1020(12, 99)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1020(12, 99) expected True, got {result}")
        failed += 1

    # Test 2
    result = in1020(21, 12)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1020(21, 12) expected True, got {result}")
        failed += 1

    # Test 3
    result = in1020(8, 99)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1020(8, 99) expected False, got {result}")
        failed += 1

    # Test 4
    result = in1020(99, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1020(99, 10) expected True, got {result}")
        failed += 1

    # Test 5
    result = in1020(20, 20)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1020(20, 20) expected True, got {result}")
        failed += 1

    # Test 6
    result = in1020(21, 21)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1020(21, 21) expected False, got {result}")
        failed += 1

    # Test 7
    result = in1020(9, 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1020(9, 9) expected False, got {result}")
        failed += 1

    print(f"in1020: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
