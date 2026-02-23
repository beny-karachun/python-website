"""
Tester for changeXY - CodingBat Python
10 test cases
"""

from change_xy import change_xy


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = change_xy(\"codex\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"codex\") expected \, got {result}")
        failed += 1

    # Test 2
    result = change_xy(\"xxhixx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"xxhixx\") expected \, got {result}")
        failed += 1

    # Test 3
    result = change_xy(\"xhixhix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"xhixhix\") expected \, got {result}")
        failed += 1

    # Test 4
    result = change_xy(\"hiy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"hiy\") expected \, got {result}")
        failed += 1

    # Test 5
    result = change_xy(\"h\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"h\") expected \, got {result}")
        failed += 1

    # Test 6
    result = change_xy(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"x\") expected \, got {result}")
        failed += 1

    # Test 7
    result = change_xy(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"\") expected \, got {result}")
        failed += 1

    # Test 8
    result = change_xy(\"xxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"xxx\") expected \, got {result}")
        failed += 1

    # Test 9
    result = change_xy(\"yyhxyi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"yyhxyi\") expected \, got {result}")
        failed += 1

    # Test 10
    result = change_xy(\"hihi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_xy(\"hihi\") expected \, got {result}")
        failed += 1

    print(f"change_xy: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
