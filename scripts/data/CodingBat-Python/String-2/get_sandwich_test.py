"""
Tester for getSandwich - CodingBat Python
12 test cases
"""

from get_sandwich import get_sandwich


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = get_sandwich(\"breadjambread\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"breadjambread\") expected \, got {result}")
        failed += 1

    # Test 2
    result = get_sandwich(\"xxbreadjambreadyy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"xxbreadjambreadyy\") expected \, got {result}")
        failed += 1

    # Test 3
    result = get_sandwich(\"xxbreadyy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"xxbreadyy\") expected \, got {result}")
        failed += 1

    # Test 4
    result = get_sandwich(\"xxbreadbreadjambreadyy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"xxbreadbreadjambreadyy\") expected \, got {result}")
        failed += 1

    # Test 5
    result = get_sandwich(\"breadAbread\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"breadAbread\") expected \, got {result}")
        failed += 1

    # Test 6
    result = get_sandwich(\"breadbread\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"breadbread\") expected \, got {result}")
        failed += 1

    # Test 7
    result = get_sandwich(\"abcbreaz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"abcbreaz\") expected \, got {result}")
        failed += 1

    # Test 8
    result = get_sandwich(\"xyz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"xyz\") expected \, got {result}")
        failed += 1

    # Test 9
    result = get_sandwich(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"\") expected \, got {result}")
        failed += 1

    # Test 10
    result = get_sandwich(\"breadbreaxbread\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"breadbreaxbread\") expected \, got {result}")
        failed += 1

    # Test 11
    result = get_sandwich(\"breaxbreadybread\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"breaxbreadybread\") expected \, got {result}")
        failed += 1

    # Test 12
    result = get_sandwich(\"breadbreadbreadbread\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: get_sandwich(\"breadbreadbreadbread\") expected \, got {result}")
        failed += 1

    print(f"get_sandwich: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
