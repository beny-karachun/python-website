"""
Tester for countX - CodingBat Python
8 test cases
"""

from count_x import count_x


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_x(\"xxhixx\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count_x(\"xxhixx\") expected 4, got {result}")
        failed += 1

    # Test 2
    result = count_x(\"xhixhix\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_x(\"xhixhix\") expected 3, got {result}")
        failed += 1

    # Test 3
    result = count_x(\"hi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_x(\"hi\") expected 0, got {result}")
        failed += 1

    # Test 4
    result = count_x(\"h\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_x(\"h\") expected 0, got {result}")
        failed += 1

    # Test 5
    result = count_x(\"x\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_x(\"x\") expected 1, got {result}")
        failed += 1

    # Test 6
    result = count_x(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_x(\"\") expected 0, got {result}")
        failed += 1

    # Test 7
    result = count_x(\"hihi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_x(\"hihi\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = count_x(\"hiAAhi12hi\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_x(\"hiAAhi12hi\") expected 0, got {result}")
        failed += 1

    print(f"count_x: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
