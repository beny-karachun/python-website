"""
Tester for xyBalance - CodingBat Python
18 test cases
"""

from xy_balance import xy_balance


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = xy_balance(\"aaxbby\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"aaxbby\") expected True, got {result}")
        failed += 1

    # Test 2
    result = xy_balance(\"aaxbb\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"aaxbb\") expected False, got {result}")
        failed += 1

    # Test 3
    result = xy_balance(\"yaaxbb\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"yaaxbb\") expected False, got {result}")
        failed += 1

    # Test 4
    result = xy_balance(\"yaaxbby\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"yaaxbby\") expected True, got {result}")
        failed += 1

    # Test 5
    result = xy_balance(\"xaxxbby\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"xaxxbby\") expected True, got {result}")
        failed += 1

    # Test 6
    result = xy_balance(\"xaxxbbyx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"xaxxbbyx\") expected False, got {result}")
        failed += 1

    # Test 7
    result = xy_balance(\"xxbxy\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"xxbxy\") expected True, got {result}")
        failed += 1

    # Test 8
    result = xy_balance(\"xxbx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"xxbx\") expected False, got {result}")
        failed += 1

    # Test 9
    result = xy_balance(\"bbb\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"bbb\") expected True, got {result}")
        failed += 1

    # Test 10
    result = xy_balance(\"bxbb\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"bxbb\") expected False, got {result}")
        failed += 1

    # Test 11
    result = xy_balance(\"bxyb\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"bxyb\") expected True, got {result}")
        failed += 1

    # Test 12
    result = xy_balance(\"xy\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"xy\") expected True, got {result}")
        failed += 1

    # Test 13
    result = xy_balance(\"y\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"y\") expected True, got {result}")
        failed += 1

    # Test 14
    result = xy_balance(\"x\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"x\") expected False, got {result}")
        failed += 1

    # Test 15
    result = xy_balance(\"\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"\") expected True, got {result}")
        failed += 1

    # Test 16
    result = xy_balance(\"yxyxyxyx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"yxyxyxyx\") expected False, got {result}")
        failed += 1

    # Test 17
    result = xy_balance(\"yxyxyxyxy\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"yxyxyxyxy\") expected True, got {result}")
        failed += 1

    # Test 18
    result = xy_balance(\"12xabxxydxyxyzz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xy_balance(\"12xabxxydxyxyzz\") expected True, got {result}")
        failed += 1

    print(f"xy_balance: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
