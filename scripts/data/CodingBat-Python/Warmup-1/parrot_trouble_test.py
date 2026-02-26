"""
Tester for parrotTrouble - CodingBat Python
10 test cases
"""

from parrot_trouble import parrot_trouble


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = parrot_trouble(True, 6)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(True, 6) expected True, got {result}")
        failed += 1

    # Test 2
    result = parrot_trouble(True, 7)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(True, 7) expected False, got {result}")
        failed += 1

    # Test 3
    result = parrot_trouble(False, 6)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(False, 6) expected False, got {result}")
        failed += 1

    # Test 4
    result = parrot_trouble(True, 21)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(True, 21) expected True, got {result}")
        failed += 1

    # Test 5
    result = parrot_trouble(False, 21)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(False, 21) expected False, got {result}")
        failed += 1

    # Test 6
    result = parrot_trouble(False, 20)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(False, 20) expected False, got {result}")
        failed += 1

    # Test 7
    result = parrot_trouble(True, 23)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(True, 23) expected True, got {result}")
        failed += 1

    # Test 8
    result = parrot_trouble(False, 23)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(False, 23) expected False, got {result}")
        failed += 1

    # Test 9
    result = parrot_trouble(True, 20)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(True, 20) expected False, got {result}")
        failed += 1

    # Test 10
    result = parrot_trouble(False, 12)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: parrot_trouble(False, 12) expected False, got {result}")
        failed += 1

    print(f"parrot_trouble: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
