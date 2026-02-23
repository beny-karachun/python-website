"""
Tester for without2 - CodingBat Python
9 test cases
"""

from without2 import without2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = without2(\"HelloHe\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"HelloHe\") expected \, got {result}")
        failed += 1

    # Test 2
    result = without2(\"HelloHi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"HelloHi\") expected \, got {result}")
        failed += 1

    # Test 3
    result = without2(\"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"Hi\") expected \, got {result}")
        failed += 1

    # Test 4
    result = without2(\"Chocolate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"Chocolate\") expected \, got {result}")
        failed += 1

    # Test 5
    result = without2(\"xxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"xxx\") expected \, got {result}")
        failed += 1

    # Test 6
    result = without2(\"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"xx\") expected \, got {result}")
        failed += 1

    # Test 7
    result = without2(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"x\") expected \, got {result}")
        failed += 1

    # Test 8
    result = without2(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = without2(\"Fruits\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without2(\"Fruits\") expected \, got {result}")
        failed += 1

    print(f"without2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
