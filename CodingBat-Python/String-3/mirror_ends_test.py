"""
Tester for mirrorEnds - CodingBat Python
11 test cases
"""

from mirror_ends import mirror_ends


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = mirror_ends(\"abXYZba\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"abXYZba\") expected \, got {result}")
        failed += 1

    # Test 2
    result = mirror_ends(\"abca\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"abca\") expected \, got {result}")
        failed += 1

    # Test 3
    result = mirror_ends(\"aba\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"aba\") expected \, got {result}")
        failed += 1

    # Test 4
    result = mirror_ends(\"abab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"abab\") expected \, got {result}")
        failed += 1

    # Test 5
    result = mirror_ends(\"xxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"xxx\") expected \, got {result}")
        failed += 1

    # Test 6
    result = mirror_ends(\"xxYxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"xxYxx\") expected \, got {result}")
        failed += 1

    # Test 7
    result = mirror_ends(\"Hi and iH\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"Hi and iH\") expected \, got {result}")
        failed += 1

    # Test 8
    result = mirror_ends(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"x\") expected \, got {result}")
        failed += 1

    # Test 9
    result = mirror_ends(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"\") expected \, got {result}")
        failed += 1

    # Test 10
    result = mirror_ends(\"123and then 321\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"123and then 321\") expected \, got {result}")
        failed += 1

    # Test 11
    result = mirror_ends(\"band andab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: mirror_ends(\"band andab\") expected \, got {result}")
        failed += 1

    print(f"mirror_ends: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
