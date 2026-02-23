"""
Tester for countCode - CodingBat Python
14 test cases
"""

from count_code import count_code


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_code(\"aaacodebbb\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_code(\"aaacodebbb\") expected 1, got {result}")
        failed += 1

    # Test 2
    result = count_code(\"codexxcode\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_code(\"codexxcode\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_code(\"cozexxcope\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_code(\"cozexxcope\") expected 2, got {result}")
        failed += 1

    # Test 4
    result = count_code(\"cozfxxcope\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_code(\"cozfxxcope\") expected 1, got {result}")
        failed += 1

    # Test 5
    result = count_code(\"xxcozeyycop\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_code(\"xxcozeyycop\") expected 1, got {result}")
        failed += 1

    # Test 6
    result = count_code(\"cozcop\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_code(\"cozcop\") expected 0, got {result}")
        failed += 1

    # Test 7
    result = count_code(\"abcxyz\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_code(\"abcxyz\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = count_code(\"code\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_code(\"code\") expected 1, got {result}")
        failed += 1

    # Test 9
    result = count_code(\"ode\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_code(\"ode\") expected 0, got {result}")
        failed += 1

    # Test 10
    result = count_code(\"c\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_code(\"c\") expected 0, got {result}")
        failed += 1

    # Test 11
    result = count_code(\"\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_code(\"\") expected 0, got {result}")
        failed += 1

    # Test 12
    result = count_code(\"AAcodeBBcoleCCccoreDD\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_code(\"AAcodeBBcoleCCccoreDD\") expected 3, got {result}")
        failed += 1

    # Test 13
    result = count_code(\"AAcodeBBcoleCCccorfDD\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_code(\"AAcodeBBcoleCCccorfDD\") expected 2, got {result}")
        failed += 1

    # Test 14
    result = count_code(\"coAcodeBcoleccoreDD\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_code(\"coAcodeBcoleccoreDD\") expected 3, got {result}")
        failed += 1

    print(f"count_code: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
