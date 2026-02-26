"""
Tester for bunnyEars2 - CodingBat Python
8 test cases
"""

from bunny_ears2 import bunny_ears2


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = bunny_ears2(0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(0) expected 0, got {result}")
        failed += 1

    # Test 2
    result = bunny_ears2(1)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(1) expected 2, got {result}")
        failed += 1

    # Test 3
    result = bunny_ears2(2)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(2) expected 5, got {result}")
        failed += 1

    # Test 4
    result = bunny_ears2(3)
    if result == 7:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(3) expected 7, got {result}")
        failed += 1

    # Test 5
    result = bunny_ears2(4)
    if result == 10:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(4) expected 10, got {result}")
        failed += 1

    # Test 6
    result = bunny_ears2(5)
    if result == 12:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(5) expected 12, got {result}")
        failed += 1

    # Test 7
    result = bunny_ears2(6)
    if result == 15:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(6) expected 15, got {result}")
        failed += 1

    # Test 8
    result = bunny_ears2(10)
    if result == 25:
        passed += 1
    else:
        print(f"FAIL: bunny_ears2(10) expected 25, got {result}")
        failed += 1

    print(f"bunny_ears2: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
