"""
Tester for splitArray - CodingBat Python
3 test cases
"""

from split_array import split_array


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = split_array([2, 2])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: split_array([2, 2]) expected True, got {result}")
        failed += 1

    # Test 2
    result = split_array([2, 3])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: split_array([2, 3]) expected False, got {result}")
        failed += 1

    # Test 3
    result = split_array([5, 2, 3])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: split_array([5, 2, 3]) expected True, got {result}")
        failed += 1

    print(f"split_array: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
