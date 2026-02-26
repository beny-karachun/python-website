"""
Tester for equalIsNot - CodingBat Python
10 test cases
"""

from equal_is_not import equal_is_not


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = equal_is_not(\"This is not\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"This is not\") expected False, got {result}")
        failed += 1

    # Test 2
    result = equal_is_not(\"This is notnot\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"This is notnot\") expected True, got {result}")
        failed += 1

    # Test 3
    result = equal_is_not(\"noisxxnotyynotxisi\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"noisxxnotyynotxisi\") expected True, got {result}")
        failed += 1

    # Test 4
    result = equal_is_not(\"noisxxnotyynotxsi\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"noisxxnotyynotxsi\") expected False, got {result}")
        failed += 1

    # Test 5
    result = equal_is_not(\"xxxyyyzzzintint\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"xxxyyyzzzintint\") expected True, got {result}")
        failed += 1

    # Test 6
    result = equal_is_not(\"\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"\") expected True, got {result}")
        failed += 1

    # Test 7
    result = equal_is_not(\"isisnotnot\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"isisnotnot\") expected True, got {result}")
        failed += 1

    # Test 8
    result = equal_is_not(\"isisnotno7Not\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"isisnotno7Not\") expected False, got {result}")
        failed += 1

    # Test 9
    result = equal_is_not(\"isnotis\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"isnotis\") expected False, got {result}")
        failed += 1

    # Test 10
    result = equal_is_not(\"mis3notpotbotis\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: equal_is_not(\"mis3notpotbotis\") expected False, got {result}")
        failed += 1

    print(f"equal_is_not: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
