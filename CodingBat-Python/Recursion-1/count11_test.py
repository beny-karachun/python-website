"""
Tester for count11 - CodingBat Python
11 test cases
"""

from count11 import count11


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count11(\"11abc11\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count11(\"11abc11\") expected 2, got {result}")
        failed += 1

    # Test 2
    result = count11(\"abc11x11x11\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count11(\"abc11x11x11\") expected 3, got {result}")
        failed += 1

    # Test 3
    result = count11(\"111\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count11(\"111\") expected 1, got {result}")
        failed += 1

    # Test 4
    result = count11(\"1111\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count11(\"1111\") expected 2, got {result}")
        failed += 1

    # Test 5
    result = count11(\"1\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count11(\"1\") expected 0, got {result}")
        failed += 1

    # Test 6
    result = count11(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count11(\"\") expected 0, got {result}")
        failed += 1

    # Test 7
    result = count11(\"hi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count11(\"hi\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = count11(\"11x111x1111\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count11(\"11x111x1111\") expected 4, got {result}")
        failed += 1

    # Test 9
    result = count11(\"1x111\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count11(\"1x111\") expected 1, got {result}")
        failed += 1

    # Test 10
    result = count11(\"1Hello1\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count11(\"1Hello1\") expected 0, got {result}")
        failed += 1

    # Test 11
    result = count11(\"Hello\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count11(\"Hello\") expected 0, got {result}")
        failed += 1

    print(f"count11: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
