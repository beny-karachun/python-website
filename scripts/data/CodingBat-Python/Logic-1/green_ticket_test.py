"""
Tester for greenTicket - CodingBat Python
12 test cases
"""

from green_ticket import green_ticket


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = green_ticket(1, 2, 3)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: green_ticket(1, 2, 3) expected 0, got {result}")
        failed += 1

    # Test 2
    result = green_ticket(2, 2, 2)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: green_ticket(2, 2, 2) expected 20, got {result}")
        failed += 1

    # Test 3
    result = green_ticket(1, 1, 2)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: green_ticket(1, 1, 2) expected 10, got {result}")
        failed += 1

    # Test 4
    result = green_ticket(2, 1, 1)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: green_ticket(2, 1, 1) expected 10, got {result}")
        failed += 1

    # Test 5
    result = green_ticket(1, 2, 1)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: green_ticket(1, 2, 1) expected 10, got {result}")
        failed += 1

    # Test 6
    result = green_ticket(3, 2, 1)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: green_ticket(3, 2, 1) expected 0, got {result}")
        failed += 1

    # Test 7
    result = green_ticket(0, 0, 0)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: green_ticket(0, 0, 0) expected 20, got {result}")
        failed += 1

    # Test 8
    result = green_ticket(2, 0, 0)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: green_ticket(2, 0, 0) expected 10, got {result}")
        failed += 1

    # Test 9
    result = green_ticket(0, 9, 10)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: green_ticket(0, 9, 10) expected 0, got {result}")
        failed += 1

    # Test 10
    result = green_ticket(0, 10, 0)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: green_ticket(0, 10, 0) expected 10, got {result}")
        failed += 1

    # Test 11
    result = green_ticket(9, 9, 9)
    if result == 20:
        passed += 1
    else:
        print(f"FAIL: green_ticket(9, 9, 9) expected 20, got {result}")
        failed += 1

    # Test 12
    result = green_ticket(9, 0, 9)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: green_ticket(9, 0, 9) expected 10, got {result}")
        failed += 1

    print(f"green_ticket: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
