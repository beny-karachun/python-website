"""
Tester for countPairs - CodingBat Python
11 test cases
"""

from count_pairs import count_pairs


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_pairs(\"axa\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"axa\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_pairs(\"axax\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"axax\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_pairs(\"axbx\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"axbx\") expected 1, got {result}")
        failed += 1

    # Test 4
    result = count_pairs(\"hi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"hi\") expected 0, got {result}")
        failed += 1

    # Test 5
    result = count_pairs(\"hihih\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"hihih\") expected 3, got {result}")
        failed += 1

    # Test 6
    result = count_pairs(\"ihihhh\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"ihihhh\") expected 3, got {result}")
        failed += 1

    # Test 7
    result = count_pairs(\"ihjxhh\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"ihjxhh\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = count_pairs(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"\") expected 0, got {result}")
        failed += 1

    # Test 9
    result = count_pairs(\"a\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"a\") expected 0, got {result}")
        failed += 1

    # Test 10
    result = count_pairs(\"aa\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"aa\") expected 0, got {result}")
        failed += 1

    # Test 11
    result = count_pairs(\"aaa\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_pairs(\"aaa\") expected 1, got {result}")
        failed += 1

    print(f"count_pairs: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
