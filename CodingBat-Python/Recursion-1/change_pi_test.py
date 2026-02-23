"""
Tester for changePi - CodingBat Python
10 test cases
"""

from change_pi import change_pi


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = change_pi(\"xpix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"xpix\") expected \, got {result}")
        failed += 1

    # Test 2
    result = change_pi(\"pipi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"pipi\") expected \, got {result}")
        failed += 1

    # Test 3
    result = change_pi(\"pip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"pip\") expected \, got {result}")
        failed += 1

    # Test 4
    result = change_pi(\"pi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"pi\") expected \, got {result}")
        failed += 1

    # Test 5
    result = change_pi(\"hip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"hip\") expected \, got {result}")
        failed += 1

    # Test 6
    result = change_pi(\"p\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"p\") expected \, got {result}")
        failed += 1

    # Test 7
    result = change_pi(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"x\") expected \, got {result}")
        failed += 1

    # Test 8
    result = change_pi(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = change_pi(\"pixx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"pixx\") expected \, got {result}")
        failed += 1

    # Test 10
    result = change_pi(\"xyzzy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: change_pi(\"xyzzy\") expected \, got {result}")
        failed += 1

    print(f"change_pi: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
