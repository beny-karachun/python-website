"""
Tester for doubleX - CodingBat Python
11 test cases
"""

from double_x import double_x


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = double_x(\"axxbb\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: double_x(\"axxbb\") expected True, got {result}")
        failed += 1

    # Test 2
    result = double_x(\"axaxax\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"axaxax\") expected False, got {result}")
        failed += 1

    # Test 3
    result = double_x(\"xxxxx\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: double_x(\"xxxxx\") expected True, got {result}")
        failed += 1

    # Test 4
    result = double_x(\"xaxxx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"xaxxx\") expected False, got {result}")
        failed += 1

    # Test 5
    result = double_x(\"aaaax\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"aaaax\") expected False, got {result}")
        failed += 1

    # Test 6
    result = double_x(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"\") expected False, got {result}")
        failed += 1

    # Test 7
    result = double_x(\"abc\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"abc\") expected False, got {result}")
        failed += 1

    # Test 8
    result = double_x(\"x\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"x\") expected False, got {result}")
        failed += 1

    # Test 9
    result = double_x(\"xx\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: double_x(\"xx\") expected True, got {result}")
        failed += 1

    # Test 10
    result = double_x(\"xax\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"xax\") expected False, got {result}")
        failed += 1

    # Test 11
    result = double_x(\"xaxx\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: double_x(\"xaxx\") expected False, got {result}")
        failed += 1

    print(f"double_x: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
