"""
Tester for hasBad - CodingBat Python
10 test cases
"""

from has_bad import has_bad


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = has_bad(\"badxx\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"badxx\") expected True, got {result}")
        failed += 1

    # Test 2
    result = has_bad(\"xbadxx\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"xbadxx\") expected True, got {result}")
        failed += 1

    # Test 3
    result = has_bad(\"xxbadxx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"xxbadxx\") expected False, got {result}")
        failed += 1

    # Test 4
    result = has_bad(\"code\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"code\") expected False, got {result}")
        failed += 1

    # Test 5
    result = has_bad(\"bad\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"bad\") expected True, got {result}")
        failed += 1

    # Test 6
    result = has_bad(\"ba\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"ba\") expected False, got {result}")
        failed += 1

    # Test 7
    result = has_bad(\"xba\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"xba\") expected False, got {result}")
        failed += 1

    # Test 8
    result = has_bad(\"xbad\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"xbad\") expected True, got {result}")
        failed += 1

    # Test 9
    result = has_bad(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"\") expected False, got {result}")
        failed += 1

    # Test 10
    result = has_bad(\"badyy\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: has_bad(\"badyy\") expected True, got {result}")
        failed += 1

    print(f"has_bad: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
