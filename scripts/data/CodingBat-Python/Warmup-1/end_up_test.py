"""
Tester for endUp - CodingBat Python
7 test cases
"""

from end_up import end_up


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = end_up(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_up(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = end_up(\"hi there\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_up(\"hi there\") expected \, got {result}")
        failed += 1

    # Test 3
    result = end_up(\"hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_up(\"hi\") expected \, got {result}")
        failed += 1

    # Test 4
    result = end_up(\"woo hoo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_up(\"woo hoo\") expected \, got {result}")
        failed += 1

    # Test 5
    result = end_up(\"xyz12\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_up(\"xyz12\") expected \, got {result}")
        failed += 1

    # Test 6
    result = end_up(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_up(\"x\") expected \, got {result}")
        failed += 1

    # Test 7
    result = end_up(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_up(\"\") expected \, got {result}")
        failed += 1

    print(f"end_up: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
