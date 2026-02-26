"""
Tester for in1To10 - CodingBat Python
15 test cases
"""

from in1_to10 import in1_to10


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = in1_to10(5, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(5, False) expected True, got {result}")
        failed += 1

    # Test 2
    result = in1_to10(11, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1_to10(11, False) expected False, got {result}")
        failed += 1

    # Test 3
    result = in1_to10(11, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(11, True) expected True, got {result}")
        failed += 1

    # Test 4
    result = in1_to10(10, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(10, False) expected True, got {result}")
        failed += 1

    # Test 5
    result = in1_to10(10, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(10, True) expected True, got {result}")
        failed += 1

    # Test 6
    result = in1_to10(9, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(9, False) expected True, got {result}")
        failed += 1

    # Test 7
    result = in1_to10(9, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1_to10(9, True) expected False, got {result}")
        failed += 1

    # Test 8
    result = in1_to10(1, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(1, False) expected True, got {result}")
        failed += 1

    # Test 9
    result = in1_to10(1, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(1, True) expected True, got {result}")
        failed += 1

    # Test 10
    result = in1_to10(0, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1_to10(0, False) expected False, got {result}")
        failed += 1

    # Test 11
    result = in1_to10(0, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(0, True) expected True, got {result}")
        failed += 1

    # Test 12
    result = in1_to10(-1, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1_to10(-1, False) expected False, got {result}")
        failed += 1

    # Test 13
    result = in1_to10(-1, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(-1, True) expected True, got {result}")
        failed += 1

    # Test 14
    result = in1_to10(99, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: in1_to10(99, False) expected False, got {result}")
        failed += 1

    # Test 15
    result = in1_to10(-99, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: in1_to10(-99, True) expected True, got {result}")
        failed += 1

    print(f"in1_to10: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
