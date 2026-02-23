"""
Tester for array123 - CodingBat Python
3 test cases
"""

from array123 import array123


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = array123([1, 1, 2, 3, 1])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: array123([1, 1, 2, 3, 1]) expected True, got {result}")
        failed += 1

    # Test 2
    result = array123([1, 1, 2, 4, 1])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: array123([1, 1, 2, 4, 1]) expected False, got {result}")
        failed += 1

    # Test 3
    result = array123([1, 1, 2, 1, 2, 3])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: array123([1, 1, 2, 1, 2, 3]) expected True, got {result}")
        failed += 1

    print(f"array123: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
