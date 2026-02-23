"""
Tester for array11 - CodingBat Python
3 test cases
"""

from array11 import array11


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = array11([1, 2, 11], 0)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: array11([1, 2, 11], 0) expected 1, got {result}")
        failed += 1

    # Test 2
    result = array11([11, 11], 0)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: array11([11, 11], 0) expected 2, got {result}")
        failed += 1

    # Test 3
    result = array11([1, 2, 3, 4], 0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: array11([1, 2, 3, 4], 0) expected 0, got {result}")
        failed += 1

    print(f"array11: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
