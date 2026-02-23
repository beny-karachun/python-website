"""
Tester for stringE - CodingBat Python
6 test cases
"""

from string_e import string_e


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_e(\"Hello\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: string_e(\"Hello\") expected True, got {result}")
        failed += 1

    # Test 2
    result = string_e(\"Heelle\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: string_e(\"Heelle\") expected True, got {result}")
        failed += 1

    # Test 3
    result = string_e(\"Heelele\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: string_e(\"Heelele\") expected False, got {result}")
        failed += 1

    # Test 4
    result = string_e(\"Hll\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: string_e(\"Hll\") expected False, got {result}")
        failed += 1

    # Test 5
    result = string_e(\"e\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: string_e(\"e\") expected True, got {result}")
        failed += 1

    # Test 6
    result = string_e(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: string_e(\"\") expected False, got {result}")
        failed += 1

    print(f"string_e: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
