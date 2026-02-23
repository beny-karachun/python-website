"""
Tester for repeatFront - CodingBat Python
9 test cases
"""

from repeat_front import repeat_front


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = repeat_front(\"Chocolate\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"Chocolate\", 4) expected \, got {result}")
        failed += 1

    # Test 2
    result = repeat_front(\"Chocolate\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"Chocolate\", 3) expected \, got {result}")
        failed += 1

    # Test 3
    result = repeat_front(\"Ice Cream\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"Ice Cream\", 2) expected \, got {result}")
        failed += 1

    # Test 4
    result = repeat_front(\"Ice Cream\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"Ice Cream\", 1) expected \, got {result}")
        failed += 1

    # Test 5
    result = repeat_front(\"Ice Cream\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"Ice Cream\", 0) expected \, got {result}")
        failed += 1

    # Test 6
    result = repeat_front(\"xyz\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"xyz\", 3) expected \, got {result}")
        failed += 1

    # Test 7
    result = repeat_front(\"\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"\", 0) expected \, got {result}")
        failed += 1

    # Test 8
    result = repeat_front(\"Java\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"Java\", 4) expected \, got {result}")
        failed += 1

    # Test 9
    result = repeat_front(\"Java\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: repeat_front(\"Java\", 1) expected \, got {result}")
        failed += 1

    print(f"repeat_front: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
