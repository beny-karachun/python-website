"""
Tester for makeOutWord - CodingBat Python
5 test cases
"""

from make_out_word import make_out_word


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = make_out_word(\"<<>>\", \"Yay\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_out_word(\"<<>>\", \"Yay\") expected \, got {result}")
        failed += 1

    # Test 2
    result = make_out_word(\"<<>>\", \"WooHoo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_out_word(\"<<>>\", \"WooHoo\") expected \, got {result}")
        failed += 1

    # Test 3
    result = make_out_word(\"[[]]\", \"word\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_out_word(\"[[]]\", \"word\") expected \, got {result}")
        failed += 1

    # Test 4
    result = make_out_word(\"HHoo\", \"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_out_word(\"HHoo\", \"Hello\") expected \, got {result}")
        failed += 1

    # Test 5
    result = make_out_word(\"abyz\", \"YAY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_out_word(\"abyz\", \"YAY\") expected \, got {result}")
        failed += 1

    print(f"make_out_word: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
