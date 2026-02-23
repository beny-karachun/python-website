"""
Tester for squirrelPlay - CodingBat Python
13 test cases
"""

from squirrel_play import squirrel_play


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = squirrel_play(70, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(70, False) expected True, got {result}")
        failed += 1

    # Test 2
    result = squirrel_play(95, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(95, False) expected False, got {result}")
        failed += 1

    # Test 3
    result = squirrel_play(95, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(95, True) expected True, got {result}")
        failed += 1

    # Test 4
    result = squirrel_play(90, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(90, False) expected True, got {result}")
        failed += 1

    # Test 5
    result = squirrel_play(90, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(90, True) expected True, got {result}")
        failed += 1

    # Test 6
    result = squirrel_play(50, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(50, False) expected False, got {result}")
        failed += 1

    # Test 7
    result = squirrel_play(50, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(50, True) expected False, got {result}")
        failed += 1

    # Test 8
    result = squirrel_play(100, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(100, False) expected False, got {result}")
        failed += 1

    # Test 9
    result = squirrel_play(100, True)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(100, True) expected True, got {result}")
        failed += 1

    # Test 10
    result = squirrel_play(105, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(105, True) expected False, got {result}")
        failed += 1

    # Test 11
    result = squirrel_play(59, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(59, False) expected False, got {result}")
        failed += 1

    # Test 12
    result = squirrel_play(59, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(59, True) expected False, got {result}")
        failed += 1

    # Test 13
    result = squirrel_play(60, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: squirrel_play(60, False) expected True, got {result}")
        failed += 1

    print(f"squirrel_play: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
