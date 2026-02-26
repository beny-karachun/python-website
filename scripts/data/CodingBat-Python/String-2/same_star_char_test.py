"""
Tester for sameStarChar - CodingBat Python
16 test cases
"""

from same_star_char import same_star_char


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = same_star_char(\"xy*yzz\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"xy*yzz\") expected True, got {result}")
        failed += 1

    # Test 2
    result = same_star_char(\"xy*zzz\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"xy*zzz\") expected False, got {result}")
        failed += 1

    # Test 3
    result = same_star_char(\"*xa*az\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"*xa*az\") expected True, got {result}")
        failed += 1

    # Test 4
    result = same_star_char(\"*xa*bz\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"*xa*bz\") expected False, got {result}")
        failed += 1

    # Test 5
    result = same_star_char(\"*xa*a*\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"*xa*a*\") expected True, got {result}")
        failed += 1

    # Test 6
    result = same_star_char(\"\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"\") expected True, got {result}")
        failed += 1

    # Test 7
    result = same_star_char(\"*xa*a*a\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"*xa*a*a\") expected True, got {result}")
        failed += 1

    # Test 8
    result = same_star_char(\"*xa*a*b\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"*xa*a*b\") expected False, got {result}")
        failed += 1

    # Test 9
    result = same_star_char(\"*12*2*2\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"*12*2*2\") expected True, got {result}")
        failed += 1

    # Test 10
    result = same_star_char(\"12*2*3*\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"12*2*3*\") expected False, got {result}")
        failed += 1

    # Test 11
    result = same_star_char(\"abcDEF\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"abcDEF\") expected True, got {result}")
        failed += 1

    # Test 12
    result = same_star_char(\"XY*YYYY*Z*\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"XY*YYYY*Z*\") expected False, got {result}")
        failed += 1

    # Test 13
    result = same_star_char(\"XY*YYYY*Y*\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"XY*YYYY*Y*\") expected True, got {result}")
        failed += 1

    # Test 14
    result = same_star_char(\"12*2*3*\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"12*2*3*\") expected False, got {result}")
        failed += 1

    # Test 15
    result = same_star_char(\"*\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"*\") expected True, got {result}")
        failed += 1

    # Test 16
    result = same_star_char(\"**\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: same_star_char(\"**\") expected True, got {result}")
        failed += 1

    print(f"same_star_char: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
