"""
Tester for strCopies - CodingBat Python
14 test cases
"""

from str_copies import str_copies


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = str_copies(\"catcowcat\", \"cat\", 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"catcowcat\", \"cat\", 2) expected True, got {result}")
        failed += 1

    # Test 2
    result = str_copies(\"catcowcat\", \"cow\", 2)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"catcowcat\", \"cow\", 2) expected False, got {result}")
        failed += 1

    # Test 3
    result = str_copies(\"catcowcat\", \"cow\", 1)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"catcowcat\", \"cow\", 1) expected True, got {result}")
        failed += 1

    # Test 4
    result = str_copies(\"iiijjj\", \"i\", 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiijjj\", \"i\", 3) expected True, got {result}")
        failed += 1

    # Test 5
    result = str_copies(\"iiijjj\", \"i\", 4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiijjj\", \"i\", 4) expected False, got {result}")
        failed += 1

    # Test 6
    result = str_copies(\"iiijjj\", \"ii\", 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiijjj\", \"ii\", 2) expected True, got {result}")
        failed += 1

    # Test 7
    result = str_copies(\"iiijjj\", \"ii\", 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiijjj\", \"ii\", 3) expected False, got {result}")
        failed += 1

    # Test 8
    result = str_copies(\"iiijjj\", \"x\", 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiijjj\", \"x\", 3) expected False, got {result}")
        failed += 1

    # Test 9
    result = str_copies(\"iiijjj\", \"x\", 0)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiijjj\", \"x\", 0) expected True, got {result}")
        failed += 1

    # Test 10
    result = str_copies(\"iiiiij\", \"iii\", 3)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiiiij\", \"iii\", 3) expected True, got {result}")
        failed += 1

    # Test 11
    result = str_copies(\"iiiiij\", \"iii\", 4)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"iiiiij\", \"iii\", 4) expected False, got {result}")
        failed += 1

    # Test 12
    result = str_copies(\"ijiiiiij\", \"iiii\", 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"ijiiiiij\", \"iiii\", 2) expected True, got {result}")
        failed += 1

    # Test 13
    result = str_copies(\"ijiiiiij\", \"iiii\", 3)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"ijiiiiij\", \"iiii\", 3) expected False, got {result}")
        failed += 1

    # Test 14
    result = str_copies(\"dogcatdogcat\", \"dog\", 2)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: str_copies(\"dogcatdogcat\", \"dog\", 2) expected True, got {result}")
        failed += 1

    print(f"str_copies: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
