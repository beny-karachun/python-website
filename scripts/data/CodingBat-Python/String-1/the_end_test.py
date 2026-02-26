"""
Tester for theEnd - CodingBat Python
10 test cases
"""

from the_end import the_end


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = the_end(\"Hello\", True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"Hello\", True) expected \, got {result}")
        failed += 1

    # Test 2
    result = the_end(\"Hello\", False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"Hello\", False) expected \, got {result}")
        failed += 1

    # Test 3
    result = the_end(\"oh\", True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"oh\", True) expected \, got {result}")
        failed += 1

    # Test 4
    result = the_end(\"oh\", False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"oh\", False) expected \, got {result}")
        failed += 1

    # Test 5
    result = the_end(\"x\", True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"x\", True) expected \, got {result}")
        failed += 1

    # Test 6
    result = the_end(\"x\", False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"x\", False) expected \, got {result}")
        failed += 1

    # Test 7
    result = the_end(\"java\", True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"java\", True) expected \, got {result}")
        failed += 1

    # Test 8
    result = the_end(\"chocolate\", False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"chocolate\", False) expected \, got {result}")
        failed += 1

    # Test 9
    result = the_end(\"1234\", True)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"1234\", True) expected \, got {result}")
        failed += 1

    # Test 10
    result = the_end(\"code\", False)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: the_end(\"code\", False) expected \, got {result}")
        failed += 1

    print(f"the_end: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
