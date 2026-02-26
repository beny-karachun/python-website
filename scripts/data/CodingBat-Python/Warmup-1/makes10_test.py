"""
Tester for makes10 - CodingBat Python
9 test cases
"""

from makes10 import makes10


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = makes10(9, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: makes10(9, 10) expected True, got {result}")
        failed += 1

    # Test 2
    result = makes10(9, 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: makes10(9, 9) expected False, got {result}")
        failed += 1

    # Test 3
    result = makes10(1, 9)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: makes10(1, 9) expected True, got {result}")
        failed += 1

    # Test 4
    result = makes10(10, 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: makes10(10, 1) expected True, got {result}")
        failed += 1

    # Test 5
    result = makes10(10, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: makes10(10, 10) expected True, got {result}")
        failed += 1

    # Test 6
    result = makes10(8, 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: makes10(8, 2) expected True, got {result}")
        failed += 1

    # Test 7
    result = makes10(8, 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: makes10(8, 3) expected False, got {result}")
        failed += 1

    # Test 8
    result = makes10(10, 42)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: makes10(10, 42) expected True, got {result}")
        failed += 1

    # Test 9
    result = makes10(12, -2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: makes10(12, -2) expected True, got {result}")
        failed += 1

    print(f"makes10: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
