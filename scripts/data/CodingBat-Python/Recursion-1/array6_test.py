"""
Tester for array6 - CodingBat Python
3 test cases
"""

from array6 import array6


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = array6([1, 6, 4], 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: array6([1, 6, 4], 0) expected True, got {result}")
        failed += 1

    # Test 2
    result = array6([1, 4], 0)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: array6([1, 4], 0) expected False, got {result}")
        failed += 1

    # Test 3
    result = array6([6], 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: array6([6], 0) expected True, got {result}")
        failed += 1

    print(f"array6: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
