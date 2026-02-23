"""
Tester for middleThree - CodingBat Python
7 test cases
"""

from middle_three import middle_three


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = middle_three(\"Candy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_three(\"Candy\") expected \, got {result}")
        failed += 1

    # Test 2
    result = middle_three(\"and\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_three(\"and\") expected \, got {result}")
        failed += 1

    # Test 3
    result = middle_three(\"solving\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_three(\"solving\") expected \, got {result}")
        failed += 1

    # Test 4
    result = middle_three(\"Hi yet Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_three(\"Hi yet Hi\") expected \, got {result}")
        failed += 1

    # Test 5
    result = middle_three(\"java yet java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_three(\"java yet java\") expected \, got {result}")
        failed += 1

    # Test 6
    result = middle_three(\"Chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_three(\"Chocolate\") expected \, got {result}")
        failed += 1

    # Test 7
    result = middle_three(\"XabcxyzabcX\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: middle_three(\"XabcxyzabcX\") expected \, got {result}")
        failed += 1

    print(f"middle_three: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
