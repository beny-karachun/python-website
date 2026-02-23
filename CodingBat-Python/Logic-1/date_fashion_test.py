"""
Tester for dateFashion - CodingBat Python
12 test cases
"""

from date_fashion import date_fashion


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = date_fashion(5, 10)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: date_fashion(5, 10) expected 2, got {result}")
        failed += 1

    # Test 2
    result = date_fashion(5, 2)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: date_fashion(5, 2) expected 0, got {result}")
        failed += 1

    # Test 3
    result = date_fashion(5, 5)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: date_fashion(5, 5) expected 1, got {result}")
        failed += 1

    # Test 4
    result = date_fashion(3, 3)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: date_fashion(3, 3) expected 1, got {result}")
        failed += 1

    # Test 5
    result = date_fashion(10, 2)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: date_fashion(10, 2) expected 0, got {result}")
        failed += 1

    # Test 6
    result = date_fashion(2, 9)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: date_fashion(2, 9) expected 0, got {result}")
        failed += 1

    # Test 7
    result = date_fashion(9, 9)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: date_fashion(9, 9) expected 2, got {result}")
        failed += 1

    # Test 8
    result = date_fashion(10, 5)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: date_fashion(10, 5) expected 2, got {result}")
        failed += 1

    # Test 9
    result = date_fashion(2, 2)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: date_fashion(2, 2) expected 0, got {result}")
        failed += 1

    # Test 10
    result = date_fashion(3, 7)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: date_fashion(3, 7) expected 1, got {result}")
        failed += 1

    # Test 11
    result = date_fashion(2, 7)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: date_fashion(2, 7) expected 0, got {result}")
        failed += 1

    # Test 12
    result = date_fashion(6, 2)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: date_fashion(6, 2) expected 0, got {result}")
        failed += 1

    print(f"date_fashion: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
