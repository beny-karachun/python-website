"""
Tester for array667 - CodingBat Python
3 test cases
"""

from array667 import array667


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = array667([6, 6, 2])
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: array667([6, 6, 2]) expected 1, got {result}")
        failed += 1

    # Test 2
    result = array667([6, 6, 2, 6])
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: array667([6, 6, 2, 6]) expected 1, got {result}")
        failed += 1

    # Test 3
    result = array667([6, 7, 2, 6])
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: array667([6, 7, 2, 6]) expected 1, got {result}")
        failed += 1

    print(f"array667: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
