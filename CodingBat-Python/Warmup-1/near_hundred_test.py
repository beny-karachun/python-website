"""
Tester for nearHundred - CodingBat Python
19 test cases
"""

from near_hundred import near_hundred


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = near_hundred(93)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(93) expected True, got {result}")
        failed += 1

    # Test 2
    result = near_hundred(90)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(90) expected True, got {result}")
        failed += 1

    # Test 3
    result = near_hundred(89)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(89) expected False, got {result}")
        failed += 1

    # Test 4
    result = near_hundred(110)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(110) expected True, got {result}")
        failed += 1

    # Test 5
    result = near_hundred(111)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(111) expected False, got {result}")
        failed += 1

    # Test 6
    result = near_hundred(121)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(121) expected False, got {result}")
        failed += 1

    # Test 7
    result = near_hundred(-101)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(-101) expected False, got {result}")
        failed += 1

    # Test 8
    result = near_hundred(-209)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(-209) expected False, got {result}")
        failed += 1

    # Test 9
    result = near_hundred(190)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(190) expected True, got {result}")
        failed += 1

    # Test 10
    result = near_hundred(209)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(209) expected True, got {result}")
        failed += 1

    # Test 11
    result = near_hundred(0)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(0) expected False, got {result}")
        failed += 1

    # Test 12
    result = near_hundred(5)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(5) expected False, got {result}")
        failed += 1

    # Test 13
    result = near_hundred(-50)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(-50) expected False, got {result}")
        failed += 1

    # Test 14
    result = near_hundred(191)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(191) expected True, got {result}")
        failed += 1

    # Test 15
    result = near_hundred(189)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(189) expected False, got {result}")
        failed += 1

    # Test 16
    result = near_hundred(200)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(200) expected True, got {result}")
        failed += 1

    # Test 17
    result = near_hundred(210)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: near_hundred(210) expected True, got {result}")
        failed += 1

    # Test 18
    result = near_hundred(211)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(211) expected False, got {result}")
        failed += 1

    # Test 19
    result = near_hundred(290)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: near_hundred(290) expected False, got {result}")
        failed += 1

    print(f"near_hundred: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
