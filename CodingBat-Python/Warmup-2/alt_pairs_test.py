"""
Tester for altPairs - CodingBat Python
8 test cases
"""

from alt_pairs import alt_pairs


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = alt_pairs(\"kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"kitten\") expected \, got {result}")
        failed += 1

    # Test 2
    result = alt_pairs(\"Chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"Chocolate\") expected \, got {result}")
        failed += 1

    # Test 3
    result = alt_pairs(\"CodingHorror\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"CodingHorror\") expected \, got {result}")
        failed += 1

    # Test 4
    result = alt_pairs(\"yak\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"yak\") expected \, got {result}")
        failed += 1

    # Test 5
    result = alt_pairs(\"ya\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"ya\") expected \, got {result}")
        failed += 1

    # Test 6
    result = alt_pairs(\"y\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"y\") expected \, got {result}")
        failed += 1

    # Test 7
    result = alt_pairs(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"\") expected \, got {result}")
        failed += 1

    # Test 8
    result = alt_pairs(\"ThisThatTheOther\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: alt_pairs(\"ThisThatTheOther\") expected \, got {result}")
        failed += 1

    print(f"alt_pairs: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
