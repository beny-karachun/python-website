"""
Tester for factorial - CodingBat Python
9 test cases
"""

from factorial import factorial


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = factorial(1)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: factorial(1) expected 1, got {result}")
        failed += 1

    # Test 2
    result = factorial(2)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: factorial(2) expected 2, got {result}")
        failed += 1

    # Test 3
    result = factorial(3)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: factorial(3) expected 6, got {result}")
        failed += 1

    # Test 4
    result = factorial(4)
    if result == 24:
        passed += 1
    else:
        print(f"FAIL: factorial(4) expected 24, got {result}")
        failed += 1

    # Test 5
    result = factorial(5)
    if result == 120:
        passed += 1
    else:
        print(f"FAIL: factorial(5) expected 120, got {result}")
        failed += 1

    # Test 6
    result = factorial(6)
    if result == 720:
        passed += 1
    else:
        print(f"FAIL: factorial(6) expected 720, got {result}")
        failed += 1

    # Test 7
    result = factorial(7)
    if result == 5040:
        passed += 1
    else:
        print(f"FAIL: factorial(7) expected 5040, got {result}")
        failed += 1

    # Test 8
    result = factorial(8)
    if result == 40320:
        passed += 1
    else:
        print(f"FAIL: factorial(8) expected 40320, got {result}")
        failed += 1

    # Test 9
    result = factorial(12)
    if result == 479001600:
        passed += 1
    else:
        print(f"FAIL: factorial(12) expected 479001600, got {result}")
        failed += 1

    print(f"factorial: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
