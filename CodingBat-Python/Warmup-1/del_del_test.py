"""
Tester for delDel - CodingBat Python
11 test cases
"""

from del_del import del_del


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = del_del(\"adelbc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"adelbc\") expected \, got {result}")
        failed += 1

    # Test 2
    result = del_del(\"adelHello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"adelHello\") expected \, got {result}")
        failed += 1

    # Test 3
    result = del_del(\"adedbc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"adedbc\") expected \, got {result}")
        failed += 1

    # Test 4
    result = del_del(\"abcdel\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"abcdel\") expected \, got {result}")
        failed += 1

    # Test 5
    result = del_del(\"add\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"add\") expected \, got {result}")
        failed += 1

    # Test 6
    result = del_del(\"ad\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"ad\") expected \, got {result}")
        failed += 1

    # Test 7
    result = del_del(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"a\") expected \, got {result}")
        failed += 1

    # Test 8
    result = del_del(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = del_del(\"del\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"del\") expected \, got {result}")
        failed += 1

    # Test 10
    result = del_del(\"adel\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"adel\") expected \, got {result}")
        failed += 1

    # Test 11
    result = del_del(\"aadelbb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: del_del(\"aadelbb\") expected \, got {result}")
        failed += 1

    print(f"del_del: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
