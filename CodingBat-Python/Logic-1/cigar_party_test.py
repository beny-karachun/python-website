"""
Tester for cigarParty - CodingBat Python
11 test cases
"""

from cigar_party import cigar_party


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = cigar_party(30, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cigar_party(30, False) expected False, got {result}")
        failed += 1

    # Test 2
    result = cigar_party(50, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cigar_party(50, False) expected True, got {result}")
        failed += 1

    # Test 3
    result = cigar_party(70, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cigar_party(70, True) expected True, got {result}")
        failed += 1

    # Test 4
    result = cigar_party(30, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cigar_party(30, True) expected False, got {result}")
        failed += 1

    # Test 5
    result = cigar_party(50, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cigar_party(50, True) expected True, got {result}")
        failed += 1

    # Test 6
    result = cigar_party(60, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cigar_party(60, False) expected True, got {result}")
        failed += 1

    # Test 7
    result = cigar_party(61, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cigar_party(61, False) expected False, got {result}")
        failed += 1

    # Test 8
    result = cigar_party(40, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cigar_party(40, False) expected True, got {result}")
        failed += 1

    # Test 9
    result = cigar_party(39, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cigar_party(39, False) expected False, got {result}")
        failed += 1

    # Test 10
    result = cigar_party(40, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cigar_party(40, True) expected True, got {result}")
        failed += 1

    # Test 11
    result = cigar_party(39, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cigar_party(39, True) expected False, got {result}")
        failed += 1

    print(f"cigar_party: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
