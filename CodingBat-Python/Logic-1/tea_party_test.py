"""
Tester for teaParty - CodingBat Python
13 test cases
"""

from tea_party import tea_party


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = tea_party(6, 8)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: tea_party(6, 8) expected 1, got {result}")
        failed += 1

    # Test 2
    result = tea_party(3, 8)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: tea_party(3, 8) expected 0, got {result}")
        failed += 1

    # Test 3
    result = tea_party(20, 6)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: tea_party(20, 6) expected 2, got {result}")
        failed += 1

    # Test 4
    result = tea_party(12, 6)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: tea_party(12, 6) expected 2, got {result}")
        failed += 1

    # Test 5
    result = tea_party(11, 6)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: tea_party(11, 6) expected 1, got {result}")
        failed += 1

    # Test 6
    result = tea_party(11, 4)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: tea_party(11, 4) expected 0, got {result}")
        failed += 1

    # Test 7
    result = tea_party(4, 5)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: tea_party(4, 5) expected 0, got {result}")
        failed += 1

    # Test 8
    result = tea_party(5, 5)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: tea_party(5, 5) expected 1, got {result}")
        failed += 1

    # Test 9
    result = tea_party(6, 6)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: tea_party(6, 6) expected 1, got {result}")
        failed += 1

    # Test 10
    result = tea_party(5, 10)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: tea_party(5, 10) expected 2, got {result}")
        failed += 1

    # Test 11
    result = tea_party(5, 9)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: tea_party(5, 9) expected 1, got {result}")
        failed += 1

    # Test 12
    result = tea_party(10, 4)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: tea_party(10, 4) expected 0, got {result}")
        failed += 1

    # Test 13
    result = tea_party(10, 20)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: tea_party(10, 20) expected 2, got {result}")
        failed += 1

    print(f"tea_party: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
