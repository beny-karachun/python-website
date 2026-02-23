"""
Tester for pairStar - CodingBat Python
10 test cases
"""

from pair_star import pair_star


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = pair_star(\"hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = pair_star(\"xxyy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"xxyy\") expected \, got {result}")
        failed += 1

    # Test 3
    result = pair_star(\"aaaa\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"aaaa\") expected \, got {result}")
        failed += 1

    # Test 4
    result = pair_star(\"aaab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"aaab\") expected \, got {result}")
        failed += 1

    # Test 5
    result = pair_star(\"aa\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"aa\") expected \, got {result}")
        failed += 1

    # Test 6
    result = pair_star(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"a\") expected \, got {result}")
        failed += 1

    # Test 7
    result = pair_star(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"\") expected \, got {result}")
        failed += 1

    # Test 8
    result = pair_star(\"noadjacent\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"noadjacent\") expected \, got {result}")
        failed += 1

    # Test 9
    result = pair_star(\"abba\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"abba\") expected \, got {result}")
        failed += 1

    # Test 10
    result = pair_star(\"abbba\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: pair_star(\"abbba\") expected \, got {result}")
        failed += 1

    print(f"pair_star: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
