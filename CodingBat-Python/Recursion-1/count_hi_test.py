"""
Tester for countHi - CodingBat Python
11 test cases
"""

from count_hi import count_hi


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_hi(\"xxhixx\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"xxhixx\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_hi(\"xhixhix\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"xhixhix\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_hi(\"hi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"hi\") expected 1, got {result}")
        failed += 1

    # Test 4
    result = count_hi(\"hihih\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"hihih\") expected 2, got {result}")
        failed += 1

    # Test 5
    result = count_hi(\"h\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"h\") expected 0, got {result}")
        failed += 1

    # Test 6
    result = count_hi(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"\") expected 0, got {result}")
        failed += 1

    # Test 7
    result = count_hi(\"ihihihihih\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"ihihihihih\") expected 4, got {result}")
        failed += 1

    # Test 8
    result = count_hi(\"ihihihihihi\")
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"ihihihihihi\") expected 5, got {result}")
        failed += 1

    # Test 9
    result = count_hi(\"hiAAhi12hi\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"hiAAhi12hi\") expected 3, got {result}")
        failed += 1

    # Test 10
    result = count_hi(\"xhixhxihihhhih\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"xhixhxihihhhih\") expected 3, got {result}")
        failed += 1

    # Test 11
    result = count_hi(\"ship\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"ship\") expected 1, got {result}")
        failed += 1

    print(f"count_hi: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
