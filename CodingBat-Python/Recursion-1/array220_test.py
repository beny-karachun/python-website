"""
Tester for array220 - CodingBat Python
3 test cases
"""

from array220 import array220


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = array220([1, 2, 20], 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: array220([1, 2, 20], 0) expected True, got {result}")
        failed += 1

    # Test 2
    result = array220([3, 30], 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: array220([3, 30], 0) expected True, got {result}")
        failed += 1

    # Test 3
    result = array220([3], 0)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: array220([3], 0) expected False, got {result}")
        failed += 1

    print(f"array220: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
