"""
Tester for splitOdd10 - CodingBat Python
3 test cases
"""

from split_odd10 import split_odd10


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = split_odd10([5, 5, 5])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: split_odd10([5, 5, 5]) expected True, got {result}")
        failed += 1

    # Test 2
    result = split_odd10([5, 5, 6])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: split_odd10([5, 5, 6]) expected False, got {result}")
        failed += 1

    # Test 3
    result = split_odd10([5, 5, 6, 1])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: split_odd10([5, 5, 6, 1]) expected True, got {result}")
        failed += 1

    print(f"split_odd10: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
