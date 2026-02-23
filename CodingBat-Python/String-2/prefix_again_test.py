"""
Tester for prefixAgain - CodingBat Python
12 test cases
"""

from prefix_again import prefix_again


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = prefix_again(\"abXYabc\", 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"abXYabc\", 1) expected True, got {result}")
        failed += 1

    # Test 2
    result = prefix_again(\"abXYabc\", 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"abXYabc\", 2) expected True, got {result}")
        failed += 1

    # Test 3
    result = prefix_again(\"abXYabc\", 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"abXYabc\", 3) expected False, got {result}")
        failed += 1

    # Test 4
    result = prefix_again(\"xyzxyxyxy\", 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"xyzxyxyxy\", 2) expected True, got {result}")
        failed += 1

    # Test 5
    result = prefix_again(\"xyzxyxyxy\", 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"xyzxyxyxy\", 3) expected False, got {result}")
        failed += 1

    # Test 6
    result = prefix_again(\"Hi12345Hi6789Hi10\", 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"Hi12345Hi6789Hi10\", 1) expected True, got {result}")
        failed += 1

    # Test 7
    result = prefix_again(\"Hi12345Hi6789Hi10\", 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"Hi12345Hi6789Hi10\", 2) expected True, got {result}")
        failed += 1

    # Test 8
    result = prefix_again(\"Hi12345Hi6789Hi10\", 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"Hi12345Hi6789Hi10\", 3) expected True, got {result}")
        failed += 1

    # Test 9
    result = prefix_again(\"Hi12345Hi6789Hi10\", 4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"Hi12345Hi6789Hi10\", 4) expected False, got {result}")
        failed += 1

    # Test 10
    result = prefix_again(\"a\", 1)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"a\", 1) expected False, got {result}")
        failed += 1

    # Test 11
    result = prefix_again(\"aa\", 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"aa\", 1) expected True, got {result}")
        failed += 1

    # Test 12
    result = prefix_again(\"ab\", 1)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: prefix_again(\"ab\", 1) expected False, got {result}")
        failed += 1

    print(f"prefix_again: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
