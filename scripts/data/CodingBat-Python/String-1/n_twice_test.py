"""
Tester for nTwice - CodingBat Python
7 test cases
"""

from n_twice import n_twice


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = n_twice(\"Hello\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: n_twice(\"Hello\", 2) expected \, got {result}")
        failed += 1

    # Test 2
    result = n_twice(\"Chocolate\", 3)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: n_twice(\"Chocolate\", 3) expected \, got {result}")
        failed += 1

    # Test 3
    result = n_twice(\"Chocolate\", 1)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: n_twice(\"Chocolate\", 1) expected \, got {result}")
        failed += 1

    # Test 4
    result = n_twice(\"Chocolate\", 0)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: n_twice(\"Chocolate\", 0) expected \, got {result}")
        failed += 1

    # Test 5
    result = n_twice(\"Hello\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: n_twice(\"Hello\", 4) expected \, got {result}")
        failed += 1

    # Test 6
    result = n_twice(\"Code\", 4)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: n_twice(\"Code\", 4) expected \, got {result}")
        failed += 1

    # Test 7
    result = n_twice(\"Code\", 2)
    if result == \:
        passed += 1
    else:
        print(f"FAIL: n_twice(\"Code\", 2) expected \, got {result}")
        failed += 1

    print(f"n_twice: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
