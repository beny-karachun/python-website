"""
Tester for countHi2 - CodingBat Python
16 test cases
"""

from count_hi2 import count_hi2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_hi2(\"ahixhi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"ahixhi\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_hi2(\"ahibhi\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"ahibhi\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_hi2(\"xhixhi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"xhixhi\") expected 0, got {result}")
        failed += 1

    # Test 4
    result = count_hi2(\"hixhi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"hixhi\") expected 1, got {result}")
        failed += 1

    # Test 5
    result = count_hi2(\"hixhhi\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"hixhhi\") expected 2, got {result}")
        failed += 1

    # Test 6
    result = count_hi2(\"hihihi\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"hihihi\") expected 3, got {result}")
        failed += 1

    # Test 7
    result = count_hi2(\"hihihix\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"hihihix\") expected 3, got {result}")
        failed += 1

    # Test 8
    result = count_hi2(\"xhihihix\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"xhihihix\") expected 2, got {result}")
        failed += 1

    # Test 9
    result = count_hi2(\"xxhi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"xxhi\") expected 0, got {result}")
        failed += 1

    # Test 10
    result = count_hi2(\"hixxhi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"hixxhi\") expected 1, got {result}")
        failed += 1

    # Test 11
    result = count_hi2(\"hi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"hi\") expected 1, got {result}")
        failed += 1

    # Test 12
    result = count_hi2(\"xxxx\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"xxxx\") expected 0, got {result}")
        failed += 1

    # Test 13
    result = count_hi2(\"h\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"h\") expected 0, got {result}")
        failed += 1

    # Test 14
    result = count_hi2(\"x\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"x\") expected 0, got {result}")
        failed += 1

    # Test 15
    result = count_hi2(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"\") expected 0, got {result}")
        failed += 1

    # Test 16
    result = count_hi2(\"Hellohi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi2(\"Hellohi\") expected 1, got {result}")
        failed += 1

    print(f"count_hi2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
