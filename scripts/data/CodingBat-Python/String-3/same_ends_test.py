"""
Tester for sameEnds - CodingBat Python
12 test cases
"""

from same_ends import same_ends


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = same_ends(\"abXYab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"abXYab\") expected \, got {result}")
        failed += 1

    # Test 2
    result = same_ends(\"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"xx\") expected \, got {result}")
        failed += 1

    # Test 3
    result = same_ends(\"xxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"xxx\") expected \, got {result}")
        failed += 1

    # Test 4
    result = same_ends(\"xxxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"xxxx\") expected \, got {result}")
        failed += 1

    # Test 5
    result = same_ends(\"javaXYZjava\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"javaXYZjava\") expected \, got {result}")
        failed += 1

    # Test 6
    result = same_ends(\"javajava\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"javajava\") expected \, got {result}")
        failed += 1

    # Test 7
    result = same_ends(\"xavaXYZjava\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"xavaXYZjava\") expected \, got {result}")
        failed += 1

    # Test 8
    result = same_ends(\"Hello! and Hello!\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"Hello! and Hello!\") expected \, got {result}")
        failed += 1

    # Test 9
    result = same_ends(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"x\") expected \, got {result}")
        failed += 1

    # Test 10
    result = same_ends(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"\") expected \, got {result}")
        failed += 1

    # Test 11
    result = same_ends(\"abcb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"abcb\") expected \, got {result}")
        failed += 1

    # Test 12
    result = same_ends(\"mymmy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: same_ends(\"mymmy\") expected \, got {result}")
        failed += 1

    print(f"same_ends: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
