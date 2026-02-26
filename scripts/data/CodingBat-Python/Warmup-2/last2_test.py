"""
Tester for last2 - CodingBat Python
13 test cases
"""

from last2 import last2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = last2(\"hixxhi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: last2(\"hixxhi\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = last2(\"xaxxaxaxx\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: last2(\"xaxxaxaxx\") expected 1, got {result}")
        failed += 1

    # Test 3
    result = last2(\"axxxaaxx\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: last2(\"axxxaaxx\") expected 2, got {result}")
        failed += 1

    # Test 4
    result = last2(\"xxaxxaxxaxx\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: last2(\"xxaxxaxxaxx\") expected 3, got {result}")
        failed += 1

    # Test 5
    result = last2(\"xaxaxaxx\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: last2(\"xaxaxaxx\") expected 0, got {result}")
        failed += 1

    # Test 6
    result = last2(\"xxxx\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: last2(\"xxxx\") expected 2, got {result}")
        failed += 1

    # Test 7
    result = last2(\"13121312\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: last2(\"13121312\") expected 1, got {result}")
        failed += 1

    # Test 8
    result = last2(\"11212\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: last2(\"11212\") expected 1, got {result}")
        failed += 1

    # Test 9
    result = last2(\"13121311\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: last2(\"13121311\") expected 0, got {result}")
        failed += 1

    # Test 10
    result = last2(\"1717171\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: last2(\"1717171\") expected 2, got {result}")
        failed += 1

    # Test 11
    result = last2(\"hi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: last2(\"hi\") expected 0, got {result}")
        failed += 1

    # Test 12
    result = last2(\"h\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: last2(\"h\") expected 0, got {result}")
        failed += 1

    # Test 13
    result = last2(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: last2(\"\") expected 0, got {result}")
        failed += 1

    print(f"last2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
