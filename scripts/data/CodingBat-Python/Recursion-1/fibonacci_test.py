"""
Tester for fibonacci - CodingBat Python
8 test cases
"""

from fibonacci import fibonacci


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = fibonacci(0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: fibonacci(0) expected 0, got {result}")
        failed += 1

    # Test 2
    result = fibonacci(1)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: fibonacci(1) expected 1, got {result}")
        failed += 1

    # Test 3
    result = fibonacci(2)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: fibonacci(2) expected 1, got {result}")
        failed += 1

    # Test 4
    result = fibonacci(3)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: fibonacci(3) expected 2, got {result}")
        failed += 1

    # Test 5
    result = fibonacci(4)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: fibonacci(4) expected 3, got {result}")
        failed += 1

    # Test 6
    result = fibonacci(5)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: fibonacci(5) expected 5, got {result}")
        failed += 1

    # Test 7
    result = fibonacci(6)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: fibonacci(6) expected 8, got {result}")
        failed += 1

    # Test 8
    result = fibonacci(7)
    if result == 13:
        passed += 1
    else:
        print(f"FAIL: fibonacci(7) expected 13, got {result}")
        failed += 1

    print(f"fibonacci: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
