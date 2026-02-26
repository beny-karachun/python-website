"""
Tester for sumNumbers - CodingBat Python
9 test cases
"""

from sum_numbers import sum_numbers


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = sum_numbers(\"abc123xyz\")
    if result == 123:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"abc123xyz\") expected 123, got {result}")
        failed += 1

    # Test 2
    result = sum_numbers(\"aa11b33\")
    if result == 44:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"aa11b33\") expected 44, got {result}")
        failed += 1

    # Test 3
    result = sum_numbers(\"7 11\")
    if result == 18:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"7 11\") expected 18, got {result}")
        failed += 1

    # Test 4
    result = sum_numbers(\"Chocolate\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"Chocolate\") expected 0, got {result}")
        failed += 1

    # Test 5
    result = sum_numbers(\"5hoco1a1e\")
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"5hoco1a1e\") expected 7, got {result}")
        failed += 1

    # Test 6
    result = sum_numbers(\"5$$1;;1!!\")
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"5$$1;;1!!\") expected 7, got {result}")
        failed += 1

    # Test 7
    result = sum_numbers(\"a1234bb11\")
    if result == 1245:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"a1234bb11\") expected 1245, got {result}")
        failed += 1

    # Test 8
    result = sum_numbers(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"\") expected 0, got {result}")
        failed += 1

    # Test 9
    result = sum_numbers(\"a22bbb3\")
    if result == 25:
        passed += 1
    else:
        print(f"FAIL: sum_numbers(\"a22bbb3\") expected 25, got {result}")
        failed += 1

    print(f"sum_numbers: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
