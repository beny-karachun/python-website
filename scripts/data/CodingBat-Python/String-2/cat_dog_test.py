"""
Tester for catDog - CodingBat Python
13 test cases
"""

from cat_dog import cat_dog


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = cat_dog(\"catdog\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"catdog\") expected True, got {result}")
        failed += 1

    # Test 2
    result = cat_dog(\"catcat\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"catcat\") expected False, got {result}")
        failed += 1

    # Test 3
    result = cat_dog(\"1cat1cadodog\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"1cat1cadodog\") expected True, got {result}")
        failed += 1

    # Test 4
    result = cat_dog(\"catxxdogxxxdog\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"catxxdogxxxdog\") expected False, got {result}")
        failed += 1

    # Test 5
    result = cat_dog(\"catxdogxdogxcat\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"catxdogxdogxcat\") expected True, got {result}")
        failed += 1

    # Test 6
    result = cat_dog(\"catxdogxdogxca\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"catxdogxdogxca\") expected False, got {result}")
        failed += 1

    # Test 7
    result = cat_dog(\"dogdogcat\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"dogdogcat\") expected False, got {result}")
        failed += 1

    # Test 8
    result = cat_dog(\"dogogcat\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"dogogcat\") expected True, got {result}")
        failed += 1

    # Test 9
    result = cat_dog(\"dog\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"dog\") expected False, got {result}")
        failed += 1

    # Test 10
    result = cat_dog(\"cat\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"cat\") expected False, got {result}")
        failed += 1

    # Test 11
    result = cat_dog(\"ca\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"ca\") expected True, got {result}")
        failed += 1

    # Test 12
    result = cat_dog(\"c\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"c\") expected True, got {result}")
        failed += 1

    # Test 13
    result = cat_dog(\"\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: cat_dog(\"\") expected True, got {result}")
        failed += 1

    print(f"cat_dog: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
