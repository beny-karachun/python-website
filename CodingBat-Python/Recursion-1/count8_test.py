"""
Tester for count8 - CodingBat Python
18 test cases
"""

from count8 import count8


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count8(8)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count8(8) expected 1, got {result}")
        failed += 1

    # Test 2
    result = count8(818)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count8(818) expected 2, got {result}")
        failed += 1

    # Test 3
    result = count8(8818)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count8(8818) expected 4, got {result}")
        failed += 1

    # Test 4
    result = count8(8088)
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: count8(8088) expected 4, got {result}")
        failed += 1

    # Test 5
    result = count8(123)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count8(123) expected 0, got {result}")
        failed += 1

    # Test 6
    result = count8(81238)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count8(81238) expected 2, got {result}")
        failed += 1

    # Test 7
    result = count8(88788)
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: count8(88788) expected 6, got {result}")
        failed += 1

    # Test 8
    result = count8(8234)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count8(8234) expected 1, got {result}")
        failed += 1

    # Test 9
    result = count8(2348)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count8(2348) expected 1, got {result}")
        failed += 1

    # Test 10
    result = count8(23884)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count8(23884) expected 3, got {result}")
        failed += 1

    # Test 11
    result = count8(0)
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count8(0) expected 0, got {result}")
        failed += 1

    # Test 12
    result = count8(1818188)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: count8(1818188) expected 5, got {result}")
        failed += 1

    # Test 13
    result = count8(8818181)
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: count8(8818181) expected 5, got {result}")
        failed += 1

    # Test 14
    result = count8(1080)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count8(1080) expected 1, got {result}")
        failed += 1

    # Test 15
    result = count8(188)
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count8(188) expected 3, got {result}")
        failed += 1

    # Test 16
    result = count8(88888)
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: count8(88888) expected 9, got {result}")
        failed += 1

    # Test 17
    result = count8(9898)
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count8(9898) expected 2, got {result}")
        failed += 1

    # Test 18
    result = count8(78)
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count8(78) expected 1, got {result}")
        failed += 1

    print(f"count8: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
