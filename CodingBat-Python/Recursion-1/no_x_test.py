"""
Tester for noX - CodingBat Python
6 test cases
"""

from no_x import no_x


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = no_x(\"xaxb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: no_x(\"xaxb\") expected \, got {result}")
        failed += 1

    # Test 2
    result = no_x(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: no_x(\"abc\") expected \, got {result}")
        failed += 1

    # Test 3
    result = no_x(\"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: no_x(\"xx\") expected \, got {result}")
        failed += 1

    # Test 4
    result = no_x(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: no_x(\"\") expected \, got {result}")
        failed += 1

    # Test 5
    result = no_x(\"axxbxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: no_x(\"axxbxx\") expected \, got {result}")
        failed += 1

    # Test 6
    result = no_x(\"Hellox\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: no_x(\"Hellox\") expected \, got {result}")
        failed += 1

    print(f"no_x: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
