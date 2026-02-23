"""
Tester for gHappy - CodingBat Python
12 test cases
"""

from g_happy import g_happy


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = g_happy(\"xxggxx\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"xxggxx\") expected True, got {result}")
        failed += 1

    # Test 2
    result = g_happy(\"xxgxx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"xxgxx\") expected False, got {result}")
        failed += 1

    # Test 3
    result = g_happy(\"xxggyygxx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"xxggyygxx\") expected False, got {result}")
        failed += 1

    # Test 4
    result = g_happy(\"g\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"g\") expected False, got {result}")
        failed += 1

    # Test 5
    result = g_happy(\"gg\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"gg\") expected True, got {result}")
        failed += 1

    # Test 6
    result = g_happy(\"\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"\") expected True, got {result}")
        failed += 1

    # Test 7
    result = g_happy(\"xxgggxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"xxgggxyz\") expected True, got {result}")
        failed += 1

    # Test 8
    result = g_happy(\"xxgggxyg\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"xxgggxyg\") expected False, got {result}")
        failed += 1

    # Test 9
    result = g_happy(\"xxgggxygg\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"xxgggxygg\") expected True, got {result}")
        failed += 1

    # Test 10
    result = g_happy(\"mgm\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"mgm\") expected False, got {result}")
        failed += 1

    # Test 11
    result = g_happy(\"mggm\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"mggm\") expected True, got {result}")
        failed += 1

    # Test 12
    result = g_happy(\"yyygggxyy\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: g_happy(\"yyygggxyy\") expected True, got {result}")
        failed += 1

    print(f"g_happy: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
