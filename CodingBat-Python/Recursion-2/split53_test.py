"""
Tester for split53 - CodingBat Python
3 test cases
"""

from split53 import split53


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = split53([1, 1])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: split53([1, 1]) expected True, got {result}")
        failed += 1

    # Test 2
    result = split53([1, 1, 1])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: split53([1, 1, 1]) expected False, got {result}")
        failed += 1

    # Test 3
    result = split53([2, 4, 2])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: split53([2, 4, 2]) expected True, got {result}")
        failed += 1

    print(f"split53: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
