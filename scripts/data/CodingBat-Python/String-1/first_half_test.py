"""
Tester for firstHalf - CodingBat Python
7 test cases
"""

from first_half import first_half


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = first_half(\"WooHoo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_half(\"WooHoo\") expected \, got {result}")
        failed += 1

    # Test 2
    result = first_half(\"HelloThere\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_half(\"HelloThere\") expected \, got {result}")
        failed += 1

    # Test 3
    result = first_half(\"abcdef\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_half(\"abcdef\") expected \, got {result}")
        failed += 1

    # Test 4
    result = first_half(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_half(\"ab\") expected \, got {result}")
        failed += 1

    # Test 5
    result = first_half(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_half(\"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = first_half(\"0123456789\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_half(\"0123456789\") expected \, got {result}")
        failed += 1

    # Test 7
    result = first_half(\"kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: first_half(\"kitten\") expected \, got {result}")
        failed += 1

    print(f"first_half: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
