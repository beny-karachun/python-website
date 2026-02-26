"""
Tester for fizzString2 - CodingBat Python
17 test cases
"""

from fizz_string2 import fizz_string2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = fizz_string2(1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(1) expected \, got {result}")
        failed += 1

    # Test 2
    result = fizz_string2(2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(2) expected \, got {result}")
        failed += 1

    # Test 3
    result = fizz_string2(3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(3) expected \, got {result}")
        failed += 1

    # Test 4
    result = fizz_string2(4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(4) expected \, got {result}")
        failed += 1

    # Test 5
    result = fizz_string2(5)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(5) expected \, got {result}")
        failed += 1

    # Test 6
    result = fizz_string2(6)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(6) expected \, got {result}")
        failed += 1

    # Test 7
    result = fizz_string2(7)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(7) expected \, got {result}")
        failed += 1

    # Test 8
    result = fizz_string2(8)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(8) expected \, got {result}")
        failed += 1

    # Test 9
    result = fizz_string2(9)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(9) expected \, got {result}")
        failed += 1

    # Test 10
    result = fizz_string2(15)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(15) expected \, got {result}")
        failed += 1

    # Test 11
    result = fizz_string2(16)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(16) expected \, got {result}")
        failed += 1

    # Test 12
    result = fizz_string2(18)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(18) expected \, got {result}")
        failed += 1

    # Test 13
    result = fizz_string2(19)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(19) expected \, got {result}")
        failed += 1

    # Test 14
    result = fizz_string2(21)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(21) expected \, got {result}")
        failed += 1

    # Test 15
    result = fizz_string2(44)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(44) expected \, got {result}")
        failed += 1

    # Test 16
    result = fizz_string2(45)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(45) expected \, got {result}")
        failed += 1

    # Test 17
    result = fizz_string2(100)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: fizz_string2(100) expected \, got {result}")
        failed += 1

    print(f"fizz_string2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
