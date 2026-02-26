"""
Tester for makeBricks - CodingBat Python
29 test cases
"""

from make_bricks import make_bricks


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = make_bricks(3, 1, 8)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(3, 1, 8) expected True, got {result}")
        failed += 1

    # Test 2
    result = make_bricks(3, 1, 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(3, 1, 9) expected False, got {result}")
        failed += 1

    # Test 3
    result = make_bricks(3, 2, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(3, 2, 10) expected True, got {result}")
        failed += 1

    # Test 4
    result = make_bricks(3, 2, 8)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(3, 2, 8) expected True, got {result}")
        failed += 1

    # Test 5
    result = make_bricks(3, 2, 9)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(3, 2, 9) expected False, got {result}")
        failed += 1

    # Test 6
    result = make_bricks(6, 1, 11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(6, 1, 11) expected True, got {result}")
        failed += 1

    # Test 7
    result = make_bricks(6, 0, 11)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(6, 0, 11) expected False, got {result}")
        failed += 1

    # Test 8
    result = make_bricks(1, 4, 11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(1, 4, 11) expected True, got {result}")
        failed += 1

    # Test 9
    result = make_bricks(0, 3, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(0, 3, 10) expected True, got {result}")
        failed += 1

    # Test 10
    result = make_bricks(1, 4, 12)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(1, 4, 12) expected False, got {result}")
        failed += 1

    # Test 11
    result = make_bricks(3, 1, 7)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(3, 1, 7) expected True, got {result}")
        failed += 1

    # Test 12
    result = make_bricks(1, 1, 7)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(1, 1, 7) expected False, got {result}")
        failed += 1

    # Test 13
    result = make_bricks(2, 1, 7)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(2, 1, 7) expected True, got {result}")
        failed += 1

    # Test 14
    result = make_bricks(7, 1, 11)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(7, 1, 11) expected True, got {result}")
        failed += 1

    # Test 15
    result = make_bricks(7, 1, 8)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(7, 1, 8) expected True, got {result}")
        failed += 1

    # Test 16
    result = make_bricks(7, 1, 13)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(7, 1, 13) expected False, got {result}")
        failed += 1

    # Test 17
    result = make_bricks(43, 1, 46)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(43, 1, 46) expected True, got {result}")
        failed += 1

    # Test 18
    result = make_bricks(40, 1, 46)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(40, 1, 46) expected False, got {result}")
        failed += 1

    # Test 19
    result = make_bricks(40, 2, 47)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(40, 2, 47) expected True, got {result}")
        failed += 1

    # Test 20
    result = make_bricks(40, 2, 50)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(40, 2, 50) expected True, got {result}")
        failed += 1

    # Test 21
    result = make_bricks(40, 2, 52)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(40, 2, 52) expected False, got {result}")
        failed += 1

    # Test 22
    result = make_bricks(22, 2, 33)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(22, 2, 33) expected False, got {result}")
        failed += 1

    # Test 23
    result = make_bricks(0, 2, 10)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(0, 2, 10) expected True, got {result}")
        failed += 1

    # Test 24
    result = make_bricks(1000000, 1000, 1000100)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(1000000, 1000, 1000100) expected True, got {result}")
        failed += 1

    # Test 25
    result = make_bricks(2, 1000000, 100003)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(2, 1000000, 100003) expected False, got {result}")
        failed += 1

    # Test 26
    result = make_bricks(20, 0, 19)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(20, 0, 19) expected True, got {result}")
        failed += 1

    # Test 27
    result = make_bricks(20, 0, 21)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(20, 0, 21) expected False, got {result}")
        failed += 1

    # Test 28
    result = make_bricks(20, 4, 51)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: make_bricks(20, 4, 51) expected False, got {result}")
        failed += 1

    # Test 29
    result = make_bricks(20, 4, 39)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: make_bricks(20, 4, 39) expected True, got {result}")
        failed += 1

    print(f"make_bricks: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
