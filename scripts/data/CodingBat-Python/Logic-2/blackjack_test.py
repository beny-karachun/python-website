"""
Tester for blackjack - CodingBat Python
15 test cases
"""

from blackjack import blackjack


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = blackjack(19, 21)
    if result == 21:
        passed += 1
    else:
        print(f"FAIL: blackjack(19, 21) expected 21, got {result}")
        failed += 1

    # Test 2
    result = blackjack(21, 19)
    if result == 21:
        passed += 1
    else:
        print(f"FAIL: blackjack(21, 19) expected 21, got {result}")
        failed += 1

    # Test 3
    result = blackjack(19, 22)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: blackjack(19, 22) expected 19, got {result}")
        failed += 1

    # Test 4
    result = blackjack(22, 19)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: blackjack(22, 19) expected 19, got {result}")
        failed += 1

    # Test 5
    result = blackjack(22, 50)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: blackjack(22, 50) expected 0, got {result}")
        failed += 1

    # Test 6
    result = blackjack(22, 22)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: blackjack(22, 22) expected 0, got {result}")
        failed += 1

    # Test 7
    result = blackjack(33, 1)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: blackjack(33, 1) expected 1, got {result}")
        failed += 1

    # Test 8
    result = blackjack(1, 2)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: blackjack(1, 2) expected 2, got {result}")
        failed += 1

    # Test 9
    result = blackjack(34, 33)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: blackjack(34, 33) expected 0, got {result}")
        failed += 1

    # Test 10
    result = blackjack(17, 19)
    if result == 19:
        passed += 1
    else:
        print(f"FAIL: blackjack(17, 19) expected 19, got {result}")
        failed += 1

    # Test 11
    result = blackjack(18, 17)
    if result == 18:
        passed += 1
    else:
        print(f"FAIL: blackjack(18, 17) expected 18, got {result}")
        failed += 1

    # Test 12
    result = blackjack(16, 23)
    if result == 16:
        passed += 1
    else:
        print(f"FAIL: blackjack(16, 23) expected 16, got {result}")
        failed += 1

    # Test 13
    result = blackjack(3, 4)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: blackjack(3, 4) expected 4, got {result}")
        failed += 1

    # Test 14
    result = blackjack(3, 2)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: blackjack(3, 2) expected 3, got {result}")
        failed += 1

    # Test 15
    result = blackjack(21, 20)
    if result == 21:
        passed += 1
    else:
        print(f"FAIL: blackjack(21, 20) expected 21, got {result}")
        failed += 1

    print(f"blackjack: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
