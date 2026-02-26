"""
Tester for frontAgain - CodingBat Python
11 test cases
"""

from front_again import front_again


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = front_again(\"edited\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: front_again(\"edited\") expected True, got {result}")
        failed += 1

    # Test 2
    result = front_again(\"edit\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: front_again(\"edit\") expected False, got {result}")
        failed += 1

    # Test 3
    result = front_again(\"ed\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: front_again(\"ed\") expected True, got {result}")
        failed += 1

    # Test 4
    result = front_again(\"jj\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: front_again(\"jj\") expected True, got {result}")
        failed += 1

    # Test 5
    result = front_again(\"jjj\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: front_again(\"jjj\") expected True, got {result}")
        failed += 1

    # Test 6
    result = front_again(\"jjjj\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: front_again(\"jjjj\") expected True, got {result}")
        failed += 1

    # Test 7
    result = front_again(\"jjjk\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: front_again(\"jjjk\") expected False, got {result}")
        failed += 1

    # Test 8
    result = front_again(\"x\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: front_again(\"x\") expected False, got {result}")
        failed += 1

    # Test 9
    result = front_again(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: front_again(\"\") expected False, got {result}")
        failed += 1

    # Test 10
    result = front_again(\"java\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: front_again(\"java\") expected False, got {result}")
        failed += 1

    # Test 11
    result = front_again(\"javaja\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: front_again(\"javaja\") expected True, got {result}")
        failed += 1

    print(f"front_again: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
