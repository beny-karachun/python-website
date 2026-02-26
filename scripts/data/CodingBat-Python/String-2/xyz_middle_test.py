"""
Tester for xyzMiddle - CodingBat Python
21 test cases
"""

from xyz_middle import xyz_middle


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = xyz_middle(\"AAxyzBB\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AAxyzBB\") expected True, got {result}")
        failed += 1

    # Test 2
    result = xyz_middle(\"AxyzBB\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AxyzBB\") expected True, got {result}")
        failed += 1

    # Test 3
    result = xyz_middle(\"AxyzBBB\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AxyzBBB\") expected False, got {result}")
        failed += 1

    # Test 4
    result = xyz_middle(\"AxyzBBBB\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AxyzBBBB\") expected False, got {result}")
        failed += 1

    # Test 5
    result = xyz_middle(\"AAAxyzB\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AAAxyzB\") expected False, got {result}")
        failed += 1

    # Test 6
    result = xyz_middle(\"AAAxyzBB\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AAAxyzBB\") expected True, got {result}")
        failed += 1

    # Test 7
    result = xyz_middle(\"AAAAxyzBB\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AAAAxyzBB\") expected False, got {result}")
        failed += 1

    # Test 8
    result = xyz_middle(\"AAAAAxyzBBB\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AAAAAxyzBBB\") expected False, got {result}")
        failed += 1

    # Test 9
    result = xyz_middle(\"1x345xyz12x4\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"1x345xyz12x4\") expected True, got {result}")
        failed += 1

    # Test 10
    result = xyz_middle(\"xyzAxyzBBB\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyzAxyzBBB\") expected True, got {result}")
        failed += 1

    # Test 11
    result = xyz_middle(\"xyzAxyzBxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyzAxyzBxyz\") expected True, got {result}")
        failed += 1

    # Test 12
    result = xyz_middle(\"xyzxyzAxyzBxyzxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyzxyzAxyzBxyzxyz\") expected True, got {result}")
        failed += 1

    # Test 13
    result = xyz_middle(\"xyzxyzxyzBxyzxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyzxyzxyzBxyzxyz\") expected True, got {result}")
        failed += 1

    # Test 14
    result = xyz_middle(\"xyzxyzAxyzxyzxyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyzxyzAxyzxyzxyz\") expected True, got {result}")
        failed += 1

    # Test 15
    result = xyz_middle(\"xyzxyzAxyzxyzxy\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyzxyzAxyzxyzxy\") expected False, got {result}")
        failed += 1

    # Test 16
    result = xyz_middle(\"AxyzxyzBB\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"AxyzxyzBB\") expected False, got {result}")
        failed += 1

    # Test 17
    result = xyz_middle(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"\") expected False, got {result}")
        failed += 1

    # Test 18
    result = xyz_middle(\"x\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"x\") expected False, got {result}")
        failed += 1

    # Test 19
    result = xyz_middle(\"xy\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xy\") expected False, got {result}")
        failed += 1

    # Test 20
    result = xyz_middle(\"xyz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyz\") expected True, got {result}")
        failed += 1

    # Test 21
    result = xyz_middle(\"xyzz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: xyz_middle(\"xyzz\") expected True, got {result}")
        failed += 1

    print(f"xyz_middle: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
