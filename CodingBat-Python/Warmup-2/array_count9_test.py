"""
Tester for arrayCount9 - CodingBat Python
3 test cases
"""

from array_count9 import array_count9


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = array_count9([1, 2, 9])
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: array_count9([1, 2, 9]) expected 1, got {result}")
        failed += 1

    # Test 2
    result = array_count9([1, 9, 9])
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: array_count9([1, 9, 9]) expected 2, got {result}")
        failed += 1

    # Test 3
    result = array_count9([1, 9, 9, 3, 9])
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: array_count9([1, 9, 9, 3, 9]) expected 3, got {result}")
        failed += 1

    print(f"array_count9: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
