"""
Tester for starOut - CodingBat Python
18 test cases
"""

from star_out import star_out


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = star_out(\"ab*cd\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"ab*cd\") expected \, got {result}")
        failed += 1

    # Test 2
    result = star_out(\"ab**cd\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"ab**cd\") expected \, got {result}")
        failed += 1

    # Test 3
    result = star_out(\"sm*eilly\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"sm*eilly\") expected \, got {result}")
        failed += 1

    # Test 4
    result = star_out(\"sm*eil*ly\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"sm*eil*ly\") expected \, got {result}")
        failed += 1

    # Test 5
    result = star_out(\"sm**eil*ly\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"sm**eil*ly\") expected \, got {result}")
        failed += 1

    # Test 6
    result = star_out(\"sm***eil*ly\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"sm***eil*ly\") expected \, got {result}")
        failed += 1

    # Test 7
    result = star_out(\"stringy*\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"stringy*\") expected \, got {result}")
        failed += 1

    # Test 8
    result = star_out(\"*stringy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"*stringy\") expected \, got {result}")
        failed += 1

    # Test 9
    result = star_out(\"*str*in*gy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"*str*in*gy\") expected \, got {result}")
        failed += 1

    # Test 10
    result = star_out(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"abc\") expected \, got {result}")
        failed += 1

    # Test 11
    result = star_out(\"a*bc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"a*bc\") expected \, got {result}")
        failed += 1

    # Test 12
    result = star_out(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"ab\") expected \, got {result}")
        failed += 1

    # Test 13
    result = star_out(\"a*b\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"a*b\") expected \, got {result}")
        failed += 1

    # Test 14
    result = star_out(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"a\") expected \, got {result}")
        failed += 1

    # Test 15
    result = star_out(\"a*\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"a*\") expected \, got {result}")
        failed += 1

    # Test 16
    result = star_out(\"*a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"*a\") expected \, got {result}")
        failed += 1

    # Test 17
    result = star_out(\"*\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"*\") expected \, got {result}")
        failed += 1

    # Test 18
    result = star_out(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: star_out(\"\") expected \, got {result}")
        failed += 1

    print(f"star_out: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
