"""
Tester for arrayFront9 - CodingBat Python
3 test cases
"""

from array_front9 import array_front9


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = array_front9([1, 2, 9, 3, 4])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: array_front9([1, 2, 9, 3, 4]) expected True, got {result}")
        failed += 1

    # Test 2
    result = array_front9([1, 2, 3, 4, 9])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: array_front9([1, 2, 3, 4, 9]) expected False, got {result}")
        failed += 1

    # Test 3
    result = array_front9([1, 2, 3, 4, 5])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: array_front9([1, 2, 3, 4, 5]) expected False, got {result}")
        failed += 1

    print(f"array_front9: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
