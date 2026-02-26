"""
Tester for diff21 - CodingBat Python
12 test cases
"""

from diff21 import diff21


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = diff21(19)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: diff21(19) expected 2, got {result}")
        failed += 1

    # Test 2
    result = diff21(10)
    if result == 11:
        passed += 1
    else:
        print(f"FAIL: diff21(10) expected 11, got {result}")
        failed += 1

    # Test 3
    result = diff21(21)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: diff21(21) expected 0, got {result}")
        failed += 1

    # Test 4
    result = diff21(22)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: diff21(22) expected 2, got {result}")
        failed += 1

    # Test 5
    result = diff21(25)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: diff21(25) expected 8, got {result}")
        failed += 1

    # Test 6
    result = diff21(30)
    if result == 18:
        passed += 1
    else:
        print(f"FAIL: diff21(30) expected 18, got {result}")
        failed += 1

    # Test 7
    result = diff21(0)
    if result == 21:
        passed += 1
    else:
        print(f"FAIL: diff21(0) expected 21, got {result}")
        failed += 1

    # Test 8
    result = diff21(1)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: diff21(1) expected 20, got {result}")
        failed += 1

    # Test 9
    result = diff21(2)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: diff21(2) expected 19, got {result}")
        failed += 1

    # Test 10
    result = diff21(-1)
    if result == 22:
        passed += 1
    else:
        print(f"FAIL: diff21(-1) expected 22, got {result}")
        failed += 1

    # Test 11
    result = diff21(-2)
    if result == 23:
        passed += 1
    else:
        print(f"FAIL: diff21(-2) expected 23, got {result}")
        failed += 1

    # Test 12
    result = diff21(50)
    if result == 58:
        passed += 1
    else:
        print(f"FAIL: diff21(50) expected 58, got {result}")
        failed += 1

    print(f"diff21: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
