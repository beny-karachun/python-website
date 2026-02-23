"""
Tester for makeAbba - CodingBat Python
9 test cases
"""

from make_abba import make_abba


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = make_abba(\"Hi\", \"Bye\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"Hi\", \"Bye\") expected \, got {result}")
        failed += 1

    # Test 2
    result = make_abba(\"Yo\", \"Alice\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"Yo\", \"Alice\") expected \, got {result}")
        failed += 1

    # Test 3
    result = make_abba(\"What\", \"Up\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"What\", \"Up\") expected \, got {result}")
        failed += 1

    # Test 4
    result = make_abba(\"aaa\", \"bbb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"aaa\", \"bbb\") expected \, got {result}")
        failed += 1

    # Test 5
    result = make_abba(\"x\", \"y\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"x\", \"y\") expected \, got {result}")
        failed += 1

    # Test 6
    result = make_abba(\"x\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"x\", \"\") expected \, got {result}")
        failed += 1

    # Test 7
    result = make_abba(\"\", \"y\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"\", \"y\") expected \, got {result}")
        failed += 1

    # Test 8
    result = make_abba(\"Bo\", \"Ya\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"Bo\", \"Ya\") expected \, got {result}")
        failed += 1

    # Test 9
    result = make_abba(\"Ya\", \"Ya\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_abba(\"Ya\", \"Ya\") expected \, got {result}")
        failed += 1

    print(f"make_abba: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
