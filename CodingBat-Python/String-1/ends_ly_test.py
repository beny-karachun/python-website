"""
Tester for endsLy - CodingBat Python
9 test cases
"""

from ends_ly import ends_ly


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = ends_ly(\"oddly\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"oddly\") expected True, got {result}")
        failed += 1

    # Test 2
    result = ends_ly(\"y\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"y\") expected False, got {result}")
        failed += 1

    # Test 3
    result = ends_ly(\"oddy\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"oddy\") expected False, got {result}")
        failed += 1

    # Test 4
    result = ends_ly(\"oddl\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"oddl\") expected False, got {result}")
        failed += 1

    # Test 5
    result = ends_ly(\"olydd\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"olydd\") expected False, got {result}")
        failed += 1

    # Test 6
    result = ends_ly(\"ly\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"ly\") expected True, got {result}")
        failed += 1

    # Test 7
    result = ends_ly(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"\") expected False, got {result}")
        failed += 1

    # Test 8
    result = ends_ly(\"Falsey\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"Falsey\") expected False, got {result}")
        failed += 1

    # Test 9
    result = ends_ly(\"evenly\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: ends_ly(\"evenly\") expected True, got {result}")
        failed += 1

    print(f"ends_ly: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
