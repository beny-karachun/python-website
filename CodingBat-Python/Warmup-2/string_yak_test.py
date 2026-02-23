"""
Tester for stringYak - CodingBat Python
7 test cases
"""

from string_yak import string_yak


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_yak(\"yakpak\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_yak(\"yakpak\") expected \, got {result}")
        failed += 1

    # Test 2
    result = string_yak(\"pakyak\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_yak(\"pakyak\") expected \, got {result}")
        failed += 1

    # Test 3
    result = string_yak(\"yak123ya\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_yak(\"yak123ya\") expected \, got {result}")
        failed += 1

    # Test 4
    result = string_yak(\"yak\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_yak(\"yak\") expected \, got {result}")
        failed += 1

    # Test 5
    result = string_yak(\"yakxxxyak\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_yak(\"yakxxxyak\") expected \, got {result}")
        failed += 1

    # Test 6
    result = string_yak(\"HiyakHi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_yak(\"HiyakHi\") expected \, got {result}")
        failed += 1

    # Test 7
    result = string_yak(\"xxxyakyyyakzzz\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_yak(\"xxxyakyyyakzzz\") expected \, got {result}")
        failed += 1

    print(f"string_yak: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
