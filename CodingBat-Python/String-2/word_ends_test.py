"""
Tester for wordEnds - CodingBat Python
13 test cases
"""

from word_ends import word_ends


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = word_ends(\"abcXY123XYijk\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"abcXY123XYijk\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 2
    result = word_ends(\"XY123XY\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"XY123XY\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 3
    result = word_ends(\"XY1XY\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"XY1XY\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 4
    result = word_ends(\"XYXY\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"XYXY\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 5
    result = word_ends(\"XY\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"XY\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 6
    result = word_ends(\"Hi\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"Hi\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 7
    result = word_ends(\"\", \"XY\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"\", \"XY\") expected \, got {result}")
        failed += 1

    # Test 8
    result = word_ends(\"abc1xyz1i1j\", \"1\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"abc1xyz1i1j\", \"1\") expected \, got {result}")
        failed += 1

    # Test 9
    result = word_ends(\"abc1xyz1\", \"1\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"abc1xyz1\", \"1\") expected \, got {result}")
        failed += 1

    # Test 10
    result = word_ends(\"abc1xyz11\", \"1\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"abc1xyz11\", \"1\") expected \, got {result}")
        failed += 1

    # Test 11
    result = word_ends(\"abc1xyz1abc\", \"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"abc1xyz1abc\", \"abc\") expected \, got {result}")
        failed += 1

    # Test 12
    result = word_ends(\"abc1xyz1abc\", \"b\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"abc1xyz1abc\", \"b\") expected \, got {result}")
        failed += 1

    # Test 13
    result = word_ends(\"abc1abc1abc\", \"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: word_ends(\"abc1abc1abc\", \"abc\") expected \, got {result}")
        failed += 1

    print(f"word_ends: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
