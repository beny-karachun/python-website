"""
Tester for seeColor - CodingBat Python
11 test cases
"""

from see_color import see_color


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = see_color(\"redxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"redxx\") expected \, got {result}")
        failed += 1

    # Test 2
    result = see_color(\"xxred\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"xxred\") expected \, got {result}")
        failed += 1

    # Test 3
    result = see_color(\"blueTimes\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"blueTimes\") expected \, got {result}")
        failed += 1

    # Test 4
    result = see_color(\"NoColor\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"NoColor\") expected \, got {result}")
        failed += 1

    # Test 5
    result = see_color(\"red\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"red\") expected \, got {result}")
        failed += 1

    # Test 6
    result = see_color(\"re\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"re\") expected \, got {result}")
        failed += 1

    # Test 7
    result = see_color(\"blu\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"blu\") expected \, got {result}")
        failed += 1

    # Test 8
    result = see_color(\"blue\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"blue\") expected \, got {result}")
        failed += 1

    # Test 9
    result = see_color(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"a\") expected \, got {result}")
        failed += 1

    # Test 10
    result = see_color(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"\") expected \, got {result}")
        failed += 1

    # Test 11
    result = see_color(\"xyzred\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: see_color(\"xyzred\") expected \, got {result}")
        failed += 1

    print(f"see_color: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
