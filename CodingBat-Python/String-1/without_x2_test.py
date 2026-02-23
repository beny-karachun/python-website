"""
Tester for withoutX2 - CodingBat Python
12 test cases
"""

from without_x2 import without_x2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = without_x2(\"xHi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"xHi\") expected \, got {result}")
        failed += 1

    # Test 2
    result = without_x2(\"Hxi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"Hxi\") expected \, got {result}")
        failed += 1

    # Test 3
    result = without_x2(\"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"Hi\") expected \, got {result}")
        failed += 1

    # Test 4
    result = without_x2(\"xxHi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"xxHi\") expected \, got {result}")
        failed += 1

    # Test 5
    result = without_x2(\"Hix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"Hix\") expected \, got {result}")
        failed += 1

    # Test 6
    result = without_x2(\"xaxb\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"xaxb\") expected \, got {result}")
        failed += 1

    # Test 7
    result = without_x2(\"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"xx\") expected \, got {result}")
        failed += 1

    # Test 8
    result = without_x2(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"x\") expected \, got {result}")
        failed += 1

    # Test 9
    result = without_x2(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"\") expected \, got {result}")
        failed += 1

    # Test 10
    result = without_x2(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 11
    result = without_x2(\"Hexllo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"Hexllo\") expected \, got {result}")
        failed += 1

    # Test 12
    result = without_x2(\"xHxllo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: without_x2(\"xHxllo\") expected \, got {result}")
        failed += 1

    print(f"without_x2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
