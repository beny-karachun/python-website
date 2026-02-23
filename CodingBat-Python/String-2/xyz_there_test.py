"""
Tester for xyzThere - CodingBat Python
14 test cases
"""

from xyz_there import xyz_there


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = xyz_there(\"abcxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"abcxyz\") expected True, got {result}")
        failed += 1

    # Test 2
    result = xyz_there(\"abc.xyz\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"abc.xyz\") expected False, got {result}")
        failed += 1

    # Test 3
    result = xyz_there(\"xyz.abc\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"xyz.abc\") expected True, got {result}")
        failed += 1

    # Test 4
    result = xyz_there(\"abcxy\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"abcxy\") expected False, got {result}")
        failed += 1

    # Test 5
    result = xyz_there(\"xyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"xyz\") expected True, got {result}")
        failed += 1

    # Test 6
    result = xyz_there(\"xy\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"xy\") expected False, got {result}")
        failed += 1

    # Test 7
    result = xyz_there(\"x\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"x\") expected False, got {result}")
        failed += 1

    # Test 8
    result = xyz_there(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"\") expected False, got {result}")
        failed += 1

    # Test 9
    result = xyz_there(\"abc.xyzxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"abc.xyzxyz\") expected True, got {result}")
        failed += 1

    # Test 10
    result = xyz_there(\"abc.xxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"abc.xxyz\") expected True, got {result}")
        failed += 1

    # Test 11
    result = xyz_there(\".xyz\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\".xyz\") expected False, got {result}")
        failed += 1

    # Test 12
    result = xyz_there(\"12.xyz\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"12.xyz\") expected False, got {result}")
        failed += 1

    # Test 13
    result = xyz_there(\"12xyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"12xyz\") expected True, got {result}")
        failed += 1

    # Test 14
    result = xyz_there(\"1.xyz.xyz2.xyz\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_there(\"1.xyz.xyz2.xyz\") expected False, got {result}")
        failed += 1

    print(f"xyz_there: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
