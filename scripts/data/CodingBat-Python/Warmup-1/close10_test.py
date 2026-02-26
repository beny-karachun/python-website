"""
Tester for close10 - CodingBat Python
11 test cases
"""

from close10 import close10


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = close10(8, 13)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: close10(8, 13) expected 8, got {result}")
        failed += 1

    # Test 2
    result = close10(13, 8)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: close10(13, 8) expected 8, got {result}")
        failed += 1

    # Test 3
    result = close10(13, 7)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: close10(13, 7) expected 0, got {result}")
        failed += 1

    # Test 4
    result = close10(7, 13)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: close10(7, 13) expected 0, got {result}")
        failed += 1

    # Test 5
    result = close10(9, 13)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: close10(9, 13) expected 9, got {result}")
        failed += 1

    # Test 6
    result = close10(13, 8)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: close10(13, 8) expected 8, got {result}")
        failed += 1

    # Test 7
    result = close10(10, 12)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: close10(10, 12) expected 10, got {result}")
        failed += 1

    # Test 8
    result = close10(11, 10)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: close10(11, 10) expected 10, got {result}")
        failed += 1

    # Test 9
    result = close10(5, 21)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: close10(5, 21) expected 5, got {result}")
        failed += 1

    # Test 10
    result = close10(0, 20)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: close10(0, 20) expected 0, got {result}")
        failed += 1

    # Test 11
    result = close10(10, 10)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: close10(10, 10) expected 0, got {result}")
        failed += 1

    print(f"close10: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
