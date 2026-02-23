"""
Tester for extraFront - CodingBat Python
6 test cases
"""

from extra_front import extra_front


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = extra_front(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_front(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = extra_front(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_front(\"ab\") expected \, got {result}")
        failed += 1

    # Test 3
    result = extra_front(\"H\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_front(\"H\") expected \, got {result}")
        failed += 1

    # Test 4
    result = extra_front(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_front(\"\") expected \, got {result}")
        failed += 1

    # Test 5
    result = extra_front(\"Candy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_front(\"Candy\") expected \, got {result}")
        failed += 1

    # Test 6
    result = extra_front(\"Code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: extra_front(\"Code\") expected \, got {result}")
        failed += 1

    print(f"extra_front: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
