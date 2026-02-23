"""
Tester for has271 - CodingBat Python
3 test cases
"""

from has271 import has271


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = has271([1, 2, 7, 1])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has271([1, 2, 7, 1]) expected True, got {result}")
        failed += 1

    # Test 2
    result = has271([1, 2, 8, 1])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has271([1, 2, 8, 1]) expected False, got {result}")
        failed += 1

    # Test 3
    result = has271([2, 7, 1])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has271([2, 7, 1]) expected True, got {result}")
        failed += 1

    print(f"has271: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
