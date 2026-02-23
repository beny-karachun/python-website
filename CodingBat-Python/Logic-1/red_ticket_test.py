"""
Tester for redTicket - CodingBat Python
11 test cases
"""

from red_ticket import red_ticket


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = red_ticket(2, 2, 2)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: red_ticket(2, 2, 2) expected 10, got {result}")
        failed += 1

    # Test 2
    result = red_ticket(2, 2, 1)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: red_ticket(2, 2, 1) expected 0, got {result}")
        failed += 1

    # Test 3
    result = red_ticket(0, 0, 0)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: red_ticket(0, 0, 0) expected 5, got {result}")
        failed += 1

    # Test 4
    result = red_ticket(2, 0, 0)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: red_ticket(2, 0, 0) expected 1, got {result}")
        failed += 1

    # Test 5
    result = red_ticket(1, 1, 1)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: red_ticket(1, 1, 1) expected 5, got {result}")
        failed += 1

    # Test 6
    result = red_ticket(1, 2, 1)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: red_ticket(1, 2, 1) expected 0, got {result}")
        failed += 1

    # Test 7
    result = red_ticket(1, 2, 0)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: red_ticket(1, 2, 0) expected 1, got {result}")
        failed += 1

    # Test 8
    result = red_ticket(0, 2, 2)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: red_ticket(0, 2, 2) expected 1, got {result}")
        failed += 1

    # Test 9
    result = red_ticket(1, 2, 2)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: red_ticket(1, 2, 2) expected 1, got {result}")
        failed += 1

    # Test 10
    result = red_ticket(0, 2, 0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: red_ticket(0, 2, 0) expected 0, got {result}")
        failed += 1

    # Test 11
    result = red_ticket(1, 1, 2)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: red_ticket(1, 1, 2) expected 0, got {result}")
        failed += 1

    print(f"red_ticket: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
