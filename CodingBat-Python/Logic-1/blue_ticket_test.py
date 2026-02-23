"""
Tester for blueTicket - CodingBat Python
12 test cases
"""

from blue_ticket import blue_ticket


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = blue_ticket(9, 1, 0)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(9, 1, 0) expected 10, got {result}")
        failed += 1

    # Test 2
    result = blue_ticket(9, 2, 0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(9, 2, 0) expected 0, got {result}")
        failed += 1

    # Test 3
    result = blue_ticket(6, 1, 4)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(6, 1, 4) expected 10, got {result}")
        failed += 1

    # Test 4
    result = blue_ticket(6, 1, 5)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(6, 1, 5) expected 0, got {result}")
        failed += 1

    # Test 5
    result = blue_ticket(10, 0, 0)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(10, 0, 0) expected 10, got {result}")
        failed += 1

    # Test 6
    result = blue_ticket(15, 0, 5)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(15, 0, 5) expected 5, got {result}")
        failed += 1

    # Test 7
    result = blue_ticket(5, 15, 5)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(5, 15, 5) expected 10, got {result}")
        failed += 1

    # Test 8
    result = blue_ticket(4, 11, 1)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(4, 11, 1) expected 5, got {result}")
        failed += 1

    # Test 9
    result = blue_ticket(13, 2, 3)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(13, 2, 3) expected 5, got {result}")
        failed += 1

    # Test 10
    result = blue_ticket(8, 4, 3)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(8, 4, 3) expected 0, got {result}")
        failed += 1

    # Test 11
    result = blue_ticket(8, 4, 2)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(8, 4, 2) expected 10, got {result}")
        failed += 1

    # Test 12
    result = blue_ticket(8, 4, 1)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: blue_ticket(8, 4, 1) expected 0, got {result}")
        failed += 1

    print(f"blue_ticket: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
