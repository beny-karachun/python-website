"""
Tester for maxBlock - CodingBat Python
11 test cases
"""

from max_block import max_block


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = max_block(\"hoopla\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: max_block(\"hoopla\") expected 2, got {result}")
        failed += 1

    # Test 2
    result = max_block(\"abbCCCddBBBxx\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: max_block(\"abbCCCddBBBxx\") expected 3, got {result}")
        failed += 1

    # Test 3
    result = max_block(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: max_block(\"\") expected 0, got {result}")
        failed += 1

    # Test 4
    result = max_block(\"xyz\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: max_block(\"xyz\") expected 1, got {result}")
        failed += 1

    # Test 5
    result = max_block(\"xxyz\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: max_block(\"xxyz\") expected 2, got {result}")
        failed += 1

    # Test 6
    result = max_block(\"xyzz\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: max_block(\"xyzz\") expected 2, got {result}")
        failed += 1

    # Test 7
    result = max_block(\"abbbcbbbxbbbx\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: max_block(\"abbbcbbbxbbbx\") expected 3, got {result}")
        failed += 1

    # Test 8
    result = max_block(\"XXBBBbbxx\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: max_block(\"XXBBBbbxx\") expected 3, got {result}")
        failed += 1

    # Test 9
    result = max_block(\"XXBBBBbbxx\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: max_block(\"XXBBBBbbxx\") expected 4, got {result}")
        failed += 1

    # Test 10
    result = max_block(\"XXBBBbbxxXXXX\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: max_block(\"XXBBBbbxxXXXX\") expected 4, got {result}")
        failed += 1

    # Test 11
    result = max_block(\"XX2222BBBbbXX2222\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: max_block(\"XX2222BBBbbXX2222\") expected 4, got {result}")
        failed += 1

    print(f"max_block: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
