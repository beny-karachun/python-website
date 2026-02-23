"""
Tester for monkeyTrouble - CodingBat Python
4 test cases
"""

from monkey_trouble import monkey_trouble


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = monkey_trouble(True, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: monkey_trouble(True, True) expected True, got {result}")
        failed += 1

    # Test 2
    result = monkey_trouble(False, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: monkey_trouble(False, False) expected True, got {result}")
        failed += 1

    # Test 3
    result = monkey_trouble(True, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: monkey_trouble(True, False) expected False, got {result}")
        failed += 1

    # Test 4
    result = monkey_trouble(False, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: monkey_trouble(False, True) expected False, got {result}")
        failed += 1

    print(f"monkey_trouble: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
