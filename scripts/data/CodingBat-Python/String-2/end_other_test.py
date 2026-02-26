"""
Tester for endOther - CodingBat Python
14 test cases
"""

from end_other import end_other


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = end_other(\"Hiabc\", \"abc\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"Hiabc\", \"abc\") expected True, got {result}")
        failed += 1

    # Test 2
    result = end_other(\"AbC\", \"HiaBc\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"AbC\", \"HiaBc\") expected True, got {result}")
        failed += 1

    # Test 3
    result = end_other(\"abc\", \"abXabc\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"abc\", \"abXabc\") expected True, got {result}")
        failed += 1

    # Test 4
    result = end_other(\"Hiabc\", \"abcd\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: end_other(\"Hiabc\", \"abcd\") expected False, got {result}")
        failed += 1

    # Test 5
    result = end_other(\"Hiabc\", \"bc\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"Hiabc\", \"bc\") expected True, got {result}")
        failed += 1

    # Test 6
    result = end_other(\"Hiabcx\", \"bc\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: end_other(\"Hiabcx\", \"bc\") expected False, got {result}")
        failed += 1

    # Test 7
    result = end_other(\"abc\", \"abc\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"abc\", \"abc\") expected True, got {result}")
        failed += 1

    # Test 8
    result = end_other(\"xyz\", \"12xyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"xyz\", \"12xyz\") expected True, got {result}")
        failed += 1

    # Test 9
    result = end_other(\"yz\", \"12xz\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: end_other(\"yz\", \"12xz\") expected False, got {result}")
        failed += 1

    # Test 10
    result = end_other(\"Z\", \"12xz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"Z\", \"12xz\") expected True, got {result}")
        failed += 1

    # Test 11
    result = end_other(\"12\", \"12\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"12\", \"12\") expected True, got {result}")
        failed += 1

    # Test 12
    result = end_other(\"abcXYZ\", \"abcDEF\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: end_other(\"abcXYZ\", \"abcDEF\") expected False, got {result}")
        failed += 1

    # Test 13
    result = end_other(\"ab\", \"ab12\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: end_other(\"ab\", \"ab12\") expected False, got {result}")
        failed += 1

    # Test 14
    result = end_other(\"ab\", \"12ab\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: end_other(\"ab\", \"12ab\") expected True, got {result}")
        failed += 1

    print(f"end_other: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
