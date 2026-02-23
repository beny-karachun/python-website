"""
Tester for bunnyEars - CodingBat Python
9 test cases
"""

from bunny_ears import bunny_ears


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = bunny_ears(0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(0) expected 0, got {result}")
        failed += 1

    # Test 2
    result = bunny_ears(1)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(1) expected 2, got {result}")
        failed += 1

    # Test 3
    result = bunny_ears(2)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(2) expected 4, got {result}")
        failed += 1

    # Test 4
    result = bunny_ears(3)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(3) expected 6, got {result}")
        failed += 1

    # Test 5
    result = bunny_ears(4)
    if result == 8:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(4) expected 8, got {result}")
        failed += 1

    # Test 6
    result = bunny_ears(5)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(5) expected 10, got {result}")
        failed += 1

    # Test 7
    result = bunny_ears(12)
    if result == 24:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(12) expected 24, got {result}")
        failed += 1

    # Test 8
    result = bunny_ears(50)
    if result == 100:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(50) expected 100, got {result}")
        failed += 1

    # Test 9
    result = bunny_ears(234)
    if result == 468:
        passed += 1
    else:
        print(f"FAIL: bunny_ears(234) expected 468, got {result}")
        failed += 1

    print(f"bunny_ears: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
