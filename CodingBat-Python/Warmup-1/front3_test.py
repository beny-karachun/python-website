"""
Tester for front3 - CodingBat Python
7 test cases
"""

from front3 import front3


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = front3(\"Java\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front3(\"Java\") expected \, got {result}")
        failed += 1

    # Test 2
    result = front3(\"Chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front3(\"Chocolate\") expected \, got {result}")
        failed += 1

    # Test 3
    result = front3(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front3(\"abc\") expected \, got {result}")
        failed += 1

    # Test 4
    result = front3(\"abcXYZ\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front3(\"abcXYZ\") expected \, got {result}")
        failed += 1

    # Test 5
    result = front3(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front3(\"ab\") expected \, got {result}")
        failed += 1

    # Test 6
    result = front3(\"a\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front3(\"a\") expected \, got {result}")
        failed += 1

    # Test 7
    result = front3(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: front3(\"\") expected \, got {result}")
        failed += 1

    print(f"front3: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
