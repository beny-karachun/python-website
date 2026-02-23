"""
Tester for startHi - CodingBat Python
8 test cases
"""

from start_hi import start_hi


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = start_hi(\"hi there\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"hi there\") expected True, got {result}")
        failed += 1

    # Test 2
    result = start_hi(\"hi\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"hi\") expected True, got {result}")
        failed += 1

    # Test 3
    result = start_hi(\"hello hi\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"hello hi\") expected False, got {result}")
        failed += 1

    # Test 4
    result = start_hi(\"he\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"he\") expected False, got {result}")
        failed += 1

    # Test 5
    result = start_hi(\"h\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"h\") expected False, got {result}")
        failed += 1

    # Test 6
    result = start_hi(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"\") expected False, got {result}")
        failed += 1

    # Test 7
    result = start_hi(\"ho hi\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"ho hi\") expected False, got {result}")
        failed += 1

    # Test 8
    result = start_hi(\"hi ho\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: start_hi(\"hi ho\") expected True, got {result}")
        failed += 1

    print(f"start_hi: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
