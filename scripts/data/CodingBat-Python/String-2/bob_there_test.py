"""
Tester for bobThere - CodingBat Python
13 test cases
"""

from bob_there import bob_there


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = bob_there(\"abcbob\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"abcbob\") expected True, got {result}")
        failed += 1

    # Test 2
    result = bob_there(\"b9b\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"b9b\") expected True, got {result}")
        failed += 1

    # Test 3
    result = bob_there(\"bac\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"bac\") expected False, got {result}")
        failed += 1

    # Test 4
    result = bob_there(\"bbb\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"bbb\") expected True, got {result}")
        failed += 1

    # Test 5
    result = bob_there(\"abcdefb\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"abcdefb\") expected False, got {result}")
        failed += 1

    # Test 6
    result = bob_there(\"123abcbcdbabxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"123abcbcdbabxyz\") expected True, got {result}")
        failed += 1

    # Test 7
    result = bob_there(\"b12\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"b12\") expected False, got {result}")
        failed += 1

    # Test 8
    result = bob_there(\"b1b\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"b1b\") expected True, got {result}")
        failed += 1

    # Test 9
    result = bob_there(\"b12b1b\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"b12b1b\") expected True, got {result}")
        failed += 1

    # Test 10
    result = bob_there(\"bbc\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"bbc\") expected False, got {result}")
        failed += 1

    # Test 11
    result = bob_there(\"bbb\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"bbb\") expected True, got {result}")
        failed += 1

    # Test 12
    result = bob_there(\"bb\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"bb\") expected False, got {result}")
        failed += 1

    # Test 13
    result = bob_there(\"b\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: bob_there(\"b\") expected False, got {result}")
        failed += 1

    print(f"bob_there: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
