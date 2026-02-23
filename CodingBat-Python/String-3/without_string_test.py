"""
Tester for withoutString - CodingBat Python
19 test cases
"""

from without_string import without_string


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = without_string(\"Hello there\", \"llo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"Hello there\", \"llo\") expected \, got {result}")
        failed += 1

    # Test 2
    result = without_string(\"Hello there\", \"e\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"Hello there\", \"e\") expected \, got {result}")
        failed += 1

    # Test 3
    result = without_string(\"Hello there\", \"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"Hello there\", \"x\") expected \, got {result}")
        failed += 1

    # Test 4
    result = without_string(\"This is a FISH\", \"IS\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"This is a FISH\", \"IS\") expected \, got {result}")
        failed += 1

    # Test 5
    result = without_string(\"THIS is a FISH\", \"is\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"THIS is a FISH\", \"is\") expected \, got {result}")
        failed += 1

    # Test 6
    result = without_string(\"THIS is a FISH\", \"iS\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"THIS is a FISH\", \"iS\") expected \, got {result}")
        failed += 1

    # Test 7
    result = without_string(\"abxxxxab\", \"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"abxxxxab\", \"xx\") expected \, got {result}")
        failed += 1

    # Test 8
    result = without_string(\"abxxxab\", \"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"abxxxab\", \"xx\") expected \, got {result}")
        failed += 1

    # Test 9
    result = without_string(\"abxxxab\", \"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"abxxxab\", \"x\") expected \, got {result}")
        failed += 1

    # Test 10
    result = without_string(\"xxx\", \"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"xxx\", \"x\") expected \, got {result}")
        failed += 1

    # Test 11
    result = without_string(\"xxx\", \"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"xxx\", \"xx\") expected \, got {result}")
        failed += 1

    # Test 12
    result = without_string(\"xyzzy\", \"Y\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"xyzzy\", \"Y\") expected \, got {result}")
        failed += 1

    # Test 13
    result = without_string(\"\", \"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"\", \"x\") expected \, got {result}")
        failed += 1

    # Test 14
    result = without_string(\"abcabc\", \"b\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"abcabc\", \"b\") expected \, got {result}")
        failed += 1

    # Test 15
    result = without_string(\"AA22bb\", \"2\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"AA22bb\", \"2\") expected \, got {result}")
        failed += 1

    # Test 16
    result = without_string(\"1111\", \"1\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"1111\", \"1\") expected \, got {result}")
        failed += 1

    # Test 17
    result = without_string(\"1111\", \"11\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"1111\", \"11\") expected \, got {result}")
        failed += 1

    # Test 18
    result = without_string(\"MkjtMkx\", \"Mk\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"MkjtMkx\", \"Mk\") expected \, got {result}")
        failed += 1

    # Test 19
    result = without_string(\"Hi HoHo\", \"Ho\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_string(\"Hi HoHo\", \"Ho\") expected \, got {result}")
        failed += 1

    print(f"without_string: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
