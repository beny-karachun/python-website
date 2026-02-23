"""
Tester for countHi - CodingBat Python
9 test cases
"""

from count_hi import count_hi


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_hi(\"abc hi ho\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"abc hi ho\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_hi(\"ABChi hi\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"ABChi hi\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_hi(\"hihi\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"hihi\") expected 2, got {result}")
        failed += 1

    # Test 4
    result = count_hi(\"hiHIhi\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"hiHIhi\") expected 2, got {result}")
        failed += 1

    # Test 5
    result = count_hi(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"\") expected 0, got {result}")
        failed += 1

    # Test 6
    result = count_hi(\"h\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"h\") expected 0, got {result}")
        failed += 1

    # Test 7
    result = count_hi(\"hi\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"hi\") expected 1, got {result}")
        failed += 1

    # Test 8
    result = count_hi(\"Hi is no HI on ahI\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"Hi is no HI on ahI\") expected 0, got {result}")
        failed += 1

    # Test 9
    result = count_hi(\"hiho not HOHIhi\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_hi(\"hiho not HOHIhi\") expected 2, got {result}")
        failed += 1

    print(f"count_hi: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
