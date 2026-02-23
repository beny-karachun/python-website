"""
Tester for sumDigits - CodingBat Python
9 test cases
"""

from sum_digits import sum_digits


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = sum_digits(\"aa1bc2d3\")
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"aa1bc2d3\") expected 6, got {result}")
        failed += 1

    # Test 2
    result = sum_digits(\"aa11b33\")
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"aa11b33\") expected 8, got {result}")
        failed += 1

    # Test 3
    result = sum_digits(\"Chocolate\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"Chocolate\") expected 0, got {result}")
        failed += 1

    # Test 4
    result = sum_digits(\"5hoco1a1e\")
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"5hoco1a1e\") expected 7, got {result}")
        failed += 1

    # Test 5
    result = sum_digits(\"123abc123\")
    if result == 12:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"123abc123\") expected 12, got {result}")
        failed += 1

    # Test 6
    result = sum_digits(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"\") expected 0, got {result}")
        failed += 1

    # Test 7
    result = sum_digits(\"Hello\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"Hello\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = sum_digits(\"X1z9b2\")
    if result == 12:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"X1z9b2\") expected 12, got {result}")
        failed += 1

    # Test 9
    result = sum_digits(\"5432a\")
    if result == 14:
        passed += 1
    else:
        print(f"FAIL: sum_digits(\"5432a\") expected 14, got {result}")
        failed += 1

    print(f"sum_digits: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
