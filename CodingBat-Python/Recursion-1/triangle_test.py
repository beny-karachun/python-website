"""
Tester for triangle - CodingBat Python
8 test cases
"""

from triangle import triangle


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = triangle(0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: triangle(0) expected 0, got {result}")
        failed += 1

    # Test 2
    result = triangle(1)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: triangle(1) expected 1, got {result}")
        failed += 1

    # Test 3
    result = triangle(2)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: triangle(2) expected 3, got {result}")
        failed += 1

    # Test 4
    result = triangle(3)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: triangle(3) expected 6, got {result}")
        failed += 1

    # Test 5
    result = triangle(4)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: triangle(4) expected 10, got {result}")
        failed += 1

    # Test 6
    result = triangle(5)
    if result == 15:
        passed += 1
    else:
        print(f"FAIL: triangle(5) expected 15, got {result}")
        failed += 1

    # Test 7
    result = triangle(6)
    if result == 21:
        passed += 1
    else:
        print(f"FAIL: triangle(6) expected 21, got {result}")
        failed += 1

    # Test 8
    result = triangle(7)
    if result == 28:
        passed += 1
    else:
        print(f"FAIL: triangle(7) expected 28, got {result}")
        failed += 1

    print(f"triangle: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
