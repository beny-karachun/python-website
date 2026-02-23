"""
Tester for makeChocolate - CodingBat Python
24 test cases
"""

from make_chocolate import make_chocolate


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = make_chocolate(4, 1, 9)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(4, 1, 9) expected 4, got {result}")
        failed += 1

    # Test 2
    result = make_chocolate(4, 1, 10)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(4, 1, 10) expected -1, got {result}")
        failed += 1

    # Test 3
    result = make_chocolate(4, 1, 7)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(4, 1, 7) expected 2, got {result}")
        failed += 1

    # Test 4
    result = make_chocolate(6, 2, 7)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 2, 7) expected 2, got {result}")
        failed += 1

    # Test 5
    result = make_chocolate(4, 1, 5)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(4, 1, 5) expected 0, got {result}")
        failed += 1

    # Test 6
    result = make_chocolate(4, 1, 4)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(4, 1, 4) expected 4, got {result}")
        failed += 1

    # Test 7
    result = make_chocolate(5, 4, 9)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(5, 4, 9) expected 4, got {result}")
        failed += 1

    # Test 8
    result = make_chocolate(9, 3, 18)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(9, 3, 18) expected 3, got {result}")
        failed += 1

    # Test 9
    result = make_chocolate(3, 1, 9)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(3, 1, 9) expected -1, got {result}")
        failed += 1

    # Test 10
    result = make_chocolate(1, 2, 7)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(1, 2, 7) expected -1, got {result}")
        failed += 1

    # Test 11
    result = make_chocolate(1, 2, 6)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(1, 2, 6) expected 1, got {result}")
        failed += 1

    # Test 12
    result = make_chocolate(1, 2, 5)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(1, 2, 5) expected 0, got {result}")
        failed += 1

    # Test 13
    result = make_chocolate(6, 1, 10)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 1, 10) expected 5, got {result}")
        failed += 1

    # Test 14
    result = make_chocolate(6, 1, 11)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 1, 11) expected 6, got {result}")
        failed += 1

    # Test 15
    result = make_chocolate(6, 1, 12)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 1, 12) expected -1, got {result}")
        failed += 1

    # Test 16
    result = make_chocolate(6, 1, 13)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 1, 13) expected -1, got {result}")
        failed += 1

    # Test 17
    result = make_chocolate(6, 2, 10)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 2, 10) expected 0, got {result}")
        failed += 1

    # Test 18
    result = make_chocolate(6, 2, 11)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 2, 11) expected 1, got {result}")
        failed += 1

    # Test 19
    result = make_chocolate(6, 2, 12)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(6, 2, 12) expected 2, got {result}")
        failed += 1

    # Test 20
    result = make_chocolate(60, 100, 550)
    if result == 50:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(60, 100, 550) expected 50, got {result}")
        failed += 1

    # Test 21
    result = make_chocolate(1000, 1000000, 5000006)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(1000, 1000000, 5000006) expected 6, got {result}")
        failed += 1

    # Test 22
    result = make_chocolate(7, 1, 12)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(7, 1, 12) expected 7, got {result}")
        failed += 1

    # Test 23
    result = make_chocolate(7, 1, 13)
    if result == -1:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(7, 1, 13) expected -1, got {result}")
        failed += 1

    # Test 24
    result = make_chocolate(7, 2, 13)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: make_chocolate(7, 2, 13) expected 3, got {result}")
        failed += 1

    print(f"make_chocolate: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
